label 0acc5fcbec0e4a344bf564ad080de1fc:
    [   0] alpha 1.0
    [   1] xoffset -5
    [   2] 0.1
    [   3] xoffset 5
    [   4] 0.1
    [   5] linear 0.1 alpha 0.6
    [   6] linear 0.1 alpha 0.8
    [   7] 0.1
    [   8] alpha 0
    [   9] $ randrangevalue = renpy.random.randint(0, 3)    # choice:
    [  10] unless randrangevalue == 0 goto [12]
    [  11] 3.25
    [  12] pass
    [  13] unless randrangevalue == 1 goto [15]
    [  14] 2.25
    [  15] pass
    [  16] unless randrangevalue == 2 goto [18]
    [  17] 4.25
    [  18] pass
    [  19] unless randrangevalue == 3 goto [21]
    [  20] 1.25
    [  21] pass
    [  22] goto [0]
