label poem(transition=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[1], constantStrings=[], constantObjects=[] }>):
    [   0] stop music fadeout 2
    [   1] unless persistent.playthrough == 3 goto [4]
    [   2] scene bg notebook-glitch
    [   3] goto [5]
    [   4] scene bg notebook
    [   5] pass
    [   6] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [   7] unless persistent.playthrough == 3 goto [10]
    [   8] show m_sticker at sticker_mid
    [   9] goto [24]
    [  10] unless persistent.playthrough == 0 goto [13]
    [  11] show s_sticker at sticker_left
    [  12] goto [13]
    [  13] pass
    [  14] show n_sticker at sticker_mid
    [  15] unless persistent.playthrough == 2 and chapter == 2 goto [18]
    [  16] show y_sticker_cut at sticker_right
    [  17] goto [19]
    [  18] show y_sticker at sticker_right
    [  19] pass
    [  20] unless persistent.playthrough == 2 and chapter == 2 goto [23]
    [  21] show m_sticker at sticker_m_glitch
    [  22] goto [23]
    [  23] pass
    [  24] pass
    [  25] unless instant_poem_transition == True goto [28]
    [  26] with None
    [  27] goto [29]
    [  28] with dissolve_scene_full
    [  29] pass
    [  30] 
    [  31] unless persistent.playthrough == 3 goto [34]
    [  32] play music "ghostmenu"
    [  33] goto [35]
    [  34] play music "t4"
    [  35] pass
    [  36] 
    [  37] 
    [  38] 
    [  39] unless persistent.playthrough == 0 and chapter == 0 goto [44]
    [  40] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [  41] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [  42] # WaitForScreen: WaitForScreen { screen="dialog" }
    [  43] goto [44]
    [  44] pass
    [  45] python:    # runs C# poem_inlinepythonblock_938483869
                
    [  46] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="all_poems_sayori", UnlockId=1573187045 }
    [  47] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="all_poems_natsuki", UnlockId=2217467263 }
    [  48] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="all_poems_yuri", UnlockId=3862821335 }
    [  49] unless persistent.playthrough == 2 and persistent.seen_eyes == False and renpy.random.randint(0,5) == 0 goto [79]
    [  50] 
    [  51] 
    [  52] play sound "8f45b63e89f6c7f4d959723aaa852c4b"
    [  53] 
    [  54] 
    [  55] stop music
    [  56] with None
    [  57] scene black
    [  58] with None
    [  59] with None
    [  60] scene black
    [  61] with None
    [  62] 
    [  63] with None
    [  64] scene black
    [  65] with None
    [  66] show bg eyes_move
    [  67] 
    [  68] hide bg eyes_move
    [  69] show bg eyes
    [  70] 
    [  71] hide bg eyes
    [  72] show bg eyes_move
    [  73] 
    [  74] with None
    [  75] hide bg eyes
    [  76] with None
    [  77] 
    [  78] goto [79]
    [  79] pass
    [  80] 
    [  81] 
    [  82] stop music fadeout 2
    [  83] scene black
    [  84] unless persistent.perfect_poem != "None" goto [96]
    [  85] unless persistent.perfect_poem = "Sayori" goto [88]
    [  86] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="perfect_poem_sayori", UnlockId=2000861516 }
    [  87] goto [94]
    [  88] unless persistent.perfect_poem = "Natsuki" goto [91]
    [  89] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="perfect_poem_natsuki", UnlockId=3903737088 }
    [  90] goto [94]
    [  91] unless persistent.perfect_poem = "Yuri" goto [94]
    [  92] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="perfect_poem_yuri", UnlockId=3291199742 }
    [  93] goto [94]
    [  94] pass
    [  95] goto [96]
    [  96] pass
    [  97] with dissolve_scene_full
    [  98] return
