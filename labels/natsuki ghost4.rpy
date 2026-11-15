label natsuki ghost4:
    [   0] call natsuki ghost3
    [   1] parallel:    # this branch runs alongside; parent continues at [4]
    [   2] easeout 0.25 zoom 4.5 yoffset 1200
    [   3] return
    [   4] parallel:    # this branch runs alongside; parent continues at [9]
    [   5] ease 0.025 xoffset -20
    [   6] ease 0.025 xoffset 20
    [   7] goto [5]
    [   8] return
    [   9] 0.25
    [  10] call black
