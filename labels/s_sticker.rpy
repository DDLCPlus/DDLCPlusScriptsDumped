label s_sticker:
    # nested label 9f2a65afed1789a46b20d4f7ad153fbb starts at [2]
    [   0] "gui/poemgame/s_sticker_1.png"    # image key s_sticker_1
    [   1] xoffset sayoriOffset xzoom sayoriZoom*0.6666667 yzoom 0.6666667
    [   2] label block 9f2a65afed1789a46b20d4f7ad153fbb    # nested entry point
    [   3] # RenpyFunction: Function { FunctionData="function randomPauseSayori", FunctionName="_UnhandledExpression_649232684" }
    [   4] parallel:    # this branch runs alongside; parent continues at [7]
    [   5] call sticker_move_n
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [10]
    [   8] # RenpyFunction: Function { FunctionData="function randomMoveSayori", FunctionName="_UnhandledExpression_146175673" }
    [   9] return
    [  10] goto [3]
