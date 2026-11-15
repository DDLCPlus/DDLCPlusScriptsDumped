label ch3_end_monika:
    [   0] 
    [   1] mc "Well, I guess I should probably be helping Monika..."
    [   2] show monika 5 at f32 zorder 3
    [   3] m "Yay, you picked me!"
    [   4] show monika at t32 zorder 2
    [   5] show natsuki 3e at f31 zorder 3
    [   6] stop music fadeout 1
    [   7] n "Hold on one second!"
    [   8] show natsuki at t31 zorder 2
    [   9] show yuri 2r at f33 zorder 3
    [  10] y "Y-Yeah!"
    [  11] show yuri at t33 zorder 2
    [  12] show natsuki at f31 zorder 3
    [  13] play music "t7"
    [  14] n "Monika, you're the one who needs the least help out of all of us!"
    [  15] show natsuki at t31 zorder 2
    [  16] show monika 1d at f32 zorder 3
    [  17] m "Eh? But..."
    [  18] show monika at t32 zorder 2
    [  19] show yuri 1h at f33 zorder 3
    [  20] y "I agree with Natsuki."
    [  21] y 1l "Not only is your work already most suitable for one person..."
    [  22] y "But you already have Sayori as well."
    [  23] show yuri at t33 zorder 2
    [  24] show monika at f32 zorder 3
    [  25] m 1p "But [player] was the one who..."
    [  26] m "Ah..."
    [  27] show monika at t32 zorder 2
    [  28] show natsuki 3c at f31 zorder 3
    [  29] n "That doesn't matter."
    [  30] n "You were the one who scared him into picking you in the first place."
    [  31] n 3e "You're the club president, Monika."
    [  32] n "You're supposed to make responsible decisions for the club!"
    [  33] show natsuki at t31 zorder 2
    [  34] show yuri 2f at f33 zorder 3
    [  35] y "Monika, you shouldn't let any ulterior motives interfere with this decision."
    [  36] show yuri at t33 zorder 2
    [  37] show monika 2i at f32 zorder 3
    [  38] m "Ulterior motives?"
    [  39] m "W-What are you saying, Yuri?"
    [  40] m "In fact, it sounds like you guys are the ones with ulterior motives!"
    [  41] show monika at t32 zorder 2
    [  42] show natsuki 1x at f31 zorder 3
    [  43] n "<i>Excuse</i> me?"
    [  44] show natsuki at t31 zorder 2
    [  45] show monika at f32 zorder 3
    [  46] m "Otherwise...this wouldn't have been made into such a big deal in the first place!"
    [  47] show monika at t32 zorder 2
    [  48] show yuri 3r at f33 zorder 3
    [  49] y "That's...completely false, Monika!"
    [  50] show yuri at t33 zorder 2
    [  51] show natsuki 3e at f31 zorder 3
    [  52] n "Yeah!"
    [  53] n "We have a lot of work to do, you know!"
    [  54] n "We won't do as good of a job if you make us work alone."
    [  55] show natsuki at t31 zorder 2
    [  56] show monika 1p at f32 zorder 3
    [  57] m "Ah...maybe...that's true..."
    [  58] show monika at t32 zorder 2
    [  59] show yuri 2l at f33 zorder 3
    [  60] y "Think of the club, Monika..."
    [  61] y "If we want our event to succeed, then we need to appropriately distribute our resources."
    [  62] show yuri at t33 zorder 2
    [  63] show monika 3n at f32 zorder 3
    [  64] m "Um..."
    [  65] m "Ah..."
    [  66] show monika at t32 zorder 2
    [  67] show natsuki 4x at f31 zorder 3
    [  68] n "So are you going to do the right thing, <i>President</i>?"
    [  69] show natsuki at t31 zorder 2
    [  70] show monika 1p at f32 zorder 3
    [  71] m "Okay, okay!"
    [  72] m "I get it!"
    [  73] stop music fadeout 1
    [  74] show natsuki 4g
    [  75] show yuri 2g
    [  76] m 1r "Sigh..."
    [  77] m 1g "It's...technically most logical for [player] to help one of you two."
    [  78] m "So..."
    [  79] m 1c "I guess...that's what we'll do."
    [  80] show monika at t32 zorder 2
    [  81] play music "t3"
    [  82] goto [89]
    [  83] call ch3_end_natsuki
    [  84] goto [91]
    [  85] call ch3_end_yuri
    [  86] goto [91]
    [  87] call ch3_end_sayori
    [  88] goto [91]
    [  89] m "Do you have a preference, [player]?{nw}"    # menu-with-caption
    [  90] menu:    # caption above
                "Natsuki.":  goto [83]
                "Yuri.":  goto [85]
                "Sayori..." if <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["help_sayori"], constantObjects=[] }>:  goto [87]
    [  91] pass
    [  92] return
