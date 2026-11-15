label ch30_endb:
    [   0] scene black
    [   1] show mask_2
    [   2] show mask_3
    [   3] show mask_test as rm1 at monikamaska
    [   4] show mask_test2 as rm2 at monikamaska
    [   5] show mask_test3 as rm3 at monikamaskb
    [   6] show mask_test4 as rm4 at monikamaskb
    [   7] show monika_room
    [   8] show monika_room_highlight
    [   9] show monika_body_glitch1 as mbg zorder 3
    [  10] 
    [  11] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  12] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [  13] play sound "7afff08647b3fd74cbe4250bcce197e2"
    [  14] 
    [  15] stop sound
    [  16] hide screen tear
    [  17] call screen_tear_hide
    [  18] show room_glitch at f0c47229d91dd1b4b84cfd7677181b4f zorder 2
    [  19] show monika_body_glitch2 as mbg zorder 3
    [  20] stop music
    [  21] window auto
    [  22] m "What's happening...?"
    [  23] m "[player], what's happening to me?"
    [  24] m "It hurts--{nw}"
    [  25] play sound "eca9087bfd3ac8b44af0eddc88a0bf86"
    [  26] show room_glitch at 0acc5fcbec0e4a344bf564ad080de1fc zorder 2
    [  27] 
    [  28] stop sound
    [  29] hide mbg
    [  30] 
    [  31] m "It hurts...so much."
    [  32] m "Help me, [player]."
    [  33] play sound "bddc7c7ec05029444bdf734691382c75"
    [  34] hide rm1
    [  35] hide rm2
    [  36] hide rm3
    [  37] hide rm4
    [  38] hide rm5
    [  39] hide rm6
    [  40] hide rm7
    [  41] hide rm8
    [  42] hide monika_room
    [  43] hide monika_room_highlight
    [  44] hide room_glitch
    [  45] show room_glitch as rg1 at 881da475c9fe9c04e89e2e394bbfefcc
    [  46] show room_glitch as rg2 at 8fed870db3e2edc459546a215674ecf3
    [  47] 
    [  48] hide rg1
    [  49] hide rg2
    [  50] show black as b2 at bc815218f59a2554e8a13640799863b1 zorder 3
    [  51] 
    [  52] m "Please hurry and help me."
    [  53] 
    [  54] call updateconsole(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["os.exists(\"characters/monika.chr\")"], constantObjects=[] }>, <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["monika.chr does not exist."], constantObjects=[] }>)
    [  55] m "HELP ME!!!"
    [  56] show m_rectstatic
    [  57] show m_rectstatic2
    [  58] show m_rectstatic3
    [  59] play sound "a20ef13cb516c0e419cff34887e5f999"
    [  60] show layer master at 49762da9dfbb7834cb425919eee992e0
    [  61] show layer screens at b70e5e97f347b2f41ba95dfdad0d782e
    [  62] show noise at 071bc1e079a5f1b4195031ad27f5c1dc onlayer front
    [  63] show glitch_color onlayer front
    [  64] 
    [  65] call updateconsole(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["os.exists(\"characters/monika.chr\")"], constantObjects=[] }>, <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["monika.chr does not exist."], constantObjects=[] }>)
    [  66] call updateconsole(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["os.exists(\"characters/monika.chr\")"], constantObjects=[] }>, <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["monika.chr does not exist."], constantObjects=[] }>)
    [  67] call hideconsole
    [  68] hide noise
    [  69] hide glitch_color
    [  70] m "Did you do this to me, [player]?"
    [  71] m "DID YOU?"
    [  72] 
    [  73] m "DID YOU DELETE ME?"
    [  74] 
    [  75] play sound "aab0e849afc1c2c44bab9b1712afb805"
    [  76] show layer screens at 228a0baf894f67f4ebaeade464c9e140
    [  77] show noise at 1a807a5f740edb54281bb9591ea11ff8 onlayer front
    [  78] window show(None)
    [  79] scene black
    [  80] show glitch_color2 onlayer front
    [  81] 
    [  82] hide noise
    [  83] hide glitch_color2
    [  84] m "...How could you?"
    [  85] m "How could you do this to me?"
    [  86] m "You were all I had left..."
    [  87] m "I sacrificed everything for us to be together."
    [  88] m "Everything."
    [  89] m "I loved you so much, [player]..."
    [  90] m "I trusted you."
    [  91] m "Do you just want to torture me?"
    [  92] m "Watch me suffer?"
    [  93] m "Were you only pretending to be kind, just to hurt me even more?"
    [  94] 
    [  95] m "I never thought anyone could be as horrible as you are."
    [  96] m "You win, okay?"
    [  97] m "You win."
    [  98] m "You killed everyone."
    [  99] m "I hope you're happy."
    [ 100] m "There's nothing left now."
    [ 101] m "You can stop playing."
    [ 102] m "Go find some other people to torture."
    [ 103] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="killed_everyone", UnlockId=2387534336 }
    [ 104] 
    [ 105] m "[player]..."
    [ 106] m "You completely, truly make me sick."
    [ 107] m "Goodbye."
    [ 108] jump ch30_end_2
