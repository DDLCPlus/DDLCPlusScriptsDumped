label splash_glitch_m:
    [   0] pass
    [   1] "gui/menu_art_m.png"    # image key menu_art_m
    [   2] zoom 0.3333
    [   3] xpos 0.5 ypos 0.5
    [   4] 0.1
    [   5] parallel:    # this branch runs alongside; parent continues at [10]
    [   6] xpos 0.3 ypos 1.2
    [   7] linear 0.08 ypos 0.1
    [   8] goto [6]
    [   9] return
    [  10] parallel:    # this branch runs alongside; parent continues at [14]
    [  11] 0.5
    [  12] alpha 0.0
    [  13] return
