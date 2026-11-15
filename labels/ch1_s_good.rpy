label ch1_s_good:
    [   0] s 1n "..."
    [   1] s "...Oh my goodness!"
    [   2] s 4b "This is sooooo good, [player]!"
    [   3] mc "Eh?"
    [   4] s 4r "I love it~!"
    [   5] s "I had no idea you were such a good writer!"
    [   6] mc "Sayori..."
    [   7] mc "You must be seriously overreacting."
    [   8] mc "I'm not a good writer at all."
    [   9] mc "I honestly have no idea what I'm doing."
    [  10] s 1x "Well..."
    [  11] s "Maybe that's why!"
    [  12] s "Because I have no idea what I like, either!"
    [  13] s 1r "Ahahaha!"
    [  14] mc "Jeez..."
    [  15] unless y_readpoem goto [18]
    [  16] "Yuri's opinion was way more constructive than this..."
    [  17] goto [19]
    [  18] "I'm sure Yuri's opinion has to be a little more constructive than this."
    [  19] pass
    [  20] unless not n_readpoem goto [23]
    [  21] "Maybe even Natsuki's."
    [  22] goto [23]
    [  23] pass
    [  24] mc "Are you sure you don't like it just because I wrote it?"
    [  25] s 1b "Eh?"
    [  26] s "Well, I'm sure that's part of it."
    [  27] s 1x "I think I understand you better than a lot of other people, you know?"
    [  28] s "So when I read your poem..."
    [  29] s "It's not just a poem..."
    [  30] s 4q "It's a [player] poem!"
    [  31] s "And that makes it feel extra special!"
    [  32] s "Like I can feel your feelings in it~"
    [  33] "Sayori hugs the sheet against her chest."
    [  34] mc "You're so weird, Sayori..."
    [  35] s "Ehehe..."
    [  36] jump ch1_s_shared
