label ch23_n_end:
    [   0] 
    [   1] 
    [   2] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_n23"], constantObjects=[] }>, revert_music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>)
    [   3] 
    [   4] 
    [   5] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [   6] 
    [   7] stop music
    [   8] hide screen tear
    [   9] call screen_tear_hide
    [  10] show natsuki ghost_base
    [  11] n "I changed my mind."
    [  12] n "Ignore everything you just read."
    [  13] n "There's no point in trying to do anything."
    [  14] n "It's Yuri's own fault that she's so unlikable."
    [  15] n "Can you hear me, [player]?"
    [  16] n "If you would just spend more time with Monika, all these problems would go away."
    [  17] n "Yuri and I are too messed up for someone as wonderful as you."
    [  18] n "Just think of Monika from now on."
    [  19] n "Just Monika."
    [  20] hide natsuki
    [  21] 
    [  22] "Just Monika."
    [  23] goto [26]
    [  24] pass
    [  25] goto [28]
    [  26] "Just Monika.{nw}"    # menu-with-caption
    [  27] menu:    # caption above
                "Just Monika.":  goto [24]
    [  28] pass
    [  29] 
    [  30] 
    [  31] scene white
    [  32] play music "t1"
    [  33] with None
    [  34] show intro
    [  35] with Dissolve(0.5, alpha=True)
    [  36] 
    [  37] with None
    [  38] hide intro
    [  39] with Dissolve(0.5, alpha=True)
    [  40] with None
    [  41] show expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["Just Monika."], constantObjects=[] }>
    [  42] with Dissolve(0.5, alpha=True)
    [  43] 
    [  44] play music "t5"
    [  45] 
    [  46] return
