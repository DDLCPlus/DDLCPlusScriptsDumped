label delayed_blink(delay=<compiled: CompiledExpression { instructions=[], constantFloats=[], constantStrings=[], constantObjects=[] }>, cycle=<compiled: CompiledExpression { instructions=[], constantFloats=[], constantStrings=[], constantObjects=[] }>):
    # nested label bf8ad36391ef59f48af2d07fc24c2e08 starts at [2]
    [   0] alpha .5
    [   1] delay
    [   2] label block bf8ad36391ef59f48af2d07fc24c2e08    # nested entry point
    [   3] linear .2 alpha 1.0
    [   4] .2
    [   5] linear .2 alpha 0.5
    [   6] (cycle - .4)
    [   7] goto [3]
