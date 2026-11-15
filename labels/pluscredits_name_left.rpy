label pluscredits_name_left(direction=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[1], constantStrings=[], constantObjects=[] }>, y=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0.5], constantStrings=[], constantObjects=[] }>):
    [   0] pass
    [   1] xalign 0.5 yalign y
    [   2] xoffset 160 * direction
    [   3] alpha 0
    [   4] parallel:    # this branch runs alongside; parent continues at [7]
    [   5] easein 5 xoffset 240 * direction
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [10]
    [   8] easein 3.0 alpha 1
    [   9] return
    [  10] 2.75
    [  11] easeout_cubic 1.75 alpha 0 xoffset 320 * direction
