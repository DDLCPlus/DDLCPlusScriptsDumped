label end_glitch4:
    [   0] 28.65
    [   1] parallel:    # this branch runs alongside; parent continues at [8]
    [   2] "bg/end-glitch4.jpg"    # image key end-glitch4
    [   3] 1.25
    [   4] "bg/end-glitch3.jpg"    # image key end-glitch3
    [   5] 0.1
    [   6] goto [2]
    [   7] return
    [   8] parallel:    # this branch runs alongside; parent continues at [14]
    [   9] yoffset 1280 ytile 2
    [  10] yoffset 1280
    [  11] linear 4 yoffset 0
    [  12] goto [9]
    [  13] return
