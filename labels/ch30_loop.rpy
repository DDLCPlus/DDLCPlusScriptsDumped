label ch30_loop:
    [   0] 
    [   1] unless persistent.topicsplayed > 14 goto [4]
    [   2] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="monika_topics_15", UnlockId=1972829240 }
    [   3] goto [4]
    [   4] pass
    [   5] unless not persistent.tried_skip goto [8]
    [   6] 
    [   7] goto [9]
    [   8] 
    [   9] pass
    [  10] window hide(config.window_hide_transition)
    [  11] 
    [  12] jump ch30_waitloop
