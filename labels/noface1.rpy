label noface1:
    # nested label d56c253139fc56e46b7f08b0d966e7c1 starts at [2]
    # nested label d449dc03484a21c4f94414bee7a7c022 starts at [3]
    # nested label acdeb509fb3de1040b8c48544be1516c starts at [11]
    [   0] call topleft
    [   1] xtile 10 ytile 10
    [   2] label block d56c253139fc56e46b7f08b0d966e7c1    # nested entry point
    [   3] label block d449dc03484a21c4f94414bee7a7c022    # nested entry point
    [   4] $ randrangevalue = renpy.random.randint(0, 1)    # choice:
    [   5] unless randrangevalue == 0 goto [7]
    [   6] "images/sayori/noface1.png"    # image key noface1
    [   7] pass
    [   8] unless randrangevalue == 1 goto [10]
    [   9] "images/sayori/noface1b.png"    # image key noface1b
    [  10] pass
    [  11] label block acdeb509fb3de1040b8c48544be1516c    # nested entry point
    [  12] $ randrangevalue = renpy.random.randint(0, 4)    # choice:
    [  13] unless randrangevalue == 0 goto [15]
    [  14] 0.075
    [  15] pass
    [  16] unless randrangevalue == 1 goto [18]
    [  17] 0.3
    [  18] pass
    [  19] unless randrangevalue == 2 goto [21]
    [  20] 0.4
    [  21] pass
    [  22] unless randrangevalue == 3 goto [24]
    [  23] 0.5
    [  24] pass
    [  25] unless randrangevalue == 4 goto [27]
    [  26] 0.6
    [  27] pass
    [  28] goto [3]
