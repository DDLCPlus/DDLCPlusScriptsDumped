label y_cg2_dust1:
    [   0] call y_cg2_dust1_original
    [   1] size(1280,720)
    [   2] pass
    [   3] parallel:    # this branch runs alongside; parent continues at [11]
    [   4] alpha 1.00
    [   5] 6.0
    [   6] linear 1.0 alpha 0.35
    [   7] 1.0
    [   8] linear 1.0 alpha 1.0
    [   9] goto [4]
    [  10] return
    [  11] parallel:    # this branch runs alongside; parent continues at [18]
    [  12] alpha 0
    [  13] linear 2.0 alpha 1.0
    [  14] 10.0
    [  15] linear 2.0 alpha 0
    [  16] goto [12]
    [  17] return
    [  18] parallel:    # this branch runs alongside; parent continues at [23]
    [  19] xoffset 100 yoffset -100
    [  20] linear 14.0 xoffset -100 yoffset 100
    [  21] goto [19]
    [  22] return
