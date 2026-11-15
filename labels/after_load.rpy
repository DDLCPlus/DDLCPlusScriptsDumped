label after_load:
    [   0] unless persistent.playthrough == 0 goto [3]
    [   1] 
    [   2] goto [3]
    [   3] pass
    [   4] 
    [   5] 
    [   6] 
    [   7] unless persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2" goto [39]
    [   8] unless persistent.yuri_kill >= 1380 goto [11]
    [   9] 
    [  10] goto [36]
    [  11] unless persistent.yuri_kill >= 1180 goto [14]
    [  12] 
    [  13] goto [36]
    [  14] unless persistent.yuri_kill >= 1120 goto [17]
    [  15] 
    [  16] goto [36]
    [  17] unless persistent.yuri_kill >= 920 goto [20]
    [  18] 
    [  19] goto [36]
    [  20] unless persistent.yuri_kill >= 720 goto [23]
    [  21] 
    [  22] goto [36]
    [  23] unless persistent.yuri_kill >= 660 goto [26]
    [  24] 
    [  25] goto [36]
    [  26] unless persistent.yuri_kill >= 460 goto [29]
    [  27] 
    [  28] goto [36]
    [  29] unless persistent.yuri_kill >= 260 goto [32]
    [  30] 
    [  31] goto [36]
    [  32] unless persistent.yuri_kill >= 200 goto [35]
    [  33] 
    [  34] goto [36]
    [  35] 
    [  36] pass
    [  37] jump expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["persistent", "autoload"], constantObjects=[] }>
    [  38] goto [61]
    [  39] unless anticheat != persistent.anticheat goto [54]
    [  40] 
    [  41] stop music
    [  42] scene black
    [  43] "The save file could not be loaded."
    [  44] "Are you trying to cheat?"
    [  45] 
    [  46] show monika 1 at t11
    [  47] unless persistent.playername == "" goto [50]
    [  48] m "You're so funny."
    [  49] goto [51]
    [  50] m "You're so funny, [persistent.playername]."
    [  51] pass
    [  52] 
    [  53] goto [61]
    [  54] unless persistent.playthrough == 0 and not persistent.first_load and not config.developer goto [60]
    [  55] 
    [  56] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [  57] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [  58] # WaitForScreen: WaitForScreen { screen="dialog" }
    [  59] goto [60]
    [  60] pass
    [  61] pass
    [  62] return
