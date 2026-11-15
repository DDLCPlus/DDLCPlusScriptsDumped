label ch23_n_bad:
    # nested label ch23_n_bad_shared starts at [19]
    [   0] unless y_gave goto [3]
    [   1] jump ch23_n_ygave
    [   2] goto [3]
    [   3] pass
    [   4] unless n_poemappeal[0] < 0 and n_poemappeal[1] < 0 goto [14]
    [   5] n 5x "I'm not going to read another one of your Yuri suck-up poems."
    [   6] n 5s "But I'm still going to make you read mine."
    [   7] n "There's a reason."
    [   8] n 5x "I really wish I didn't have to do this..."
    [   9] n "But unfortunately I don't have much of a choice."
    [  10] n 5h "Just...read it carefully, okay?"
    [  11] n "Then you can go away."
    [  12] return
    [  13] goto [40]
    [  14] unless n_poemappeal[0] < 0 or n_poemappeal[1] < 0 goto [34]
    [  15] n "..."
    [  16] n 2c "...Meh."
    [  17] n "I guess you really haven't learned anything after all."
    [  18] n "Honestly, I don't know why I got my hopes up in the first place."
    [  19] label label ch23_n_bad_shared:    # nested entry point
    [  20] n 42c "This is clearly Yuri's influence..."
    [  21] n "I didn't realize you were so impressionable."
    [  22] n "Spending all this time with her in the club..."
    [  23] n "Now trying to write like her..."
    [  24] n 1s "This is stupid."
    [  25] n "At least Monika appreciates my writing..."
    [  26] n 1r "...Ugh."
    [  27] n 1q "Okay...I guess I'm going to share my poem with you now."
    [  28] n "I really hate that I have to do this."
    [  29] n "But unfortunately I don't have much of a choice."
    [  30] n 1h "Just...read it carefully, okay?"
    [  31] n "Then you can go away."
    [  32] return
    [  33] goto [40]
    [  34] n "..."
    [  35] n 2r "Oh, man."
    [  36] n "This is seriously a step backwards."
    [  37] mc "Eh?"
    [  38] n 2c "I liked your last two way better than this one."
    [  39] jump ch23_n_bad_shared
    [  40] pass
