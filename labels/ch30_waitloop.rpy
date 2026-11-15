label ch30_waitloop:
    [   0] python:    # runs C# ch30_waitloop_inlinepythonblock_1124479306
                
    [   1] 
    [   2] 
    [   3] unless waittime > 0 goto [6]
    [   4] jump ch30_waitloop
    [   5] goto [6]
    [   6] pass
    [   7] window auto
    [   8] python:    # runs C# ch30_waitloop_inlinepythonblock_414649179
                
    [   9] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[1, 0], constantStrings=["ch30_", "persistent", "current_monikatopic", "str"], constantObjects=[] }>
    [  10] jump ch30_loop
