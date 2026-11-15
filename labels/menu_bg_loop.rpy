label menu_bg_loop:
    [   0] pass
    [   1] call topleft
    [   2] parallel:    # this branch runs alongside; parent continues at [7]
    [   3] xoffset 0 yoffset 0
    [   4] linear 3.0 xoffset -100 yoffset -100
    [   5] goto [3]
    [   6] return
