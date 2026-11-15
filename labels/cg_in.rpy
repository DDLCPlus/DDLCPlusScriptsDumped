label cg_in:    # on: Hide
    [   0] unless showop == "onhide" goto [3]
    [   1] alpha 1
    [   2] linear 0.5 alpha 0
    [   3] pass
    [   4] unless showop == "main" goto [7]
    [   5] alpha 0
    [   6] linear 0.5 alpha 1
    [   7] pass
