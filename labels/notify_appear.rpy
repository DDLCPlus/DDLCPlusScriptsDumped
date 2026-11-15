label notify_appear:    # on: Show, Hide
    [   0] unless showop == "onshow" goto [3]
    [   1] alpha 0
    [   2] linear .25 alpha 1.0
    [   3] pass
    [   4] unless showop == "onhide" goto [6]
    [   5] linear .5 alpha 0.0
    [   6] pass
    [   7] unless showop == "main" goto [8]
    [   8] pass
