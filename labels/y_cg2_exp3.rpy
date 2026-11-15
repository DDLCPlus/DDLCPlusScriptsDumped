label y_cg2_exp3:    # on: Hide
    [   0] unless showop == "onhide" goto [2]
    [   1] linear 0.5 alpha 0
    [   2] pass
    [   3] unless showop == "main" goto [8]
    [   4] call y_cg2_exp3_original
    [   5] size(1280,720)
    [   6] alpha 0
    [   7] linear 0.5 alpha 1
    [   8] pass
