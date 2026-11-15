label n_sticker:
    # nested label 5f3306d0cf33ecf42bc89c2c3010a904 starts at [2]
    [   0] "gui/poemgame/n_sticker_1.png"    # image key n_sticker_1
    [   1] xoffset natsukiOffset xzoom natsukiZoom*0.6666667 yzoom 0.6666667
    [   2] label block 5f3306d0cf33ecf42bc89c2c3010a904    # nested entry point
    [   3] # RenpyFunction: Function { FunctionData="function randomPauseNatsuki", FunctionName="_UnhandledExpression_1961729472" }
    [   4] parallel:    # this branch runs alongside; parent continues at [7]
    [   5] call sticker_move_n
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [10]
    [   8] # RenpyFunction: Function { FunctionData="function randomMoveNatsuki", FunctionName="_UnhandledExpression_1336789617" }
    [   9] return
    [  10] goto [3]
