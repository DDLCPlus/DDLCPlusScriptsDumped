label updateconsolehistory(history=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=[""], constantObjects=[] }>):
    [   0] unless text goto [6]
    [   1] hide chistory
    [   2] with None
    [   3] python:    # runs C# updateconsolehistory_inlinepythonblock_76962088
                
    [   4] show expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["", "consolehistorydisplay"], constantObjects=[] }> as chistory at console_history_t onlayer front
    [   5] goto [6]
    [   6] pass
    [   7] return
