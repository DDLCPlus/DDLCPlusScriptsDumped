label dizzy_monika_scare:
    [   0] pass
    [   1] parallel:    # this branch runs alongside; parent continues at [13]
    [   2] xoffset 0
    [   3] ease 0.0075 xoffset 15
    [   4] ease 0.0075 xoffset 7.5
    [   5] ease 0.0075 xoffset -7.5
    [   6] ease 0.0075 xoffset -4.5
    [   7] ease 0.0075 xoffset -15
    [   8] ease 0.0075 xoffset 0
    [   9] ease 0.0075 xoffset 7.5
    [  10] ease 0.0075 xoffset 0
    [  11] goto [2]
    [  12] return
    [  13] parallel:    # this branch runs alongside; parent continues at [20]
    [  14] yoffset 0
    [  15] ease 0.01 yoffset 7.5
    [  16] ease 0.02 yoffset -7.5
    [  17] easein 0.01 yoffset 0
    [  18] goto [14]
    [  19] return
