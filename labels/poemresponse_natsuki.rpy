label poemresponse_natsuki:
    [   0] scene bg club_day
    [   1] show natsuki 1c at t11 zorder 2
    [   2] with wipeleft_scene
    [   3] 
    [   4] unless n_poemappeal[chapter - 1] < 0 goto [7]
    [   5] 
    [   6] goto [10]
    [   7] unless n_poemappeal[chapter - 1] > 0 goto [10]
    [   8] 
    [   9] goto [10]
    [  10] pass
    [  11] 
    [  12] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [  13] unless not skip_poem goto [17]
    [  14] 
    [  15] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [  16] goto [17]
    [  17] pass
    [  18] return
