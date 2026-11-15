label ch3_n_bad:
    # nested label ch3_n_bad12_shared starts at [1]
    # nested label ch3_n_shared starts at [28]
    [   0] unless n_poemappeal[0] < 0 and n_poemappeal[1] < 0 goto [8]
    [   1] label label ch3_n_bad12_shared:    # nested entry point
    [   2] n 5x "Yeah, no thanks."
    [   3] mc "Eh? You didn't even--"
    [   4] n 5w "<i>Next!</i>"
    [   5] 
    [   6] return
    [   7] goto [61]
    [   8] unless n_poemappeal[0] < 0 or n_poemappeal[1] < 0 goto [17]
    [   9] n "..."
    [  10] n 2c "...Meh."
    [  11] n "I guess you really haven't learned anything after all."
    [  12] n "Honestly, I don't know why I got my hopes up in the first place."
    [  13] mc "What? I didn't think this one was that bad..."
    [  14] mc "What did I do wrong?"
    [  15] jump ch2_n_bad_sharedwithch3
    [  16] goto [61]
    [  17] n "..."
    [  18] n 2r "Oh, man."
    [  19] n "This is seriously a step backwards."
    [  20] mc "Eh?"
    [  21] n 2c "I liked your last two way better than this one."
    [  22] n 1k "I mean..."
    [  23] n "I guess I can't be mad at you for trying different things."
    [  24] n 1c "As long as you're not just trying to impress Yuri or something like that."
    [  25] n 5x "Gross."
    [  26] mc "Okay, okay."
    [  27] mc "Like you said, I'm allowed to try new things."
    [  28] label label ch3_n_shared:    # nested entry point
    [  29] show natsuki 5g
    [  30] mc "Why are you so emotionally invested in my poems, anyway?"
    [  31] mc "Isn't that more of a compliment to me?"
    [  32] n 1o "...Eh?"
    [  33] n 4x "N-No! Gross!"
    [  34] n 4w "It's not like I care!"
    [  35] n "It's just that <i>one</i> of us in this club has to make sure you're not slacking off."
    [  36] mc "Really?"
    [  37] mc "Well, what if you ended up just scaring me away?"
    [  38] n 1t "That's--um..."
    [  39] n "...It's not like you would actually do that."
    [  40] mc "Yeah, you're right."
    [  41] mc "It's kind of fun to hang out here, even if I have to put up with you."
    [  42] show natsuki 1x
    [  43] mc "<i>Guh--!!</i>"
    [  44] "Natsuki's elbow connects with my stomach."
    [  45] n 2y "Oh?"
    [  46] n "Maybe I won't mind scaring you away after all."
    [  47] mc "I was......just joking...."
    [  48] n 4z "Oh, I know!"
    [  49] n "Don't worry, I was too."
    [  50] n "Ahahaha!"
    [  51] show natsuki 4j
    [  52] mc "..."
    [  53] "How the hell do you call that a joke?"
    [  54] "That seriously hurt."
    [  55] "Well, maybe it was funny to her..."
    [  56] "...I guess that's kind of the point."
    [  57] "I should really just watch my mouth around Natsuki."
    [  58] n 2c "Anyway..."
    [  59] "Natsuki holds her poem out to me like nothing even happened."
    [  60] return
    [  61] pass
