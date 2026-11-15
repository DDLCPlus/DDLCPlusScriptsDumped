label y_kill:
    [   0] unless persistent.yuri_kill >= 1380 goto [3]
    [   1] call yk3a
    [   2] goto [40]
    [   3] pass
    [   4] unless persistent.yuri_kill >= 1180 goto [7]
    [   5] call yk3c
    [   6] goto [40]
    [   7] pass
    [   8] unless persistent.yuri_kill >= 1120 goto [11]
    [   9] call yk3b
    [  10] goto [40]
    [  11] pass
    [  12] unless persistent.yuri_kill >= 920 goto [15]
    [  13] call yk3a
    [  14] goto [40]
    [  15] pass
    [  16] unless persistent.yuri_kill >= 720 goto [19]
    [  17] call yk2c
    [  18] goto [40]
    [  19] pass
    [  20] unless persistent.yuri_kill >= 660 goto [23]
    [  21] call yk2b
    [  22] goto [40]
    [  23] pass
    [  24] unless persistent.yuri_kill >= 460 goto [27]
    [  25] call yk2a
    [  26] goto [40]
    [  27] pass
    [  28] unless persistent.yuri_kill >= 260 goto [31]
    [  29] call yk1c
    [  30] goto [40]
    [  31] pass
    [  32] unless persistent.yuri_kill >= 200 goto [35]
    [  33] call yk1b
    [  34] goto [40]
    [  35] pass
    [  36] unless True goto [39]
    [  37] call yk1a
    [  38] goto [40]
    [  39] pass
    [  40] pass
    [  41] 1.0
    [  42] goto [0]
