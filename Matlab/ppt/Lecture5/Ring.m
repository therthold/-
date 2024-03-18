% Copyright (c) 2013, Massachusetts Institute of Technology
% This program was presented in the book "Visual Psychophysics:
% From Laboratory to Theory" by Zhong-Lin Lu and Barbara Dosher.
% The book is available at http://mitpress.mit.edu/books/visual-psychophysics

%%% Program Ring.m

function Ring

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

% set up general experimental parameters
keys = {'1' '2' 'esc'};   % response keys for fixation
                            % change and to break
p.randSeed = ClockRandSeed; % use clock to set random number 
                            % generator

% Specify the stimulus
p.radius = 8.5;      % radius in degrees of visual angle
p.innerRad = 0.2;    % room for fixation in degrees of 
                     % visual angle
p.fixColor = 0;      % set fixation color to black
p.period = 20;       % seconds of one cycle of expanding rings
p.repeats = 8;       % number of expansion cycles
p.lag = 12;          % seconds before and after the repeated 
                     % expansion stimuli
p.tf = 7.5;          % flicker frequency in Hz
p.TR = 1;            % duration of each image location in 
                     % expansion, set = TR for fMRI
p.fixDur = [5 15];   % set up range of time intervals between 
                     % fixation color changes

% Compute stimulus parameters
ppd = pi/180 * p.ScreenDistance / p.ScreenHeight * ...
      p.ScreenRect(4); % pixels/degree
m = round(p.radius * ppd * 2);   % stimulus size in pixels
fixSz = round(p.innerRad * ppd); % fixation size in pixels
fixRect = CenterRect([0 0 1 1] * fixSz, p.ScreenRect);
% Compute radii of all rings, so the black/white check is 
% approximately square
nRings = p.period / p.TR;
radius = logspace(log10(p.radius), log10(p.innerRad), ...
         nRings+2);
radius = radius * ppd;
ratio = radius(2) / radius(1); 
dA = 2 * atand((1 - ratio) / (1 + ratio)); 
        % sub-wedge width in deg
nSectors = round(180 / dA) * 2;
dA = 360 / nSectors;
 
% The call to Screen(?MakeTexture?, ) converts a 2D image to a 
% OpenGL texture. One will be the black/white negative of the 
% other, used for flicker
img = ones(m) * p.ScreenBackground; 
        % Create 2 textures with background color
tex(1) = Screen('MakeTexture', windowPtr, img, 0 ,0, 2);
tex(2) = Screen('MakeTexture', windowPtr, img, 0 ,0, 2);
 
rect = CenterRect([0 0 2 2] * radius(1), [0 0 m m]); 
        % Color the whole annulus white
nPixels = diff(radius([3 1]));
Screen('FrameArc', tex(1), 1, rect, 0, 360, nPixels);
Screen('FrameArc', tex(2), 1, rect, 0, 360, nPixels);
 
for i = 1 : 2   % add black to make checks  
    rect = CenterRect([0 0 2 2] * radius(i), [0 0 m m]);
    nPixels = diff(radius([i+1 i]));
    for j = 0 : 2 : nSectors-1 % every other sector
        for iTex = 1 : 2 
            ang0 = (j + mod(i + iTex, 2)) * dA;
            Screen('FrameArc', tex(iTex), 0, rect, ang0, ...
                   dA, nPixels);
        end
    end
end

% Set up onset times of fixation color changes
p.recLabel = {'fixChangeSecs' 'respTime'};
secs = p.period * p.repeats; % total seconds to run
durs = rand(round(secs / p.fixDur(1)), 1);  % [0 1]
durs = durs * diff(p.fixDur) + p.fixDur(1); % [5 15]
durs = cumsum(durs);
durs(durs >= secs) = [];
rec = nan(length(durs), length(p.recLabel));
rec(:, 1) = durs;  % record onset times of fixation 
                   % color changes

% Prioritize display to optimize display timing
Priority(MaxPriority(windowPtr));
 
% Start experiment with instructions
str = sprintf(['Please fixate at the center of the ' ...
      'screen.\n\n' 'Press 1 for white or 2 for red.\n\n' ...
      'Press 5 to start.']);
DrawFormattedText(windowPtr, str, 'center', 'center', 1);
        % Draw Instruction text string centered in window
Screen('Flip', windowPtr);  
        % flip the text image into active buffer
WaitTill('5');      
        % wait till 5 (trigger to start display) is pressed
 
Screen('FillOval', windowPtr, 1, fixRect); % draw fixation
startSecs = Screen('Flip', windowPtr);  
        % flip the fixation image into active buffer
p.start = datestr(now);                    % record start time
 
t0 = startSecs + p.lag;  % planned onset of wedge
durs = [durs; inf] + t0; % absolute time to change fixation
iFix = 1;                % index for fixation color: 
                         % 1 or 2 for white and red fixation
fixColor = [1 1 1; 1 0 0]; % set color tables for 
                           % white and red
i = 1;                   % index for fixation change
endSecs = t0 + p.period * p.repeats; 
        % end time of cycle of rings
key = ReadKey; key = ReadKey; 
        % ReadKey twice to speed up subsequent calls to it.
validResp = 1;           % set valid response flag to 1
WaitTill(t0 - 0.02);     % wait for wedge start time
 
Screen('FillOval', windowPtr, 1, fixRect);
vbl = Screen('Flip', windowPtr, t0 - 1 / p.ScreenFrameRate);
t0 = vbl;
while vbl < endSecs  % show the expanding ring stimulus with 
                     % fixation changes and collect responses 
                     % and record the response times
    iTex = (mod(vbl - t0, 1 / p.tf) < 0.5 / p.tf) + 1;
    iRing = nRings - floor(mod(vbl - t0, p.period) / p.TR); 
                     % expanding
    % iRing = 1 + floor(mod(vbl - t0, p.period) / p.TR); 
                     % shrinking
    rect = CenterRect([0 0 2 2] * radius(iRing), ...
           p.ScreenRect);
    if vbl > durs(i)
        iFix = 3 - iFix;  % change fixation color between 
                          % red and white
        t1 = vbl + 1 / p.ScreenFrameRate; 
                          % fixation change time
        i = i + 1;
    end 
    Screen('DrawTexture', windowPtr, tex(iTex), [], rect);
    Screen('FillOval', windowPtr, fixColor(iFix, :), fixRect);
    vbl = Screen('Flip', windowPtr);
    
    key = ReadKey(keys);
    if strcmp(key, 'esc'), break; end % to stop
    if isempty(key)
        validResp = 1; % key released, next response 
                       % will be valid
    elseif validResp
        validResp = 0; % debouncing
        rec(i, 2) = vbl - t1;  % record response time
    end
end
 
Screen('FillOval', windowPtr, fixColor(iFix, :), fixRect);
Screen('Flip', windowPtr);
 
WaitTill(endSecs +p.lag, 'esc'); % wait for p.lag after wedge
p.finish = datestr(now);         % record finish time
 
save Ring_rst.mat rec p;         % save the results



%% System Reinstatement Module

Priority(0);  % restore priority
sca; % close window and textures, restore color lookup table

