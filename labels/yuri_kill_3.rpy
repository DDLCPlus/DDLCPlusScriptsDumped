label yuri_kill_3:
    [   0] python:    # runs C# yuri_kill_3_inlinepythonblock_1397197202
                
    [   1] 
    [   2] 
    [   3] unless persistent.has_skipped_yuri == False goto [6]
    [   4] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="yuri_noskip", UnlockId=2849673567 }
    [   5] goto [6]
    [   6] pass
    [   7] 
    [   8] 
    [   9] 
    [  10] 
    [  11] 
    [  12] 
    [  13] unless not renpy.music.get_playing(channel='music') == audio.t6s goto [18]
    [  14] 
    [  15] 
    [  16] play music "t6s"
    [  17] goto [18]
    [  18] pass
    [  19] scene bg club_day
    [  20] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  21] unless persistent.content_warnings_enabled == True goto [24]
    [  22] 
    [  23] goto [24]
    [  24] pass
    [  25] window auto
    [  26] n "Alright, it's festival time!"
    [  27] show natsuki 4k at t11 zorder 2
    [  28] n "Wow, you got here before me?"
    [  29] n "I thought I was pretty ea--{nw}"
    [  30] show natsuki scream at h11
    [  31] n "EYAH!"
    [  32] n "AAAAAAAAAAAAAAAHHHH!!!"
    [  33] 
    [  34] show natsuki scream at h11
    [  35] 
    [  36] show natsuki vomit at h11
    [  37] 
    [  38] show natsuki at lhide
    [  39] hide natsuki
    [  40] "Natsuki runs away."
    [  41] m "..."
    [  42] show monika 2b at t11 zorder 2
    [  43] m "I'm here!"
    [  44] m 2d "[player], did something happen?"
    [  45] m "Natsuki just ran past me..."
    [  46] m 2i "...Oh..."
    [  47] m "...Oh."
    [  48] m 2r "..."
    [  49] m 2l "Ahahaha!"
    [  50] m "Well, that's a shame."
    [  51] m 2d "Wait, were you here the entire weekend, [player]?"
    [  52] m "Oh, jeez..."
    [  53] m 2g "I didn't realize the script was broken that badly."
    [  54] m "I'm super sorry!"
    [  55] m "It must have been pretty boring..."
    [  56] m 2e "I'll make it up to you, okay?"
    [  57] m "Just gimme a sec..."
    [  58] 
    [  59] call updateconsole(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["os.remove(\"characters/yuri.chr\")"], constantObjects=[] }>, <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["yuri.chr deleted successfully."], constantObjects=[] }>)
    [  60] 
    [  61] 
    [  62] call updateconsole(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["os.remove(\"characters/natsuki.chr\")"], constantObjects=[] }>, <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["natsuki.chr deleted successfully."], constantObjects=[] }>)
    [  63] 
    [  64] 
    [  65] m 2a "I'm almost done."
    [  66] m 2j "I just want to have a cupcake real quick!"
    [  67] 
    [  68] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  69] m 2b "Seriously, these are the best!"
    [  70] m "I really just had to have one, since it's the last time I'll ever get the chance to."
    [  71] m 2a "You know, before they stop existing and everything."
    [  72] m "...But anyway, I really shouldn't be making you wait any longer."
    [  73] m 2j "Just bear with me, okay?"
    [  74] m 2a "This should only take a second."
    [  75] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [  76] 
    [  77] 
    [  78] 
    [  79] 
    [  80] 
    [  81] 
    [  82] hide screen tear
    [  83] call screen_tear_hide
    [  84] scene white
    [  85] 
    [  86] return
