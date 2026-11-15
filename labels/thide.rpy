label thide(z=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0.8], constantStrings=[], constantObjects=[] }>):    # on: Hide
    [   0] unless showop == "onhide" goto [2]
    [   1] easein .25 zoom z*0.95 alpha 0.00 yoffset -20
    [   2] pass
    [   3] unless showop == "main" goto [6]
    [   4] pass
    [   5] pass
    [   6] pass
