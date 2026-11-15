label layerflicker(t=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>):
    [   0] call truecenter
    [   1] t + 2.030
    [   2] parallel:    # this branch runs alongside; parent continues at [12]
    [   3] zoom 1.05
    [   4] linear 0.2 zoom 1.04
    [   5] 0.1
    [   6] zoom 1.035
    [   7] linear 0.1 zoom 1.05
    [   8] zoom 1.0
    [   9] 1.21
    [  10] goto [3]
    [  11] return
    [  12] parallel:    # this branch runs alongside; parent continues at [17]
    [  13] easeout_bounce 0.3 xalign 0.6
    [  14] easeout_bounce 0.3 xalign 0.4
    [  15] goto [13]
    [  16] return
