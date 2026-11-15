label y_cg2_nochoc:    # on: Hide
    [   0] unless showop == "onhide" goto [2]
    [   1] linear 0.5 alpha 0
    [   2] pass
    [   3] unless showop == "main" goto [6]
    [   4] call y_cg2_nochoc_original
    [   5] size(1280,720)
    [   6] pass
