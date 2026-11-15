label ch22_n_bad:
    [   0] unless n_poemappeal[0] < 0 goto [19]
    [   1] n 1r "..."
    [   2] n "Yeah, just as I thought..."
    [   3] mc "...?"
    [   4] n 2w "[player], come on."
    [   5] n "I'm not stupid."
    [   6] n 2h "I know how much time you've been spending with Yuri..."
    [   7] n "It's obvious that you care more about impressing her than trying to improve your writing."
    [   8] n 2w "To put it bluntly, it's kind of pathetic."
    [   9] n 4h "Why are you even in this club, [player]?"
    [  10] n "Honestly..."
    [  11] n "I thought getting a new member would help everyone get more involved together."
    [  12] n 4s "Not exclude each other even more."
    [  13] n 1u "This is such a stupid activity anyway..."
    [  14] n 12c "...Look, I'm not in a good mood today, and I just really don't feel like talking right now."
    [  15] n "Please go away."
    [  16] 
    [  17] return
    [  18] goto [27]
    [  19] n 1k "...Hm."
    [  20] n "I liked your last one better."
    [  21] mc "Eh? Really?"
    [  22] n 2c "Well yeah. I can tell you were a little more daring with this one."
    [  23] n "But you're really not good enough for that yet. It fell flat."
    [  24] mc "That may be true, but I just wanted to try something different."
    [  25] mc "I'm still figuring this all out."
    [  26] jump ch22_n_med_shared2
    [  27] pass
