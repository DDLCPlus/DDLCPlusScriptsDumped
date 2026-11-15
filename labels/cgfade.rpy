label cgfade:    # on: Show, Hide
    [   0] unless showop == "onshow" goto [3]
    [   1] alpha 0.0
    [   2] linear 0.5 alpha 1.0
    [   3] pass
    [   4] unless showop == "onhide" goto [7]
    [   5] alpha 1.0
    [   6] linear 0.5 alpha 0.0
    [   7] pass
    [   8] unless showop == "main" goto [9]
    [   9] pass
