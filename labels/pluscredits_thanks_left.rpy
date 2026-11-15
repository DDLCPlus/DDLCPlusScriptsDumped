label pluscredits_thanks_left(direction=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[1], constantStrings=[], constantObjects=[] }>):
    [   0] pass
    [   1] xalign 0.5
    [   2] xoffset 160 * direction
    [   3] alpha 0
    [   4] parallel:    # this branch runs alongside; parent continues at [7]
    [   5] easein 5 xoffset 240 * direction
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [11]
    [   8] 3
    [   9] easein 1 alpha 1
    [  10] return
    [  11] 3.85
    [  12] easeout_cubic 0.75 alpha 0
