label splash_glitch:
    [   0] pass
    [   1] "images/bg/splash-comp-glitch.png"    # image key splash-comp-glitch
    [   2] size(1280, 720)
    [   3] alpha 0.0
    [   4] 0.5
    [   5] linear 0.5 alpha 1.0
    [   6] 2.5
    [   7] linear 0.5 alpha 0.0
    [   8] "gui/menu_bg.png"    # image key menu_bg
    [   9] call topleft
    [  10] alpha 0.0
    [  11] parallel:    # this branch runs alongside; parent continues at [16]
    [  12] xoffset 0 yoffset 0
    [  13] linear 0.25 xoffset -100 yoffset -100
    [  14] goto [12]
    [  15] return
    [  16] parallel:    # this branch runs alongside; parent continues at [19]
    [  17] linear 0.5 alpha 1.0
    [  18] return
    [  19] parallel:    # this branch runs alongside; parent continues at [24]
    [  20] ypos 0
    [  21] 1.0
    [  22] easeout 1.0 ypos -500
    [  23] return
