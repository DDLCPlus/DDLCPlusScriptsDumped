label poemresponse_start:
    # nested label poemresponse_loop starts at [2]
    [   0] 
    [   1] 
    [   2] label label poemresponse_loop:    # nested entry point
    [   3] 
    [   4] unless renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c) goto [8]
    [   5] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="bgm_okayeveryone", UnlockId=546343283 }
    [   6] play music "t5" fadeout 1
    [   7] goto [8]
    [   8] pass
    [   9] unless skip_transition goto [12]
    [  10] scene bg club_day
    [  11] goto [14]
    [  12] scene bg club_day
    [  13] with wipeleft_scene
    [  14] pass
    [  15] 
    [  16] unless not renpy.music.get_playing() goto [20]
    [  17] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="bgm_okayeveryone", UnlockId=546343283 }
    [  18] play music "t5"
    [  19] goto [20]
    [  20] pass
    [  21] jump poemresponse_start2
