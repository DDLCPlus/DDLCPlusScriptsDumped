label poemresponse_monika:
    [   0] scene bg club_day
    [   1] show monika 1a at t11 zorder 2
    [   2] with wipeleft_scene
    [   3] unless m_poemappeal[chapter - 1] < 0 goto [6]
    [   4] 
    [   5] goto [9]
    [   6] unless m_poemappeal[chapter - 1] > 0 goto [9]
    [   7] 
    [   8] goto [9]
    [   9] pass
    [  10] 
    [  11] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [  12] unless not skip_poem goto [16]
    [  13] 
    [  14] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [  15] goto [16]
    [  16] pass
    [  17] return
