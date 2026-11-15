label y_sticker:
    # nested label 4b30d65a725432149b6e473e7081a74f starts at [2]
    [   0] "gui/poemgame/y_sticker_1.png"    # image key y_sticker_1
    [   1] xoffset yuriOffset xzoom yuriZoom*0.6666667 yzoom 0.6666667
    [   2] label block 4b30d65a725432149b6e473e7081a74f    # nested entry point
    [   3] # RenpyFunction: Function { FunctionData="function randomPauseYuri", FunctionName="_UnhandledExpression_735643762" }
    [   4] parallel:    # this branch runs alongside; parent continues at [7]
    [   5] call sticker_move_n
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [10]
    [   8] # RenpyFunction: Function { FunctionData="function randomMoveYuri", FunctionName="_UnhandledExpression_747524997" }
    [   9] return
    [  10] goto [3]
