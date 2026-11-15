label showpoem(poem=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=[], constantObjects=[] }>, music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[1], constantStrings=[], constantObjects=[] }>, track=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=[], constantObjects=[] }>, revert_music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[1], constantStrings=[], constantObjects=[] }>, img=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=[], constantObjects=[] }>, where=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["i11"], constantObjects=[] }>, paper=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=[], constantObjects=[] }>):
    [   0] unless poem == None goto [3]
    [   1] return
    [   2] goto [3]
    [   3] pass
    [   4] play sound "page_turn"
    [   5] unless music goto [15]
    [   6] 
    [   7] unless track goto [10]
    [   8] 
    [   9] goto [11]
    [  10] 
    [  11] pass
    [  12] stop music fadeout 2
    [  13] 
    [  14] goto [15]
    [  15] pass
    [  16] window hide
    [  17] 
    [  18] unless paper goto [21]
    [  19] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [  20] goto [22]
    [  21] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [  22] pass
    [  23] with Dissolve(1)
    [  24] 
    [  25] unless img goto [29]
    [  26] 
    [  27] 
    [  28] goto [29]
    [  29] pass
    [  30] hide screen poem
    [  31] call screen_poem_hide
    [  32] with Dissolve(.5)
    [  33] window auto
    [  34] unless music and revert_music goto [40]
    [  35] 
    [  36] 
    [  37] stop musicpoem fadeout 2
    [  38] 
    [  39] goto [40]
    [  40] pass
    [  41] return
