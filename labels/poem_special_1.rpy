label poem_special_1:
    [   0] 
    [   1] unless persistent.content_warnings_enabled == True goto [4]
    [   2] 
    [   3] goto [4]
    [   4] pass
    [   5] play sound "page_turn"
    [   6] with None
    [   7] show poem_special1
    [   8] with Dissolve(1.0)
    [   9] 
    [  10] 
    [  11] return
