label yuri_kill_2:
    # nested label yuri_kill_loop starts at [34]
    [   0] unless persistent.yuri_kill > 1399 goto [3]
    [   1] 
    [   2] goto [4]
    [   3] 
    [   4] pass
    [   5] 
    [   6] 
    [   7] 
    [   8] 
    [   9] python:    # runs C# yuri_kill_2_inlinepythonblock_105532812
                
    [  10] 
    [  11] unless not renpy.music.get_playing(channel='music') == audio.t6s goto [16]
    [  12] 
    [  13] 
    [  14] play music "t6s"
    [  15] goto [16]
    [  16] pass
    [  17] unless persistent.yuri_kill == 0 goto [25]
    [  18] with None
    [  19] scene black
    [  20] with dissolve_cg
    [  21] with None
    [  22] show y_kill
    [  23] with dissolve_cg
    [  24] goto [31]
    [  25] with None
    [  26] scene black
    [  27] with None
    [  28] with None
    [  29] show y_kill
    [  30] with None
    [  31] pass
    [  32] 
    [  33] window show(None)
    [  34] label label yuri_kill_loop:    # nested entry point
    [  35] 
    [  36] unless persistent.yuri_kill < 1440 goto [53]
    [  37] 
    [  38] unless persistent.has_skipped_yuri == False goto [44]
    [  39] unless config.skipping goto [42]
    [  40] 
    [  41] goto [42]
    [  42] pass
    [  43] goto [44]
    [  44] pass
    [  45] unless config.developer goto [48]
    [  46] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  47] goto [49]
    [  48] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  49] pass
    [  50] 
    [  51] jump yuri_kill_loop
    [  52] goto [57]
    [  53] 
    [  54] 
    [  55] hide y_kill
    [  56] jump yuri_kill_3
    [  57] pass
