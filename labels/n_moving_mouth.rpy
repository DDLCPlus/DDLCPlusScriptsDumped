label n_moving_mouth:
    [   0] "images/natsuki/mouth.png"    # image key mouth
    [   1] pos (615, 305)
    [   2] xanchor 0.5 yanchor 0.5
    [   3] parallel:    # this branch runs alongside; parent continues at [52]
    [   4] $ randrangevalue = renpy.random.randint(0, 13)    # choice:
    [   5] unless randrangevalue == 0 goto [7]
    [   6] ease 0.10 yzoom 0.2
    [   7] pass
    [   8] unless randrangevalue == 1 goto [10]
    [   9] ease 0.05 yzoom 0.2
    [  10] pass
    [  11] unless randrangevalue == 2 goto [13]
    [  12] ease 0.075 yzoom 0.2
    [  13] pass
    [  14] pass
    [  15] unless randrangevalue == 3 goto [17]
    [  16] 0.02
    [  17] pass
    [  18] unless randrangevalue == 4 goto [20]
    [  19] 0.04
    [  20] pass
    [  21] unless randrangevalue == 5 goto [23]
    [  22] 0.06
    [  23] pass
    [  24] unless randrangevalue == 6 goto [26]
    [  25] 0.08
    [  26] pass
    [  27] pass
    [  28] unless randrangevalue == 7 goto [30]
    [  29] ease 0.10 yzoom 1
    [  30] pass
    [  31] unless randrangevalue == 8 goto [33]
    [  32] ease 0.05 yzoom 1
    [  33] pass
    [  34] unless randrangevalue == 9 goto [36]
    [  35] ease 0.075 yzoom 1
    [  36] pass
    [  37] pass
    [  38] unless randrangevalue == 10 goto [40]
    [  39] 0.02
    [  40] pass
    [  41] unless randrangevalue == 11 goto [43]
    [  42] 0.04
    [  43] pass
    [  44] unless randrangevalue == 12 goto [46]
    [  45] 0.06
    [  46] pass
    [  47] unless randrangevalue == 13 goto [49]
    [  48] 0.08
    [  49] pass
    [  50] goto [4]
    [  51] return
    [  52] parallel:    # this branch runs alongside; parent continues at [67]
    [  53] $ randrangevalue = renpy.random.randint(0, 2)    # choice:
    [  54] unless randrangevalue == 0 goto [56]
    [  55] 0.2
    [  56] pass
    [  57] unless randrangevalue == 1 goto [59]
    [  58] 0.4
    [  59] pass
    [  60] unless randrangevalue == 2 goto [62]
    [  61] 0.6
    [  62] pass
    [  63] ease 0.2 xzoom 0.4
    [  64] ease 0.2 xzoom 0.8
    [  65] goto [53]
    [  66] return
