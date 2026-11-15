label ch23_n_med:
    # nested label ch23_n_shared starts at [12]
    [   0] unless y_gave goto [3]
    [   1] jump ch23_n_ygave
    [   2] goto [3]
    [   3] pass
    [   4] unless n_poemappeal[0] < 0 and n_poemappeal[1] < 0 goto [7]
    [   5] jump ch23_n_bad
    [   6] goto [32]
    [   7] unless n_poemappeal[1] < 0 goto [26]
    [   8] n "..."
    [   9] n 2k "...This one's alright."
    [  10] mc "Alright?"
    [  11] n "Yeah, it's at least better than yesterday's."
    [  12] label label ch23_n_shared:    # nested entry point
    [  13] n 2c "I still can't really tell how much you actually care about writing, but either way, you're doing alright."
    [  14] n 4r "Even though you're not really spending time with anyone but Yuri..."
    [  15] n 4h "I still think it's nice to have activities that we all participate in."
    [  16] n 4w "So you better keep working hard!"
    [  17] n "I mean..."
    [  18] n 1h "I know I'm not President or Vice President or anything..."
    [  19] n "But that doesn't mean you can let me down, okay?"
    [  20] n 1q "So, at least read mine too for now."
    [  21] n "But just to be clear..."
    [  22] n 1h "This poem...means a lot to me."
    [  23] n "So read it carefully, okay?"
    [  24] return
    [  25] goto [32]
    [  26] n "..."
    [  27] n 2k "...This one's alright."
    [  28] mc "Alright?"
    [  29] n "Well, yeah."
    [  30] n "About as good as yesterday's, anyway."
    [  31] jump ch23_n_shared
    [  32] pass
