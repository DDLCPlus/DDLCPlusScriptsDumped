label vignetteflicker(t=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>):
    [   0] alpha 0.0
    [   1] t + 2.030
    [   2] parallel:    # this branch runs alongside; parent continues at [12]
    [   3] alpha 1.00
    [   4] linear 0.2 alpha 0.8
    [   5] 0.1
    [   6] alpha 0.7
    [   7] linear 0.1 alpha 1.00
    [   8] alpha 0.0
    [   9] 1.21
    [  10] goto [3]
    [  11] return
    [  12] parallel:    # this branch runs alongside; parent continues at [15]
    [  13] easeout 20 zoom 3.0
    [  14] return
