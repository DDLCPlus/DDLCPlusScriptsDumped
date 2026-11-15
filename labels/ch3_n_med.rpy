label ch3_n_med:
    [   0] unless n_poemappeal[0] < 0 and n_poemappeal[1] < 0 goto [3]
    [   1] jump ch3_n_bad12_shared
    [   2] goto [23]
    [   3] unless n_poemappeal[1] != 0 goto [13]
    [   4] n "..."
    [   5] n 2k "...This one's alright."
    [   6] mc "Alright?"
    [   7] n "Well, yeah."
    [   8] n "It doesn't blow me away."
    [   9] n "But there's nothing I really hate about it."
    [  10] n "It's just not really my style. I mean, that's fine."
    [  11] jump ch2_n_med_shared
    [  12] goto [23]
    [  13] n "..."
    [  14] n 2k "...This one's alright."
    [  15] mc "Alright?"
    [  16] n "Well, yeah."
    [  17] n "About as good as yesterday's, anyway."
    [  18] n "I see what you're going for, but it's just not really my style."
    [  19] n 2a "I mean, that's fine."
    [  20] n "I'm mostly just glad that you're trying a little bit."
    [  21] mc "Well, of course I'm at least trying."
    [  22] jump ch3_n_shared
    [  23] pass
