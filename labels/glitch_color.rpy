label glitch_color:
    [   0] ytile 3
    [   1] zoom 2.5
    [   2] parallel:    # this branch runs alongside; parent continues at [11]
    [   3] "bg/glitch-red.png"    # image key glitch-red
    [   4] 0.1
    [   5] "bg/glitch-green.png"    # image key glitch-green
    [   6] 0.1
    [   7] "bg/glitch-blue.png"    # image key glitch-blue
    [   8] 0.1
    [   9] goto [3]
    [  10] return
    [  11] parallel:    # this branch runs alongside; parent continues at [16]
    [  12] yoffset 720
    [  13] linear 0.5 yoffset 0
    [  14] goto [12]
    [  15] return
    [  16] parallel:    # this branch runs alongside; parent continues at [42]
    [  17] $ randrangevalue = renpy.random.randint(0, 6)    # choice:
    [  18] unless randrangevalue == 0 goto [20]
    [  19] xoffset 0
    [  20] pass
    [  21] unless randrangevalue == 1 goto [23]
    [  22] xoffset 10
    [  23] pass
    [  24] unless randrangevalue == 2 goto [26]
    [  25] xoffset 20
    [  26] pass
    [  27] unless randrangevalue == 3 goto [29]
    [  28] xoffset 35
    [  29] pass
    [  30] unless randrangevalue == 4 goto [32]
    [  31] xoffset -10
    [  32] pass
    [  33] unless randrangevalue == 5 goto [35]
    [  34] xoffset -20
    [  35] pass
    [  36] unless randrangevalue == 6 goto [38]
    [  37] xoffset -30
    [  38] pass
    [  39] 0.01
    [  40] goto [17]
    [  41] return
    [  42] parallel:    # this branch runs alongside; parent continues at [52]
    [  43] alpha 0.6
    [  44] linear 0.15 alpha 0.1
    [  45] 0.2
    [  46] alpha 0.6
    [  47] linear 0.15 alpha 0.1
    [  48] 0.2
    [  49] alpha 0.7
    [  50] linear 0.45 alpha 0
    [  51] return
