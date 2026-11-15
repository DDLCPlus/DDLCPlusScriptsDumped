label s_kill2_zoom:
    # nested label b5beb9ddfb2c4114c87eb5dfd5f7a54f starts at [0]
    [   0] label contains b5beb9ddfb2c4114c87eb5dfd5f7a54f    # nested entry point
    [   1] call s_kill2
    [   2] call truecenter
    [   3] zoom 2.0 xalign 0.5 yalign 0.05
    [   4] parallel:    # this branch runs alongside; parent continues at [8]
    [   5] pass
    [   6] call dizzy_s_kill_zoom
    [   7] return
    [   8] parallel:    # this branch runs alongside; parent continues at [21]
    [   9] alpha 0.3
    [  10] linear 0.25 alpha 0.3
    [  11] linear 0.25 alpha 0.4
    [  12] linear 0.25 alpha 0.3
    [  13] linear 0.25 alpha 0.5
    [  14] linear 0.25 alpha 0.4
    [  15] linear 0.25 alpha 0.6
    [  16] linear 0.25 alpha 0.5
    [  17] linear 0.25 alpha 0.6
    [  18] linear 0.25 alpha 0.4
    [  19] goto [9]
    [  20] return
