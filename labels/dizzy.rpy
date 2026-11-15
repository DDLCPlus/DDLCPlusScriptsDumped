label dizzy(m=<compiled: CompiledExpression { instructions=[], constantFloats=[], constantStrings=[], constantObjects=[] }>, t=<compiled: CompiledExpression { instructions=[], constantFloats=[], constantStrings=[], constantObjects=[] }>, s=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[1], constantStrings=[], constantObjects=[] }>):
    [   0] pass
    [   1] parallel:    # this branch runs alongside; parent continues at [13]
    [   2] xoffset 0
    [   3] ease 0.75 * t xoffset 10 * m
    [   4] ease 0.75 * t xoffset 5 * m
    [   5] ease 0.75 * t xoffset -5 * m
    [   6] ease 0.75 * t xoffset -3 * m
    [   7] ease 0.75 * t xoffset -10 * m
    [   8] ease 0.75 * t xoffset 0
    [   9] ease 0.75 * t xoffset 5 * m
    [  10] ease 0.75 * t xoffset 0
    [  11] goto [2]
    [  12] return
    [  13] parallel:    # this branch runs alongside; parent continues at [20]
    [  14] yoffset 0
    [  15] ease 1.0 * t yoffset 5 * m
    [  16] ease 2.0 * t yoffset -5 * m
    [  17] easein 1.0 * t yoffset 0
    [  18] goto [14]
    [  19] return
