1% Copyright (c) 2013, Massachusetts Institute of Technology
% This program was presented in the book "Visual Psychophysics:
% From Laboratory to Theory" by Zhong-Lin Lu and Barbara Dosher.
% The book is available at http://mitpress.mit.edu/books/visual-psychophysics

%%% Program Wedge.m

 

%% Display Setup Module
% Define display parameters
whichScreen = max(Screen('screens'));
p.ScreenDistance = 30;  % in inches
p.ScreenHeight = 15;    % in inches
p.ScreenGamma = 2;  % from monitor calibration
p.maxLuminance = 100; % from monitor calibration
p.ScreenBackground = 0.5; 

% Open the display window, set up lookup table, and hide the 
% mouse cursor
if exist('onCleanup', 'class'), oC_Obj = onCleanup(@()sca); end  
        % close any pre-existing PTB Screen window
% Prepare setup of imaging pipeline for onscreen window. 
PsychImaging('PrepareConfiguration'); % First step in starting
                                      % pipeline
PsychImaging('AddTask', 'General',  'FloatingPoint32BitIfPossible');  
        % set up a 32-bit floatingpoint framebuffer
PsychImaging('AddTask', 'General', 'NormalizedHighresColorRange');   
        % normalize the color range ([0, 1] corresponds 
        % to [min, max])
PsychImaging('AddTask', 'General', 'EnablePseudoGrayOutput'); 
        % enable high gray level resolution output with 
        % bitstealing
PsychImaging('AddTask','FinalFormatting',  'DisplayColorCorrection','SimpleGamma');  
        % setup Gamma correction method using simple power 
        % function for all color channels 
[windowPtr p.ScreenRect] = PsychImaging('OpenWindow', whichScreen, p.ScreenBackground);  
        % Finishes the setup phase for imaging pipeline
        % creates an onscreen window, performs all remaining  
        % configuration steps
PsychColorCorrection('SetEncodingGamma', windowPtr, 1/ p.ScreenGamma);  
% set Gamma for all color channels
HideCursor;  % Hide the mouse cursor 

% Get frame rate and set screen font
p.ScreenFrameRate = FrameRate(windowPtr); 
        % get current frame rate
Screen('TextFont', windowPtr, 'Times'); 
        % set the font for the screen to Times
Screen('TextSize', windowPtr, 24); % set the font size 
                                   % for the screen to 24


%% Experimental Module

% Specify general experiment parameters
keys = {'1' '2' 'esc'};      % response keys for fixation 
                             % change and to break
p.randSeed = ClockRandSeed;  % use clock to set random number 
                             % generator

% Specify the stimulus 
p.radius = 8.5;     % radius in degrees of visual angle
p.innerRad = 0.2;   % room for fixation in degrees of visual
                    %  angle
p.startAng = 0;     % starting angle of wedge
p.wedgeDeg = 45;    % Wedge width in degrees of visual angle
p.fixColor = 0;     % fixation color set to black
p.period = 32;      % seconds of one full rotation
p.repeats = 8;      % total number of full rotations of 
                    % the wedge 
p.lag = 12;         % seconds of blank screen before and after 
                    % the 8 repeats of wedge stimuli
p.tf = 7.5;         % flicker frequency in Hz
p.TR = 1;           % duration of each position, set equal 
                    % to TR for fMRI
p.fixDur = [5 15];  % set up range of time intervals between
                    % fixation color changes

% Compute stimulus parameters
ppd = pi/180 * p.ScreenDistance / p.ScreenHeight * ...
      p.ScreenRect(4); % pixels/degree
m = round(p.radius * ppd * 2);   % stimulus size in pixels
fixSz = round(p.innerRad * ppd); % radius of fixation circle 
                                 % in pixels
fixRect = CenterRect([0 0 1 1] * fixSz, p.ScreenRect);  
        % position fixation on the screen
dA = p.wedgeDeg / 4; % width of each of 4 sub-sectors of 
                     % the wedge in degrees
% Compute radial height of each subsector as the tangent of 
% its half-width in deg
tanAng = tand(dA / 2); 
ratio = (1 - tanAng) / (1 + tanAng);
nRings = floor(log(p.innerRad / p.radius) / log(ratio));
radius = p.radius * ppd * ratio.^ (0 : nRings-1);
        % The call to Screen(?MakeTexture?, ) converts a 2D
        % image to a OpenGL texture. one will be the 
        % black/white negative of the other, used for flicker
img = ones(m) * p.ScreenBackground; 
tex(1) = Screen('MakeTexture', windowPtr, img, 0 ,0, 2);
tex(2) = Screen('MakeTexture', windowPtr, img, 0 ,0, 2);
nPixels = diff(radius([nRings 1])); 
       % Fill the whole wedge with white
