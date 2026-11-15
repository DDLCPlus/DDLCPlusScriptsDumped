label menu_art_move(z=<compiled: CompiledExpression { instructions=[], constantFloats=[], constantStrings=[], constantObjects=[] }>, x=<compiled: CompiledExpression { instructions=[], constantFloats=[], constantStrings=[], constantObjects=[] }>, z2=<compiled: CompiledExpression { instructions=[], constantFloats=[], constantStrings=[], constantObjects=[] }>):
    [   0] pass
    [   1] yoffset 0 + (1200 * z)
    [   2] xoffset (740 - x) * z * 0.5
    [   3] zoom z2 * 0.75
    [   4] 1.0
    [   5] parallel:    # this branch runs alongside; parent continues at [8]
    [   6] ease 1.75 yoffset 0
    [   7] return
    [   8] parallel:    # this branch runs alongside; parent continues at [12]
    [   9] 0.75
    [  10] ease 1.5 zoom z2 xoffset 0
    [  11] return
