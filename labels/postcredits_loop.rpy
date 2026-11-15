label postcredits_loop:
    [   0] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="game_complete", UnlockId=2364778287 }
    [   1] 
    [   2] 
    [   3] 
    [   4] 
    [   5] 
    [   6] 
    [   7] 
    [   8] 
    [   9] scene black
    [  10] unless persistent.clearall goto [15]
    [  11] with None
    [  12] show poem_end_clearall
    [  13] with Dissolve(1)
    [  14] goto [18]
    [  15] with None
    [  16] show poem_end
    [  17] with Dissolve(1)
    [  18] pass
    [  19] 
    [  20] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [  21] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [  22] # WaitForScreen: WaitForScreen { screen="dialog" }
    [  23] return
