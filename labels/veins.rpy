label veins:
    [   0] xanchor 0.05 zoom 1.10
    [   1] xpos -5
    [   2] pass
    [   3] parallel:    # this branch runs alongside; parent continues at [12]
    [   4] ease 2.0 xpos 5
    [   5] ease 1.0 xpos 0
    [   6] ease 1.0 xpos 5
    [   7] ease 2.0 xpos -5
    [   8] ease 1.0 xpos 0
    [   9] ease 1.0 xpos -5
    [  10] goto [4]
    [  11] return
    [  12] parallel:    # this branch runs alongside; parent continues at [47]
    [  13] $ randrangevalue = renpy.random.randint(0, 9)    # choice:
    [  14] unless randrangevalue == 0 goto [16]
    [  15] 0.6
    [  16] pass
    [  17] unless randrangevalue == 1 goto [19]
    [  18] 0.2
    [  19] pass
    [  20] unless randrangevalue == 2 goto [22]
    [  21] 0.3
    [  22] pass
    [  23] unless randrangevalue == 3 goto [25]
    [  24] 0.4
    [  25] pass
    [  26] unless randrangevalue == 4 goto [28]
    [  27] 0.5
    [  28] pass
    [  29] pass
    [  30] unless randrangevalue == 5 goto [32]
    [  31] xoffset 0
    [  32] pass
    [  33] unless randrangevalue == 6 goto [35]
    [  34] xoffset 1
    [  35] pass
    [  36] unless randrangevalue == 7 goto [38]
    [  37] xoffset 2
    [  38] pass
    [  39] unless randrangevalue == 8 goto [41]
    [  40] xoffset -1
    [  41] pass
    [  42] unless randrangevalue == 9 goto [44]
    [  43] xoffset -2
    [  44] pass
    [  45] goto [13]
    [  46] return
    [  47] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
