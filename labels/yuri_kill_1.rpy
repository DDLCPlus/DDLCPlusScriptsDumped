label yuri_kill_1:
    [   0] window auto
    [   1] 
    [   2] 
    [   3] 
    [   4] stop music
    [   5] scene bg club_day
    [   6] show yuri 3d at i11
    [   7] y "...Ahahaha."
    [   8] y "Ahahahahahaha!"
    [   9] 
    [  10] y 3y5 "Ahahahahahahahaha!"
    [  11] 
    [  12] y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    [  13] unless persistent.stab_censor == True goto [18]
    [  14] scene black
    [  15] show noise at ee331df39dbaf12419bb7f459269e4cf
    [  16] show yuri 3y3 at i11
    [  17] goto [18]
    [  18] pass
    [  19] 
    [  20] 
    [  21] window hide(None)
    [  22] window auto
    [  23] 
    [  24] unless persistent.stab_censor == True goto [57]
    [  25] play sound "c5877b861dbffdb4899f5b4b5c5cf05c"
    [  26] 
    [  27] 
    [  28] show yuri stab_1
    [  29] 
    [  30] hide yuri
    [  31] show stab_censor stab_censor_2 at i11
    [  32] show blood_censor at 8127786a842fc604d81a83b6022b6b43
    [  33] 1.25
    [  34] 
    [  35] show stab_censor stab_censor_3
    [  36] 
    [  37] show stab_censor stab_censor_2
    [  38] show blood_censor at d8ecde30d49ad8445a49b74be35ec061
    [  39] with None
    [  40] show stab_censor stab_censor_4
    [  41] with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    [  42] 
    [  43] show stab_censor stab_censor_5
    [  44] 
    [  45] show stab_censor stab_censor_6 at 6d61dce3b17f8e449a99467d9fefa1c1
    [  46] show blood_censor as blood2 at 5c7e94d678a086a44a138789d20e446d
    [  47] 
    [  48] hide blood_censor
    [  49] hide blood2
    [  50] 
    [  51] play sound "fall"
    [  52] 
    [  53] show black zorder 3
    [  54] 
    [  55] scene black
    [  56] goto [87]
    [  57] play sound "f96d27f301eb00049b8fb131a0b06ac7"
    [  58] 
    [  59] 
    [  60] show yuri stab_1
    [  61] 
    [  62] show yuri stab_2
    [  63] show blood at 243eb1a249a47264a839ef686a368d27
    [  64] 1.25
    [  65] 
    [  66] show yuri stab_3
    [  67] 
    [  68] show yuri stab_2
    [  69] show blood at 33c84db0a10ed684aa16344b412470da
    [  70] with None
    [  71] show yuri stab_4
    [  72] with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    [  73] 
    [  74] show yuri stab_5
    [  75] 
    [  76] show yuri stab_6 at 6c6e3cbf1aad17d4e8aa0113f9207782
    [  77] show blood2 at 33df7b6087812834a8d8761840f576e5
    [  78] 
    [  79] hide blood
    [  80] hide blood2
    [  81] 
    [  82] play sound "fall"
    [  83] 
    [  84] show black zorder 3
    [  85] 
    [  86] scene black
    [  87] pass
    [  88] 
    [  89] jump yuri_kill_2
