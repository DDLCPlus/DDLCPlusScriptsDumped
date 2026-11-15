label dizzy_faint_effect:
    [   0] pass
    [   1] parallel:    # this branch runs alongside; parent continues at [13]
    [   2] xoffset 0
    [   3] ease 0.75 xoffset 5
    [   4] ease 0.75 xoffset 2.5
    [   5] ease 0.75 xoffset -2.5
    [   6] ease 0.75 xoffset -1.5
    [   7] ease 0.75 xoffset -5
    [   8] ease 0.75 xoffset 0
    [   9] ease 0.75 xoffset 2.5
    [  10] ease 0.75 xoffset 0
    [  11] goto [2]
    [  12] return
    [  13] parallel:    # this branch runs alongside; parent continues at [20]
    [  14] yoffset 0
    [  15] ease 1.0 yoffset 2.5
    [  16] ease 2.0 yoffset -2.5
    [  17] easein 1.0 yoffset 0
    [  18] goto [14]
    [  19] return
