label cg_in_instant:    # on: Hide
    [   0] unless showop == "onhide" goto [3]
    [   1] alpha 1
    [   2] linear 0.5 alpha 0
    [   3] pass
    [   4] unless showop == "main" goto [6]
    [   5] alpha 1
    [   6] pass
