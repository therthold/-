

% function transparent
AssertOpenGL;
Screen('Preference','SkipSyncTests', 2);
try
    % front matters
    screens = Screen('Screens');
    screenNumber = max(screens);
    [w, rect] = Screen('OpenWindow', screenNumber, 0);
    HideCursor;
    Priority(MaxPriority(w));
    
    % set the blend function for alpha-blending
    Screen('BlendFunction', w, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    image1 = imread('Koala.jpg');
    [x,y,c] = size(image1);
    % make image 1 opaque by setting its alpha to 255
    image1(:,:,4) = 255+zeros(x,y);
    
    image2 = imread('Jellyfish.jpg');
    [x,y,c] = size(image2);
    % make image 2 opaque in the centre and transparent otherwhere
    [X, Y] = meshgrid(1:x, 1:y);
    alpha = (X-x/2).^2 + (Y-y/2).^2; % calculate the distance from the centre
    alpha = 255*(1-alpha/max(max(alpha))); % scale it into the range of 0 and 255
    image2(:,:,4) = alpha';
    
    tex1 = Screen('MakeTexture', w, image1);
    tex2 = Screen('MakeTexture', w, image2);
    
    dest1 = RectOfMatrix(image1);
    dest2 = OffsetRect(RectOfMatrix(image2), 400, 100);
    Screen('DrawTexture', w, tex1,RectOfMatrix(image1),dest1,0,0,1);
    Screen('DrawTexture', w, tex2,RectOfMatrix(image2),dest2,0,0,1);
    
    % dots can be transparent too
    N = 20;
    x = rect(3)*rand(1,N);
    y = rect(4)*rand(1,N);
    rgba = 255*rand(4, N);
    Screen('DrawDots', w, [x;y], 50, rgba, [0 0],3);
    Screen('Flip', w);
    WaitSecs(8);
    
    Priority(0);
    ShowCursor;
    Screen('CloseAll');
catch
    Priority(0);
    ShowCursor;
    Screen('CloseAll');
    rethrow(lasterror);
end