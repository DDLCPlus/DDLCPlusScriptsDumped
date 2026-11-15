label end_glitch1:
    [   0] "bg/end-glitch1.jpg"    # image key end-glitch1
    [   1] alpha 0.0
    [   2] 1.0
    [   3] alpha 1.0
    [   4] parallel:    # this branch runs alongside; parent continues at [9]
    [   5] yoffset 1280 ytile 2
    [   6] linear 1 yoffset 0
    [   7] goto [5]
    [   8] return
