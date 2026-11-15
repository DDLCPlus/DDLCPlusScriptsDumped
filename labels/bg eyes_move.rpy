label bg eyes_move:
    [   0] "images/bg/eyes.png"    # image key eyes
    [   1] parallel:    # this branch runs alongside; parent continues at [6]
    [   2] yoffset 720 ytile 2
    [   3] linear 0.5 yoffset 0
    [   4] goto [2]
    [   5] return
    [   6] parallel:    # this branch runs alongside; parent continues at [19]
    [   7] 0.1
    [   8] $ randrangevalue = renpy.random.randint(0, 1)    # choice:
    [   9] unless randrangevalue == 0 goto [13]
    [  10] xoffset 20
    [  11] 0.05
    [  12] xoffset 0
    [  13] pass
    [  14] unless randrangevalue == 1 goto [16]
    [  15] xoffset 0
    [  16] pass
    [  17] goto [7]
    [  18] return
