label ch22_n_end2:
    [   0] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_n2b"], constantObjects=[] }>, revert_music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>)
    [   1] 
    [   2] n 1g "[player]..."
    [   3] n "Why didn't you come read with me today?"
    [   4] n 1m "I was waiting for you."
    [   5] n "I was waiting for a long time."
    [   6] n "It was the only thing I had to look forward to today."
    [   7] n "Why did you ruin it?"
    [   8] n "Do you like Yuri more?"
    [   9] n 1k "I think you're better off not associating with her."
    [  10] n "Are you listening to me?"
    [  11] show darkred at fed3708a66dcfbd4cae238e9a2f28e3f zorder 5
    [  12] 
    [  13] 
    [  14] stop musicpoem fadeout 2
    [  15] 
    [  16] show n_rects_ghost1 zorder 4
    [  17] show n_rects_ghost2 zorder 4
    [  18] show n_rects_ghost3 zorder 4
    [  19] n ghost1 "Yuri is a sick freak."
    [  20] n "That should be obvious by now."
    [  21] n "So just play with me instead."
    [  22] n "Okay?"
    [  23] n "You don't hate me, [player], do you?"
    [  24] n "Do you hate me?"
    [  25] show natsuki_ghost_blood at ng_blood_t zorder 3
    [  26] n "Do you want to make me go home crying?"
    [  27] n "The club is the only place I feel safe."
    [  28] n "Don't ruin that for me."
    [  29] n "Don't ruin it."
    [  30] n "Please."
    [  31] n "Just stop talking to Yuri."
    [  32] n "Play with me instead."
    [  33] n "It's all I have..."
    [  34] n "Play with me."
    [  35] stop music
    [  36] hide n_rects_ghost3
    [  37] n ghost2 "PLAY WITH ME!!!"
    [  38] 
    [  39] 
    [  40] 
    [  41] play sound "289e0ad6ba08858429346780981d7de5"
    [  42] hide natsuki_ghost_blood
    [  43] hide n_rects_ghost1
    [  44] hide n_rects_ghost2
    [  45] show natsuki ghost3
    [  46] show n_rects_ghost4 onlayer front zorder 4
    [  47] show n_rects_ghost5 onlayer front zorder 4
    [  48] 
    [  49] hide natsuki
    [  50] play sound "8d87507c00830ee4aaba05d7242edc23"
    [  51] show natsuki ghost4 at i11 onlayer front
    [  52] 
    [  53] window hide(None)
    [  54] hide natsuki
    [  55] hide n_rects_ghost4
    [  56] hide n_rects_ghost5
    [  57] scene black
    [  58] with None
    [  59] window auto
    [  60] scene black
    [  61] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="natsuki_bad_end", UnlockId=2743115698 }
    [  62] 
    [  63] show end at a3d2875dd08bc5040b696812204db3b6
    [  64] with dissolve_cg
    [  65] 
    [  66] scene black
    [  67] with None
    [  68] 
    [  69] return