Screen('FrameArc', tex(1), 1, [], 0, p.wedgeDeg, nPixels);
Screen('FrameArc', tex(2), 1, [], 0, p.wedgeDeg, nPixels);
       % Screen(?FrameArc, ) draws an arc in a texture with 
       % starting angle, angle of arc and width of line

for i = 1 : nRings-1  % Fill every other sector with black 
                      % to make checker pattern
    rect = CenterRect([0 0 2 2] * radius(i), [0 0 m m]);
    nPixels = diff(radius([i+1 i]));
    for j = [0 2] % every other sector
        for iTex = 1 : 2 
            ang0 = (j + mod(i + iTex, 2)) * dA;
            Screen('FrameArc', tex(iTex), 0, rect, ang0, ...
                   dA, nPixels);
        end
    end
end
 
% Set up onset times of fixation color changes
p.recLabel = {'fixChangeSecs' 'respTime'}; 
        % labels of columns of condition/data rec
secs = p.period * p.repeats; % total seconds to run
durs = rand(round(secs / p.fixDur(1)), 1); % [0 1]
durs = durs * diff(p.fixDur) + p.fixDur(1); % [5 15]
durs = cumsum(durs);
durs(durs >= secs) = [];
rec = nan(length(durs), length(p.recLabel));
rec(:, 1) = durs; % record onset times of fixation 
                  % color changes
 
% Prioritize display to optimize display timing
Priority(MaxPriority(windowPtr));
 
% Start experiment with instructions
str = sprintf(['Please fixate at the center of the ' ...
       'screen. \n\n' 'Press 1 for white fixation or 2 for ' ...
       'red fixation.\n\nPress 5 to start.']);
DrawFormattedText(windowPtr, str, 'center', 'center', 1);
        % Draw Instruction text string centered in window
Screen('Flip', windowPtr);  
        % flip the text image into active frame buffer
WaitTill('5');    % wait till 5 (trigger to start the display)
                  % is pressed
 
Screen('FillOval', windowPtr, 1, fixRect); % draw fixation
startSecs = Screen('Flip', windowPtr);  
        % flip the fixation image into active buffer
p.start = datestr(now);    % record start time
 
t0 = startSecs + p.lag;    % planned onset of wedge
durs = [durs; inf] + t0;   % absolute time to change fixation
iFix = 1;                  % index for fixation color: 1 or 2
                           % for white and red fixation
fixColor = [1 1 1; 1 0 0]; % set up color tables for white and
                           % red fixation colors
i = 1;                     % index to count fixation changes
dA = 360 / p.period;       % rotation in degrees per second
endSecs = t0 + p.period * p.repeats; 
                           % end time of wedge rotations
key = ReadKey; key = ReadKey;  
        % ReadKey twice to speed up subsequent calls to it.
validResp = 1;             % preset a valid response flag to 1    
WaitTill(t0 - 0.02); % wait for start time for wedge display
 
Screen('FillOval', windowPtr, 1, fixRect);
vbl = Screen('Flip', windowPtr, t0 - 1 / p.ScreenFrameRate);
t0 = vbl;
while vbl < endSecs  % show the wedge stimulus with fixation 
                     % changes and collect responses and 
                     % record the response times
    iTex = (mod(vbl - t0, 1 / p.tf) < 0.5 / p.tf) + 1;
    ang = p.startAng + floor((vbl - t0) / p.TR) * dA;
    if vbl > durs(i)
        iFix = 3 - iFix; % change fixation color between red
                         % and white
        t1 = vbl + 1 / p.ScreenFrameRate; 
                         % fixation change time
        i = i + 1;
    end 
    Screen('DrawTexture', windowPtr, tex(iTex), [], [], ang);
    Screen('FillOval', windowPtr, fixColor(iFix, :), fixRect);
    vbl = Screen('Flip', windowPtr);
    
    key = ReadKey(keys);
    if strcmp(key, 'esc'), break; end 
        % stop the dispay if ?esc? is pressed
    if isempty(key)
        validResp = 1; 
        % reset response flag, the next response will be valid
    elseif validResp
        validResp = 0; 
        rec(i, 2) = vbl - t1;  % record response time
    end
end
 
Screen('FillOval', windowPtr, fixColor(iFix, :), fixRect);
Screen('Flip', windowPtr);
 
WaitTill(endSecs +p.lag, 'esc'); % wait for p.lag after wedge
p.finish = datestr(now);         % record finish time
 
save Wedge_rst.mat rec p;        % save the results


%% System Reinstatement Module

Priority(0);  % restore priority
sca; % close window and textures, restore color lookup table
 