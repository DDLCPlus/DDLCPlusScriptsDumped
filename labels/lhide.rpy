label lhide:    # on: Hide
    [   0] unless showop == "onhide" goto [2]
    [   1] easeout .25 xcenter -300
    [   2] pass
    [   3] unless showop == "main" goto [5]
    [   4] pass
    [   5] pass
