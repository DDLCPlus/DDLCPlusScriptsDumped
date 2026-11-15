label panic(x=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[640], constantStrings=[], constantObjects=[] }>, z=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0.8], constantStrings=[], constantObjects=[] }>):
    [   0] xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    [   1] parallel:    # this branch runs alongside; parent continues at [6]
    [   2] ease 1.2 yoffset 25
    [   3] ease 1.2 yoffset 0
    [   4] goto [2]
    [   5] return
    [   6] parallel:    # this branch runs alongside; parent continues at [12]
    [   7] easein .3 xoffset 20
    [   8] ease .6 xoffset -20
    [   9] easeout .3 xoffset 0
    [  10] goto [7]
    [  11] return
