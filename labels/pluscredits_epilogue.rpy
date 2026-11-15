label pluscredits_epilogue:
    [   0] "plus_credits/epilogue.png"    # image key epilogue
    [   1] size(config.screen_width, config.screen_height)
    [   2] xalign 0.5 yalign 0.5
    [   3] pass
    [   4] zoom 1.1 alpha 0
    [   5] parallel:    # this branch runs alongside; parent continues at [8]
    [   6] easein_cubic 4 zoom 1.00
    [   7] return
    [   8] parallel:    # this branch runs alongside; parent continues at [11]
    [   9] easeout 4 alpha 1
    [  10] return
