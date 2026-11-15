label ch2_n_good:
    # nested label ch2_n_good_sharedwithch3 starts at [31]
    [   0] unless n_poemappeal[0] != 1 goto [31]
    [   1] n 1h "..."
    [   2] "Natsuki reads my poem."
    [   3] "She keeps glancing at me, then back at the poem."
    [   4] "By now, she must have read it more than once."
    [   5] n 1q "...Aren't you supposed to be bad at this?"
    [   6] mc "...Is that a compliment?"
    [   7] n 1o "N-No! I mean... You know..."
    [   8] "Natsuki struggles to find the words she wants."
    [   9] n 5w "I just...expected a lot less after what you showed me yesterday."
    [  10] n "That's all."
    [  11] mc "Well, I guess I just got lucky with this one."
    [  12] n 4t "Y-Yeah!! Exactly!"
    [  13] n "You just got lucky, you know?"
    [  14] n 4y "Don't get used to it."
    [  15] n "You won't always manage to write poems this cute. I mean--!"
    [  16] n 1p "I mean well-written! No, I mean--"
    [  17] mc "Ah, so that's how it is. My poem is cute?"
    [  18] n 1v "No! Why are you smiling?! It's not like I like cute things!"
    [  19] "Natsuki shoves my poem back towards me."
    [  20] n 4w "H-Huh! Reading it again, I decided that it's not so great after all."
    [  21] n "It's too cute and doki-doki."
    [  22] n 4t "It would only impress...you know, girls...who like those kinds of things."
    [  23] n "Ahaha!"
    [  24] "For some reason, Natsuki is incredibly easy to see through."
    [  25] n 1w "Well, anyway...!"
    [  26] n 1h "You're gonna read mine now, right?"
    [  27] n "Judging by your tastes, you'll probably like it a lot."
    [  28] n 2q "You'll probably learn something, too. Don't forget who the <i>real</i> pro is."
    [  29] return
    [  30] goto [172]
    [  31] label label ch2_n_good_sharedwithch3:    # nested entry point
    [  32] n 1n "..."
    [  33] "Natsuki reads my poem."
    [  34] "She keeps glancing at me, then back at the poem."
    [  35] "By now, she must have read it more than once."
    [  36] n 1u "Rrgh..."
    [  37] mc "...?"
    [  38] mc "Is it that bad?"
    [  39] n 1r "No! No, it's not!"
    [  40] n "It's good. It's really good, okay?!"
    [  41] n 5w "There, I said it!"
    [  42] n "Ugh, this wasn't supposed to happen at all...!"
    [  43] n 5s "Why can't you just be bad at this?"
    [  44] n "My poems are supposed to impress <i>you</i>, not the other way around!"
    [  45] mc "You're trying to impress me?"
    [  46] n 12c "Obviously! You think I'd let you enjoy Yuri's writing more than mine?"
    [  47] n "Give me a break."
    [  48] mc "Well..."
    [  49] mc "In that case, what's the problem with me trying to impress you?"
    [  50] n 1e "I'll tell you! You--"
    [  51] n 1p "--"
    [  52] "Natsuki's face freezes, like she just realized something."
    [  53] n "Y-Y-You..."
    [  54] n "You're trying to...impress <i>me?</i>"
    [  55] show natsuki 1q
    [  56] "Natsuki vigorously scans her eyes over my poem one more time."
    [  57] "Then, the poem slips out of her hands and flutters to the floor."
    [  58] n 1p "I...have to use the bathroom!"
    [  59] show natsuki at lhide
    [  60] hide natsuki
    [  61] "Red-faced, Natsuki quickly walks out of the room."
    [  62] show monika 1d at t11 zorder 2
    [  63] m "Hey, [player]..."
    [  64] m "Did you do something to Natsuki?"
    [  65] m "I just saw her rush out like that..."
    [  66] m 2g "You didn't do anything terrible, did you?"
    [  67] mc "N-No!"
    [  68] mc "I just told her that--"
    [  69] "My voice gets caught in my throat."
    [  70] "There's no way I could tell Monika that I'm trying to impress Natsuki."
    [  71] m 2d "Hmm?"
    [  72] "Monika sees the poem lying on the floor and swiftly picks it up."
    [  73] unless m_readpoem goto [79]
    [  74] "She skims over it a second time, her smile not fading from her face."
    [  75] m 2a "I see."
    [  76] m "At first I just thought you liked her writing style..."
    [  77] m "But you wrote this <i>for</i> Natsuki, didn't you?"
    [  78] goto [83]
    [  79] 
    [  80] "She reads through it, her smile not fading from her face."
    [  81] m 2a "I see."
    [  82] m "You wrote this for Natsuki, didn't you?"
    [  83] pass
    [  84] mc "I-I mean..."
    [  85] mc "Not really..."
    [  86] m 2d "In fact, didn't she like your poem a lot the other day, too?"
    [  87] m "I'm surprised you know her taste so well already."
    [  88] m 4a "Are you sure you're not cheating, [player]?"
    [  89] mc "Cheating...?"
    [  90] mc "What do you mean by that?"
    [  91] m 5a "Never mind, I'm just kidding. Ahaha!"
    [  92] "I didn't understand Monika's joke at all."
    [  93] m "Anyway..."
    [  94] m 1a "How do you think Natsuki feels about you?"
    [  95] m "Oh, you don't need to answer that."
    [  96] m "It was just something for you to think about."
    [  97] show monika at t22 zorder 2
    [  98] show natsuki 4e at l21
    [  99] n "Hey!"
    [ 100] "Natsuki comes up and snatches the poem out of Monika's hands."
    [ 101] "Neither of us had noticed her reenter the classroom."
    [ 102] show natsuki at f21 zorder 3
    [ 103] n "Did you read this, Monika?"
    [ 104] show natsuki at t21 zorder 2
    [ 105] show monika at f22 zorder 3
    [ 106] m 1j "Of course! I liked it!"
    [ 107] show monika 1a at t22 zorder 2
    [ 108] show natsuki at f21 zorder 3
    [ 109] n 1r "Ugh..."
    [ 110] n "You should really stop reading things that aren't for you, you know."
    [ 111] n "You have a bad habit of doing that."
    [ 112] show natsuki at t21 zorder 2
    [ 113] show monika at f22 zorder 3
    [ 114] m 1d "Eh?"
    [ 115] m "But [player] wrote this poem."
    [ 116] m 1a "And we're supposed to share with everyone, right?"
    [ 117] show monika at t22 zorder 2
    [ 118] show natsuki at f21 zorder 3
    [ 119] n 1x "Uu--"
    [ 120] "Natsuki freezes."
    [ 121] "She apparently forgot that my poem is technically for everyone to read."
    [ 122] n 42c "Okay, well, I think [player] is done sharing this poem with everyone."
    [ 123] n "It's not like anyone would want to read this anyway."
    [ 124] n 4h "In fact, I'm just going to hold onto this."
    [ 125] show natsuki at t21 zorder 2
    [ 126] show monika at f22 zorder 3
    [ 127] m 5 "If you insist~"
    [ 128] show monika at t22 zorder 2
    [ 129] show natsuki at f21 zorder 3
    [ 130] n 1i "What?"
    [ 131] n "Why are you looking at me like that??"
    [ 132] show natsuki at t21 zorder 2
    [ 133] show monika at f22 zorder 3
    [ 134] m "Like what?"
    [ 135] show monika at t22 zorder 2
    [ 136] show natsuki at f21 zorder 3
    [ 137] n 12b "Ugh..."
    [ 138] n "Never mind."
    [ 139] unless s_readpoem and y_readpoem goto [143]
    [ 140] "Well, I guess Natsuki has my poem now."
    [ 141] "Not that I really planned on keeping it."
    [ 142] goto [164]
    [ 143] 
    [ 144] unless s_readpoem goto [147]
    [ 145] 
    [ 146] goto [147]
    [ 147] pass
    [ 148] show natsuki at t21 zorder 2
    [ 149] mc "Ah, Natsuki..."
    [ 150] # RenpyDialogueLine: RenpyDialogueLine {  }
    [ 151] mc "...She hasn't gotten to read it yet."
    [ 152] show natsuki at f21 zorder 3
    [ 153] n 2q "So what?"
    [ 154] show natsuki at t21 zorder 2
    [ 155] show monika at f22 zorder 3
    [ 156] m 2a "Well... I guess [player] is right, Natsuki..."
    [ 157] m "It's not fair if you don't let everyone finish reading it."
    [ 158] show monika at t22 zorder 2
    [ 159] show natsuki at f21 zorder 3
    [ 160] n "..."
    [ 161] n 2h "...Fine."
    [ 162] "Natsuki returns my poem."
    [ 163] n "It's not like she's going to like it, though."
    [ 164] pass
    [ 165] show monika at thide zorder 1
    [ 166] show natsuki at t11 zorder 2
    [ 167] hide monika
    [ 168] n 2h "Anyway, read my poem now."
    [ 169] n 4h "And no, I won't let you keep it."
    [ 170] n "This is my only copy."
    [ 171] return
    [ 172] pass
