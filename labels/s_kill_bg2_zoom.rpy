label s_kill_bg2_zoom:
    # nested label 6748bcb2fab0d43479555b7c2e057c54 starts at [0]
    [   0] label contains 6748bcb2fab0d43479555b7c2e057c54    # nested entry point
    [   1] call s_kill_bg2
    [   2] xalign 0.2 yalign 0.3 zoom 2.0*0.6666667
    [   3] parallel:    # this branch runs alongside; parent continues at [7]
    [   4] pass
    [   5] call dizzy_s_kill_bg_zoom
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [20]
    [   8] alpha 0.2
    [   9] linear 0.25 alpha 0.2
    [  10] linear 0.25 alpha 0.25
    [  11] linear 0.25 alpha 0.2
    [  12] linear 0.25 alpha 0.3
    [  13] linear 0.25 alpha 0.25
    [  14] linear 0.25 alpha 0.35
    [  15] linear 0.25 alpha 0.3
    [  16] linear 0.25 alpha 0.35
    [  17] linear 0.25 alpha 0.2
    [  18] goto [8]
    [  19] return
