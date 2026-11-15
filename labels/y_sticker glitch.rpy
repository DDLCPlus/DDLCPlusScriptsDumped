label y_sticker glitch:
    # nested label e9ef17a2d985827438b0085d6e64bfbd starts at [2]
    [   0] "gui/poemgame/y_sticker_1_broken.png"    # image key y_sticker_1_broken
    [   1] xoffset yuriOffset xzoom yuriZoom*2.0 zoom 2.0
    [   2] label block e9ef17a2d985827438b0085d6e64bfbd    # nested entry point
    [   3] # RenpyFunction: Function { FunctionData="function randomPauseYuri", FunctionName="_UnhandledExpression_735643762" }
    [   4] parallel:    # this branch runs alongside; parent continues at [7]
    [   5] call sticker_move_n
    [   6] return
    [   7] parallel:    # this branch runs alongside; parent continues at [10]
    [   8] # RenpyFunction: Function { FunctionData="function randomMoveYuri", FunctionName="_UnhandledExpression_747524997" }
    [   9] return
    [  10] goto [3]
