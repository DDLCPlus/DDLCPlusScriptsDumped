label yuri dragon:
    [   0] call yuri 3a
    [   1] 0.25
    [   2] parallel:    # this branch runs alongside; parent continues at [40]
    [   3] "yuri/dragon1.png"    # image key dragon1
    [   4] 0.01
    [   5] "yuri/dragon2.png"    # image key dragon2
    [   6] 0.01
    [   7] "yuri/dragon1.png"    # image key dragon1
    [   8] 0.01
    [   9] "yuri/dragon2.png"    # image key dragon2
    [  10] 0.01
    [  11] "yuri/dragon1.png"    # image key dragon1
    [  12] 0.01
    [  13] "yuri/dragon2.png"    # image key dragon2
    [  14] 0.01
    [  15] "yuri/dragon1.png"    # image key dragon1
    [  16] 0.01
    [  17] "yuri/dragon2.png"    # image key dragon2
    [  18] 0.01
    [  19] "yuri/dragon1.png"    # image key dragon1
    [  20] 0.01
    [  21] "yuri/dragon2.png"    # image key dragon2
    [  22] 0.01
    [  23] "yuri/dragon1.png"    # image key dragon1
    [  24] 0.01
    [  25] "yuri/dragon2.png"    # image key dragon2
    [  26] 0.01
    [  27] "yuri/dragon1.png"    # image key dragon1
    [  28] 0.01
    [  29] "yuri/dragon2.png"    # image key dragon2
    [  30] 0.01
    [  31] "yuri/dragon1.png"    # image key dragon1
    [  32] 0.01
    [  33] "yuri/dragon2.png"    # image key dragon2
    [  34] 0.01
    [  35] "yuri/dragon1.png"    # image key dragon1
    [  36] 0.01
    [  37] "yuri/dragon2.png"    # image key dragon2
    [  38] 0.01
    [  39] return
    [  40] parallel:    # this branch runs alongside; parent continues at [142]
    [  41] 0.01
    [  42] $ randrangevalue = renpy.random.randint(0, 8)    # choice:
    [  43] unless randrangevalue == 0 goto [50]
    [  44] xoffset -1
    [  45] xoffset -2
    [  46] xoffset -5
    [  47] xoffset -6
    [  48] xoffset -9
    [  49] xoffset -10
    [  50] pass
    [  51] 0.01
    [  52] xoffset 0
    [  53] 0.01
    [  54] unless randrangevalue == 1 goto [61]
    [  55] xoffset -1
    [  56] xoffset -2
    [  57] xoffset -5
    [  58] xoffset -6
    [  59] xoffset -9
    [  60] xoffset -10
    [  61] pass
    [  62] 0.01
    [  63] xoffset 0
    [  64] 0.01
    [  65] unless randrangevalue == 2 goto [72]
    [  66] xoffset -1
    [  67] xoffset -2
    [  68] xoffset -5
    [  69] xoffset -6
    [  70] xoffset -9
    [  71] xoffset -10
    [  72] pass
    [  73] 0.01
    [  74] xoffset 0
    [  75] 0.01
    [  76] unless randrangevalue == 3 goto [83]
    [  77] xoffset -1
    [  78] xoffset -2
    [  79] xoffset -5
    [  80] xoffset -6
    [  81] xoffset -9
    [  82] xoffset -10
    [  83] pass
    [  84] 0.01
    [  85] xoffset 0
    [  86] 0.01
    [  87] unless randrangevalue == 4 goto [94]
    [  88] xoffset -1
    [  89] xoffset -2
    [  90] xoffset -5
    [  91] xoffset -6
    [  92] xoffset -9
    [  93] xoffset -10
    [  94] pass
    [  95] 0.01
    [  96] xoffset 0
    [  97] 0.01
    [  98] unless randrangevalue == 5 goto [105]
    [  99] xoffset -1
    [ 100] xoffset -2
    [ 101] xoffset -5
    [ 102] xoffset -6
    [ 103] xoffset -9
    [ 104] xoffset -10
    [ 105] pass
    [ 106] 0.01
    [ 107] xoffset 0
    [ 108] 0.01
    [ 109] unless randrangevalue == 6 goto [116]
    [ 110] xoffset -1
    [ 111] xoffset -2
    [ 112] xoffset -5
    [ 113] xoffset -6
    [ 114] xoffset -9
    [ 115] xoffset -10
    [ 116] pass
    [ 117] 0.01
    [ 118] xoffset 0
    [ 119] 0.01
    [ 120] unless randrangevalue == 7 goto [127]
    [ 121] xoffset -1
    [ 122] xoffset -2
    [ 123] xoffset -5
    [ 124] xoffset -6
    [ 125] xoffset -9
    [ 126] xoffset -10
    [ 127] pass
    [ 128] 0.01
    [ 129] xoffset 0
    [ 130] 0.01
    [ 131] unless randrangevalue == 8 goto [138]
    [ 132] xoffset -1
    [ 133] xoffset -2
    [ 134] xoffset -5
    [ 135] xoffset -6
    [ 136] xoffset -9
    [ 137] xoffset -10
    [ 138] pass
    [ 139] 0.01
    [ 140] xoffset 0
    [ 141] return
    [ 142] 0.6
    [ 143] xoffset 0
    [ 144] call yuri 3a
