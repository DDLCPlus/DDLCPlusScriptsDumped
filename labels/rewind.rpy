label rewind:
    [   0] call truecenter
    [   1] zoom 1.20
    [   2] parallel:    # this branch runs alongside; parent continues at [7]
    [   3] easeout_bounce 0.2 xalign 0.55
    [   4] easeout_bounce 0.2 xalign 0.45
    [   5] goto [3]
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [12]
    [   8] easeout_bounce 0.33 yalign 0.55
    [   9] easeout_bounce 0.33 yalign 0.45
    [  10] goto [8]
    [  11] return
