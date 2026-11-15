label ch30_autoload:
    [   0] 
    [   1] 
    [   2] 
    [   3] 
    [   4] 
    [   5] 
    [   6] unless persistent.monika_kill goto [13]
    [   7] 
    [   8] 
    [   9] 
    [  10] 
    [  11] jump ch30_end
    [  12] goto [13]
    [  13] pass
    [  14] scene black
    [  15] show mask_2
    [  16] show mask_3
    [  17] show mask_test as rm1 at monikamaska
    [  18] show mask_test2 as rm2 at monikamaska
    [  19] show mask_test3 as rm3 at monikamaskb
    [  20] show mask_test4 as rm4 at monikamaskb
    [  21] show monika_bg
    [  22] show monika_bg_highlight
    [  23] play music "m1a"
    [  24] window auto
    [  25] unless persistent.monika_reload <= 4 goto [28]
    [  26] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[1, 0], constantStrings=["ch30_reload_", "persistent", "monika_reload", "str"], constantObjects=[] }>
    [  27] goto [29]
    [  28] call ch30_reload_4
    [  29] pass
    [  30] 
    [  31] 
    [  32] unless not persistent.tried_skip goto [35]
    [  33] 
    [  34] goto [36]
    [  35] 
    [  36] pass
    [  37] unless persistent.current_monikatopic != 0 goto [46]
    [  38] m "Now, where was I...?"
    [  39] 
    [  40] unless not persistent.current_monikatopic or persistent.current_monikatopic == 26 goto [43]
    [  41] 
    [  42] goto [43]
    [  43] pass
    [  44] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[1, 0], constantStrings=["ch30_", "persistent", "current_monikatopic", "str"], constantObjects=[] }>
    [  45] goto [46]
    [  46] pass
    [  47] jump ch30_loop
