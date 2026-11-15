label ch3_end_sayori:
    [   0] 
    [   1] mc "I mean..."
    [   2] mc "If it's going to be anyone, then I prefer helping Sayori."
    [   3] mc "I mean, we're already neighbors, and--"
    [   4] show yuri 2f at f33 zorder 3
    [   5] y "But Monika said--"
    [   6] show yuri at t33 zorder 2
    [   7] show natsuki 4w at f31 zorder 3
    [   8] n "Monika said that Sayori was helping her!"
    [   9] n "Jeez..."
    [  10] n 4h "Do you really hate us that much?"
    [  11] show natsuki at t31 zorder 2
    [  12] mc "N-No!"
    [  13] show monika 1e at f32 zorder 3
    [  14] m "Sorry, I didn't mean for this to be difficult..."
    [  15] show monika at t32 zorder 2
    [  16] goto [23]
    [  17] call ch3_end_natsuki
    [  18] goto [25]
    [  19] call ch3_end_yuri
    [  20] goto [25]
    [  21] call ch3_end_monika
    [  22] goto [25]
    [  23] m "Just think of the club, okay?{nw}"    # menu-with-caption
    [  24] menu:    # caption above
                "Natsuki.":  goto [17]
                "Yuri.":  goto [19]
                "Monika." if <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["help_monika"], constantObjects=[] }>:  goto [21]
    [  25] pass
    [  26] return
