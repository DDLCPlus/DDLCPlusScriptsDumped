label yuri stab_6_eyes:
    [   0] "yuri/stab/6-eyes.png"    # image key 6-eyes
    [   1] size(960, 960)
    [   2] pass
    [   3] parallel:    # this branch runs alongside; parent continues at [17]
    [   4] $ randrangevalue = renpy.random.randint(0, 2)    # choice:
    [   5] unless randrangevalue == 0 goto [7]
    [   6] xoffset 0.5
    [   7] pass
    [   8] unless randrangevalue == 1 goto [10]
    [   9] xoffset 0
    [  10] pass
    [  11] unless randrangevalue == 2 goto [13]
    [  12] xoffset -0.5
    [  13] pass
    [  14] 0.2
    [  15] goto [4]
    [  16] return
    [  17] parallel:    # this branch runs alongside; parent continues at [143]
    [  18] $ randrangevalue = renpy.random.randint(0, 35)    # choice:
    [  19] unless randrangevalue == 0 goto [21]
    [  20] yoffset 0.5
    [  21] pass
    [  22] unless randrangevalue == 1 goto [24]
    [  23] yoffset 0
    [  24] pass
    [  25] unless randrangevalue == 2 goto [27]
    [  26] yoffset -0.5
    [  27] pass
    [  28] 0.2
    [  29] unless randrangevalue == 3 goto [31]
    [  30] yoffset 0.5
    [  31] pass
    [  32] unless randrangevalue == 4 goto [34]
    [  33] yoffset 0
    [  34] pass
    [  35] unless randrangevalue == 5 goto [37]
    [  36] yoffset -0.5
    [  37] pass
    [  38] 0.2
    [  39] unless randrangevalue == 6 goto [41]
    [  40] yoffset 0.5
    [  41] pass
    [  42] unless randrangevalue == 7 goto [44]
    [  43] yoffset 0
    [  44] pass
    [  45] unless randrangevalue == 8 goto [47]
    [  46] yoffset -0.5
    [  47] pass
    [  48] 0.2
    [  49] unless randrangevalue == 9 goto [51]
    [  50] yoffset 0.5
    [  51] pass
    [  52] unless randrangevalue == 10 goto [54]
    [  53] yoffset 0
    [  54] pass
    [  55] unless randrangevalue == 11 goto [57]
    [  56] yoffset -0.5
    [  57] pass
    [  58] 0.2
    [  59] unless randrangevalue == 12 goto [61]
    [  60] yoffset 0.5
    [  61] pass
    [  62] unless randrangevalue == 13 goto [64]
    [  63] yoffset 0
    [  64] pass
    [  65] unless randrangevalue == 14 goto [67]
    [  66] yoffset -0.5
    [  67] pass
    [  68] 0.2
    [  69] unless randrangevalue == 15 goto [71]
    [  70] yoffset 0.5
    [  71] pass
    [  72] unless randrangevalue == 16 goto [74]
    [  73] yoffset 0
    [  74] pass
    [  75] unless randrangevalue == 17 goto [77]
    [  76] yoffset -0.5
    [  77] pass
    [  78] 0.2
    [  79] unless randrangevalue == 18 goto [81]
    [  80] yoffset 0.5
    [  81] pass
    [  82] unless randrangevalue == 19 goto [84]
    [  83] yoffset 0
    [  84] pass
    [  85] unless randrangevalue == 20 goto [87]
    [  86] yoffset -0.5
    [  87] pass
    [  88] 0.2
    [  89] unless randrangevalue == 21 goto [91]
    [  90] yoffset 0.5
    [  91] pass
    [  92] unless randrangevalue == 22 goto [94]
    [  93] yoffset 0
    [  94] pass
    [  95] unless randrangevalue == 23 goto [97]
    [  96] yoffset -0.5
    [  97] pass
    [  98] 0.2
    [  99] unless randrangevalue == 24 goto [101]
    [ 100] yoffset 0.5
    [ 101] pass
    [ 102] unless randrangevalue == 25 goto [104]
    [ 103] yoffset 0
    [ 104] pass
    [ 105] unless randrangevalue == 26 goto [107]
    [ 106] yoffset -0.5
    [ 107] pass
    [ 108] 0.2
    [ 109] unless randrangevalue == 27 goto [111]
    [ 110] yoffset 0.5
    [ 111] pass
    [ 112] unless randrangevalue == 28 goto [114]
    [ 113] yoffset 0
    [ 114] pass
    [ 115] unless randrangevalue == 29 goto [117]
    [ 116] yoffset -0.5
    [ 117] pass
    [ 118] 0.2
    [ 119] unless randrangevalue == 30 goto [121]
    [ 120] yoffset 0.5
    [ 121] pass
    [ 122] unless randrangevalue == 31 goto [124]
    [ 123] yoffset 0
    [ 124] pass
    [ 125] unless randrangevalue == 32 goto [127]
    [ 126] yoffset -0.5
    [ 127] pass
    [ 128] 0.2
    [ 129] unless randrangevalue == 33 goto [131]
    [ 130] yoffset 0.5
    [ 131] pass
    [ 132] unless randrangevalue == 34 goto [134]
    [ 133] yoffset 0
    [ 134] pass
    [ 135] unless randrangevalue == 35 goto [137]
    [ 136] yoffset -0.5
    [ 137] pass
    [ 138] 0.08
    [ 139] yoffset 0
    [ 140] easeout 1.0 yoffset -15
    [ 141] linear 10 yoffset -15
    [ 142] return
