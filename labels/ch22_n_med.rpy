label ch22_n_med:
    # nested label ch22_n_med_shared starts at [5]
    # nested label ch22_n_med_shared2 starts at [38]
    [   0] unless n_poemappeal[0] < 0 goto [17]
    [   1] n "...Hm."
    [   2] n 2k "Well, I can admit that it's better than the last one."
    [   3] n "It's nice to see that you're putting in some effort."
    [   4] mc "That's good..."
    [   5] label label ch22_n_med_shared:    # nested entry point
    [   6] n 2c "Just make sure you find a little bit of influence from everyone."
    [   7] n "I think you're at least being influenced by Yuri a little bit, aren't you?"
    [   8] n 5q "I mean, I know you've been, like..."
    [   9] n "Spending some time with her, or whatever..."
    [  10] n 1w "But you know, Monika and I are just as good as her!"
    [  11] n 1q "A-At poems, I mean!"
    [  12] n 1h "So you should really try to learn something, or you'll never get better!"
    [  13] n "Here's the one I wrote..."
    [  14] n "I'll make sure you learn something from it."
    [  15] return
    [  16] goto [50]
    [  17] unless n_poemappeal[0] == 0 goto [33]
    [  18] n "...Hm."
    [  19] n 2k "Well, it's not really any worse than your last one."
    [  20] n "But I can't really say it's any better, either."
    [  21] mc "Phew..."
    [  22] n 2c "Huh? 'Phew' what?"
    [  23] mc "Ah... Well anything that isn't a trainwreck, I'll take as a win."
    [  24] mc "And I get the feeling you're probably the most critical."
    [  25] n 1p "H-Hey! What makes you--"
    [  26] n 1q "<i>(Wait, maybe that was a compliment...?)</i>"
    [  27] n 4y "A-Ahah! Glad to see someone recognizes my experience!"
    [  28] n "Well then, keep practicing and maybe you'll be as good as me someday!"
    [  29] mc "That's...uh..."
    [  30] "Something tells me Natsuki completely missed the point."
    [  31] jump ch22_n_med_shared
    [  32] goto [50]
    [  33] n "...Hm."
    [  34] n 2c "Well, it's not terrible."
    [  35] n "But it's pretty disappointing after your last one."
    [  36] n 2s "Then again, if this one was as good as your last one, I would be completely pissed."
    [  37] mc "Well, I guess I wanted to try something a little different this time."
    [  38] label label ch22_n_med_shared2:    # nested entry point
    [  39] n 2c "Fair enough. You're still new to this, so I wouldn't expect you to find your style right away."
    [  40] n "I mean, everyone in the club writes really differently from each other..."
    [  41] n "Maybe you'll find a little influence from all of us."
    [  42] n 2q "For instance..."
    [  43] n 5q "I noticed that you were spending some time with Yuri today..."
    [  44] n "Not that I care who you spend your time with."
    [  45] n 5w "After all, I was taught never to expect anything from anybody."
    [  46] n 5s "So it's not like I was waiting for you, or anything."
    [  47] n 5h "Still, you should at least look over my poem..."
    [  48] n "You'll probably be able to learn something from it."
    [  49] return
    [  50] pass
