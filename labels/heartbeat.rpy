label heartbeat:
    [   0] call truecenter
    [   1] parallel:    # this branch runs alongside; parent continues at [10]
    [   2] 0.144
    [   3] # RenpyClrFlag: RenpyClrFlag { flag="hb" }
    [   4] linear 0.1 zoom 1.07 yalign 0.48
    [   5] easein 0.250 zoom 1.00 + 0.04 yalign 0.49
    [   6] easeout 0.269 zoom 1.00 + 0.07 yalign 0.48
    [   7] linear 0.1 zoom 1.0 yalign 0.5
    [   8] goto [2]
    [   9] return
    [  10] parallel:    # this branch runs alongside; parent continues at [15]
    [  11] easeout_bounce 0.3 xalign 0.5 + 0.02
    [  12] easeout_bounce 0.3 xalign 0.5 - 0.02
    [  13] goto [11]
    [  14] return
