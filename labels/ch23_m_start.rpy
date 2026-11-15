label ch23_m_start:
    [   0] 
    [   1] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [   2] unless y_appeal < 3 goto [17]
    [   3] m 1a "Anyway..."
    [   4] unless y_gave goto [11]
    [   5] m 1m "I guess we won't worry about your poem..."
    [   6] m "Yuri should have at least had the courtesy of letting you finish sharing it before taking it."
    [   7] m 1r "...Well, whatever."
    [   8] m "If it makes her happy, I won't stop her."
    [   9] m 1a "As for mine..."
    [  10] goto [11]
    [  11] pass
    [  12] m 1e "I worked really...really hard on this poem, so..."
    [  13] m "I hope that it's, uh, effective."
    [  14] m 1r "Here goes..."
    [  15] 
    [  16] goto [17]
    [  17] pass
    [  18] return
