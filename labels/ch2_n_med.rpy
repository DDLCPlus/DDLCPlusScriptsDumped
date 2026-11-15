label ch2_n_med:
    # nested label ch2_n_med_shared starts at [5]
    [   0] unless n_poemappeal[0] < 0 goto [21]
    [   1] n "...Hm."
    [   2] n 2k "Well, I can admit that it's better than the last one."
    [   3] n "It's nice to see that you're putting in some effort."
    [   4] mc "That's good..."
    [   5] label label ch2_n_med_shared:    # nested entry point
    [   6] n 2c "Come to think of it, this kind of reminds me of Sayori's poem from yesterday..."
    [   7] mc "Eh? You think so?"
    [   8] n 2j "Yeah. Well I guess if you've been friends with her for so long, you might be on the same wavelength."
    [   9] n 2k "But you never really struck me as her type."
    [  10] mc "Sayori has a 'type' all of a sudden...?"
    [  11] n 42c "Well, I don't know! But honestly, how can someone so...er, fluffy...spend so much time with someone like you?"
    [  12] n "It's like she's dragging around a dead weight."
    [  13] mc "Uug... That was a little unnecessary..."
    [  14] mc "But think of it this way. If it weren't for me, she would probably just fly away like letting go of a balloon."
    [  15] mc "You could say we each take care of each other in our own way."
    [  16] n 2q "Whatever it is, I don't get it..."
    [  17] n "...Oh, yeah, I guess I'm supposed to show you my poem."
    [  18] n "Here."
    [  19] return
    [  20] goto [44]
    [  21] unless n_poemappeal[0] == 0 goto [37]
    [  22] n "...Hm."
    [  23] n 2k "Well, it's not really any worse than your last one."
    [  24] n "But I can't really say it's any better, either."
    [  25] mc "Phew..."
    [  26] n 2c "Huh? 'Phew' what?"
    [  27] mc "Ah... Well anything that isn't a trainwreck, I'll take as a win."
    [  28] mc "And I get the feeling you're probably the most critical."
    [  29] n 1p "H-Hey! What makes you--"
    [  30] n 1q "<i>(Wait, maybe that was a compliment...?)</i>"
    [  31] n 4y "A-Ahah! Glad to see someone recognizes my experience!"
    [  32] n "Well then, keep practicing and maybe you'll be as good as me someday!"
    [  33] mc "That's...uh..."
    [  34] "Something tells me Natsuki completely missed the point."
    [  35] jump ch2_n_med_shared
    [  36] goto [44]
    [  37] n "...Hm."
    [  38] n 2c "Well, it's not terrible."
    [  39] n "But it's pretty disappointing after your last one."
    [  40] n 2s "Then again, if this one was as good as your last one, I would be completely pissed."
    [  41] mc "Well, I guess I wanted to try something a little different this time."
    [  42] n 2c "Fair enough. You're still new to this, so I wouldn't expect you to find your style right away."
    [  43] jump ch2_n_med_shared
    [  44] pass
