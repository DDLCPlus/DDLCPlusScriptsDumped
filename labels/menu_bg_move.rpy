label menu_bg_move:
    [   0] pass
    [   1] call topleft
    [   2] parallel:    # this branch runs alongside; parent continues at [7]
    [   3] ypos 0
    [   4] 0.65
    [   5] ease_cubic 2.5 ypos -500
    [   6] return
