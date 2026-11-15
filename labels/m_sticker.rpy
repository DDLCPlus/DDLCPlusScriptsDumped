label m_sticker:
    # nested label 348e82a57517b414b8b6fdde86df1035 starts at [2]
    [   0] "gui/poemgame/m_sticker_1.png"    # image key m_sticker_1
    [   1] xoffset monikaOffset xzoom monikaZoom*0.6666667 yzoom 0.6666667
    [   2] label block 348e82a57517b414b8b6fdde86df1035    # nested entry point
    [   3] # RenpyFunction: Function { FunctionData="function randomPauseMonika", FunctionName="_UnhandledExpression_310984740" }
    [   4] parallel:    # this branch runs alongside; parent continues at [7]
    [   5] call sticker_move_n
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [10]
    [   8] # RenpyFunction: Function { FunctionData="function randomMoveMonika", FunctionName="_UnhandledExpression_1980503799" }
    [   9] return
    [  10] goto [3]
