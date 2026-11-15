label ch2_n_bad:
    # nested label ch2_n_bad_sharedwithch3 starts at [8]
    [   0] unless n_poemappeal[0] < 0 goto [33]
    [   1] n "...Hm."
    [   2] n 2k "Well, I can admit that it's better than the last one."
    [   3] n "It's nice to see that you're putting in some effort."
    [   4] mc "That's good..."
    [   5] n 2c "But I still don't like this at all."
    [   6] n "It's trying too hard to be serious."
    [   7] mc "Eh? What do you mean by that?"
    [   8] label label ch2_n_bad_sharedwithch3:    # nested entry point
    [   9] n 4c "Poems don't need to be all deep-sounding to express something."
    [  10] n "It's going to just sound like you're forcing it unless you really don't suck at it."
    [  11] n 4w "Honestly... Don't bother trying to write poems like this until you're on Yuri's level--"
    [  12] show natsuki 4o
    [  13] "Natsuki stops short all of a sudden."
    [  14] n 1o "D-Don't...tell me..."
    [  15] mc "Eh?"
    [  16] n "You're not...you're not just trying to impress Yuri, are you?!"
    [  17] mc "W-What are you talking about?? And keep your voice down...!"
    [  18] n 1x "You know Yuri would love this kind of...this angsty.......!!"
    [  19] mc "Just because she's a talented writer doesn't mean...I-I mean..."
    [  20] n 1o "Uu....!!"
    [  21] "Looks like I'm in trouble."
    [  22] "I somehow struck a nerve, though what I did is beyond me."
    [  23] n 1c "I am so done with you."
    [  24] "Natsuki shoves the poem I handed her back over to me."
    [  25] n 5w "Take your stupid poem. If you wrote it for someone else, just don't show it to me!"
    [  26] mc "Ouch..."
    [  27] "This is what I get for letting a younger girl step into my business."
    [  28] "Unless I was a mind reader, I was destined to be in a world of pain from the start."
    [  29] "At least Natsuki wasn't really the girl I was trying to impress in the first place..."
    [  30] 
    [  31] return
    [  32] goto [51]
    [  33] n 1k "...Hm."
    [  34] n "I liked your last one better."
    [  35] mc "Eh? Really?"
    [  36] n 2c "Well yeah. I can tell you were a little more daring with this one."
    [  37] n "But you're really not good enough for that yet. It fell flat."
    [  38] mc "That may be true, but I just wanted to try something different."
    [  39] mc "I'm still figuring this all out."
    [  40] n 2k "I mean, I always like poems that aren't trying too hard."
    [  41] n 2q "I hate when people try to sound fancy or add more meaning just by using annoying and complicated language."
    [  42] n 4b "Just make it simple, cute, and to the point!"
    [  43] n 4y "Yuri's head over heels for all this cryptic nonsense, but I see right through that BS. Hah!"
    [  44] n 42a "Making your reader look so hard for all this deep meaning is just an excuse to have no meaning at all."
    [  45] mc "I guess that's one way to look at it."
    [  46] n 2d "Well, everyone has their own opinion."
    [  47] n "But my opinion is the best opinion. I'm sure you've figured that out already."
    [  48] mc "Er..."
    [  49] n 2a "Anyway, here's my poem. Maybe you'll learn something."
    [  50] return
    [  51] pass
