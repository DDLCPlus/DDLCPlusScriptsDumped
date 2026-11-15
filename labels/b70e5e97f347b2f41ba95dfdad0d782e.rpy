label b70e5e97f347b2f41ba95dfdad0d782e:
    [   0] call truecenter
    [   1] parallel:    # this branch runs alongside; parent continues at [9]
    [   2] zoom 1.5
    [   3] easeout 0.35 zoom 1.0
    [   4] zoom 1.5
    [   5] easeout 0.35 zoom 1.0
    [   6] zoom 1.5
    [   7] easeout 0.35 zoom 1.0
    [   8] return
    [   9] parallel:    # this branch runs alongside; parent continues at [17]
    [  10] xpos 0
    [  11] easein_elastic 0.35 xpos 640
    [  12] xpos 1280
    [  13] easein_elastic 0.35 xpos 640
    [  14] xpos 0
    [  15] easein_elastic 0.35 xpos 640
    [  16] return
