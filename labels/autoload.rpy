label autoload:
    [   0] python:    # runs C# autoload_inlinepythonblock_668462969
                
    [   1] unless persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2" goto [4]
    [   2] 
    [   3] goto [4]
    [   4] pass
    [   5] unless renpy.get_return_stack() goto [8]
    [   6] 
    [   7] goto [8]
    [   8] pass
    [   9] jump expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["persistent", "autoload"], constantObjects=[] }>
