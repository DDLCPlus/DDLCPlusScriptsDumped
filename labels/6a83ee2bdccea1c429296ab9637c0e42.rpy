label 6a83ee2bdccea1c429296ab9637c0e42:
    [   0] $ randrangevalue = renpy.random.randint(0, 12)    # choice:
    [   1] unless randrangevalue == 0 goto [3]
    [   2] ease 0.25 alpha 0.1
    [   3] pass
    [   4] unless randrangevalue == 1 goto [6]
    [   5] ease 0.25 alpha 0.125
    [   6] pass
    [   7] unless randrangevalue == 2 goto [9]
    [   8] ease 0.25 alpha 0.15
    [   9] pass
    [  10] unless randrangevalue == 3 goto [12]
    [  11] ease 0.25 alpha 0.175
    [  12] pass
    [  13] unless randrangevalue == 4 goto [15]
    [  14] ease 0.25 alpha 0.2
    [  15] pass
    [  16] unless randrangevalue == 5 goto [18]
    [  17] ease 0.25 alpha 0.225
    [  18] pass
    [  19] unless randrangevalue == 6 goto [21]
    [  20] ease 0.25 alpha 0.25
    [  21] pass
    [  22] unless randrangevalue == 7 goto [24]
    [  23] ease 0.25 alpha 0.275
    [  24] pass
    [  25] unless randrangevalue == 8 goto [27]
    [  26] ease 0.25 alpha 0.3
    [  27] pass
    [  28] pass
    [  29] unless randrangevalue == 9 goto [31]
    [  30] pass
    [  31] pass
    [  32] unless randrangevalue == 10 goto [34]
    [  33] 0.25
    [  34] pass
    [  35] unless randrangevalue == 11 goto [37]
    [  36] 0.5
    [  37] pass
    [  38] unless randrangevalue == 12 goto [40]
    [  39] 0.75
    [  40] pass
    [  41] goto [0]
