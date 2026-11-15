label ch22_y_good:
    # nested label ch22_y_good_shared starts at [9]
    [   0] unless y_poemappeal[0] < 1 goto [32]
    [   1] y 2b "I've been waiting for this..."
    [   2] y "Let's see what you've written for today."
    [   3] y 2e "..."
    [   4] y "......"
    [   5] "Yuri stares at the poem with a surprised expression on her face."
    [   6] mc "Do you...like it?"
    [   7] y "[player]..."
    [   8] y "...How did you pick up on this so quickly?"
    [   9] label label ch22_y_good_shared:    # nested entry point
    [  10] y 2v "Just yesterday, I was telling you the kind of techniques worth practicing..."
    [  11] mc "Maybe that's why..."
    [  12] mc "You did a good job explaining."
    [  13] mc "I really wanted to try giving it more imagery."
    [  14] show yuri 4b at t11 zorder 2
    [  15] "Yuri visibly swallows."
    [  16] "Even her hands appear sweaty."
    [  17] y 4e "A-Ah..."
    [  18] y "That makes me so happy..."
    [  19] y 3y5 "It's so amazing to feel like I'm valued, [player]!"
    [  20] y "Everything that you write is a treasure to me."
    [  21] y 3m "My heart pounds just holding it..."
    [  22] y 3q "Ahaha..."
    [  23] y "I want to write a poem about this feeling..."
    [  24] y 3y6 "Is that bad, [player]?"
    [  25] y "I'm not being weird, right?"
    [  26] y 3s "I-I'm having a harder time than usual at concealing my emotions..."
    [  27] y 3m "I'm kind of embarrassed."
    [  28] y 3y6 "But right now, I just want you to read my poem, too."
    [  29] y 3y5 "Okay?"
    [  30] return
    [  31] goto [42]
    [  32] y 2b "I've been waiting for this..."
    [  33] y "Let's see what you've written for today."
    [  34] y 2e "..."
    [  35] y "......"
    [  36] "Yuri stares at the poem with a surprised expression on her face."
    [  37] mc "Do you...like it?"
    [  38] y "[player]..."
    [  39] y 2t "This one might even be better than yesterday's..."
    [  40] y "...How did you even pick up on this so quickly?"
    [  41] jump ch22_y_good_shared
    [  42] pass
