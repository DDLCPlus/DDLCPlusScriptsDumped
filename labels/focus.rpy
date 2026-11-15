label focus(x=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[640], constantStrings=[], constantObjects=[] }>, z=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0.8], constantStrings=[], constantObjects=[] }>):    # on: Show, Replace
    [   0] unless showop == "onshow" goto [5]
    [   1] zoom z*0.95 alpha 0.00
    [   2] xcenter x yoffset -20
    [   3] easein .25 yoffset 0 zoom z*1.05 alpha 1.00
    [   4] yanchor 1.0 ypos 1.03
    [   5] pass
    [   6] unless showop == "onreplace" goto [14]
    [   7] alpha 1.00
    [   8] parallel:    # this branch runs alongside; parent continues at [11]
    [   9] easein .25 xcenter x zoom z*1.05
    [  10] return
    [  11] parallel:    # this branch runs alongside; parent continues at [14]
    [  12] easein .15 yoffset 0
    [  13] return
    [  14] pass
    [  15] unless showop == "main" goto [17]
    [  16] yanchor 1.0 ypos 1.03 subpixel True
    [  17] pass
