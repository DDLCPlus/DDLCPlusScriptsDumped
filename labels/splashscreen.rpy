label splashscreen:
    [   0] python:    # runs C# splashscreen_inlinepythonblock_191040891
                
    [   1] python:    # runs C# splashscreen_inlinepythonblock_318042419
                
    [   2] unless not firstrun goto [19]
    [   3] unless persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop") goto [16]
    [   4] 
    [   5] scene black
    [   6] goto [12]
    [   7] "Deleting save data...{nw}"
    [   8] python:    # runs C# splashscreen_inlinepythonblock_1380127844
                
    [   9] goto [14]
    [  10] 
    [  11] goto [14]
    [  12] "A previous save file has been found. Would you like to delete your save data and start over?{nw}"    # menu-with-caption
    [  13] menu:    # caption above
                "Yes, delete my existing data.":  goto [7]
                "No, continue where I left off.":  goto [10]
    [  14] pass
    [  15] goto [16]
    [  16] pass
    [  17] python:    # runs C# splashscreen_inlinepythonblock_1905976040
                
    [  18] goto [19]
    [  19] pass
    [  20] unless config.version != persistent.oldversion goto [25]
    [  21] 
    [  22] 
    [  23] 
    [  24] goto [25]
    [  25] pass
    [  26] unless not persistent.first_run goto [70]
    [  27] python:    # runs C# splashscreen_inlinepythonblock_1620991023
                
    [  28] 
    [  29] scene white
    [  30] 0.5
    [  31] scene tos
    [  32] with Dissolve(1.0)
    [  33] 1.0
    [  34] "This game is not suitable for children or those who are easily disturbed."
    [  35] "Individuals suffering from anxiety or depression may not have a positive experience playing this game."
    [  36] goto [53]
    [  37] "Thank you for your interest in Doki Doki Literature Club."
    [  38] "Doki Doki Literature Club is a horror game. Please do not take this lightly."
    [  39] "Doki Doki Literature Club may not be suitable for you if you are affected by any of the following themes:"
    [  40] "Depression"
    [  41] "Suicide"
    [  42] "Self-harm"
    [  43] "Abuse"
    [  44] "These themes are not merely suggested, but are often portrayed as realistically as possible, and thus may disturb you as if they were real."
    [  45] "Furthermore, the above list is not 100% exhaustive."
    [  46] "If you would like to be warned when potentially sensitive content is about to occur while playing the game, detailed content warnings can be enabled in the settings menu."
    [  47] "For those with extra concern for their mental health, our recommendation of the safest approach is to avoid playing Doki Doki Literature Club."
    [  48] "We trust that given your understanding of your own mental health, you are able to make the decision that is right for you."
    [  49] "Thank you for your consideration and for staying safe."
    [  50] goto [55]
    [  51] pass
    [  52] goto [55]
    [  53] "Would you like to review detailed content warnings, which contain spoilers? Alternatively, in-game content warnings can be enabled in the settings menu at any time.{nw}"    # menu-with-caption
    [  54] menu:    # caption above
                "Yes (contains spoilers)":  goto [37]
                "No":  goto [51]
    [  55] pass
    [  56] 1.0
    [  57] goto [60]
    [  58] pass
    [  59] goto [62]
    [  60] "By playing Doki Doki Literature Club, you agree that you have noted the game's age rating in your region, and you consent to your exposure of highly disturbing content.{nw}"    # menu-with-caption
    [  61] menu:    # caption above
                "I agree.":  goto [58]
    [  62] pass
    [  63] scene tos2
    [  64] with Dissolve(2.0)
    [  65] 
    [  66] 
    [  67] 
    [  68] scene white
    [  69] goto [70]
    [  70] pass
    [  71] python:    # runs C# splashscreen_inlinepythonblock_85563775
                
    [  72] unless not persistent.special_poems goto [75]
    [  73] python:    # runs C# splashscreen_inlinepythonblock_320855191
                
    [  74] goto [75]
    [  75] pass
    [  76] 
    [  77] 
    [  78] 
    [  79] unless persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0 goto [93]
    [  80] show black
    [  81] 
    [  82] 
    [  83] 
    [  84] 
    [  85] 
    [  86] with None
    [  87] show end
    [  88] with dissolve_cg
    [  89] 
    [  90] 
    [  91] return
    [  92] goto [93]
    [  93] pass
    [  94] unless s_kill_early goto [112]
    [  95] scene white
    [  96] show black zorder 2
    [  97] play music "923f66eb272d5bb4e838bf5bee92d9f2"
    [  98] 
    [  99] with None
    [ 100] show end zorder 2
    [ 101] with dissolve_cg
    [ 102] 
    [ 103] scene white
    [ 104] show eb5b54320bc046543a6aab1ad564d5b4 at 4c76e73c94c070248b2ad6fd12f93858
    [ 105] show white as w2 at 6a83ee2bdccea1c429296ab9637c0e42
    [ 106] show noise at 448cee0a38a3eba44bad66d7b1c10906
    [ 107] show s_kill_early_splash_text at ade91891ba5737a4c9690967c06d6186
    [ 108] with dissolve_scene
    [ 109] 0
    [ 110] 
    [ 111] goto [113]
    [ 112] 
    [ 113] pass
    [ 114] show white
    [ 115] 
    [ 116] 
    [ 117] 
    [ 118] 
    [ 119] 
    [ 120] with None
    [ 121] show intro
    [ 122] with Dissolve(0.5, alpha=True)
    [ 123] 
    [ 124] with None
    [ 125] hide intro
    [ 126] with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    [ 127] unless persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0 goto [130]
    [ 128] 
    [ 129] goto [130]
    [ 130] pass
    [ 131] with None
    [ 132] show expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["", "splash_message"], constantObjects=[] }>
    [ 133] with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    [ 134] 
    [ 135] with None
    [ 136] hide splash_warning
    [ 137] with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    [ 138] 
    [ 139] 
    [ 140] return
