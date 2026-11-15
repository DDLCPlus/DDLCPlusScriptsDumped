label dizzy_s_kill_early:
    [   0] pass
    [   1] parallel:    # this branch runs alongside; parent continues at [13]
    [   2] xoffset 0
    [   3] ease 3 xoffset 10
    [   4] ease 3 xoffset 5
    [   5] ease 3 xoffset -5
    [   6] ease 3 xoffset -3
    [   7] ease 3 xoffset -10
    [   8] ease 3 xoffset 0
    [   9] ease 3 xoffset 5
    [  10] ease 3 xoffset 0
    [  11] goto [2]
    [  12] return
    [  13] parallel:    # this branch runs alongside; parent continues at [20]
    [  14] yoffset 0
    [  15] ease 4 yoffset 5
    [  16] ease 8 yoffset -5
    [  17] easein 4 yoffset 0
    [  18] goto [14]
    [  19] return
