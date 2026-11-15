label renpymain:
    # nested label innerrenpymain starts at [4]
    [   0] scene white
    [   1] window hide
    [   2] window auto
    [   3] call splashscreen
    [   4] label label innerrenpymain:    # nested entry point
    [   5] window hide
    [   6] window auto
    [   7] call main_menu
    [   8] jump innerrenpymain
    [   9] jump navigation
