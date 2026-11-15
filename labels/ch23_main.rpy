label ch23_main:
    [   0] unless renpy.random.randint(0,15) == 0 and seen_eyes_this_chapter == 0 goto [12]
    [   1] 
    [   2] scene white
    [   3] show noface1
    [   4] show noface2
    [   5] with dissolve_scene_half
    [   6] play sound "5e908100f05e2754891064ee22ffa901"
    [   7] 
    [   8] 
    [   9] scene bg club_day2
    [  10] show yuri 2 at i11 zorder 2
    [  11] goto [14]
    [  12] scene bg club_day2
    [  13] with dissolve_scene_half
    [  14] pass
    [  15] play music "t6"
    [  16] show yuri 2y5 at t11 zorder 2
    [  17] dc "Don't Skip Previous Line on AutoSave"    # say, developer commentary
    [  18] 
    [  19] y "Hi, [player]!"
    [  20] y "I've been waiting for you."
    [  21] y 2d "Are you ready to continue reading?"
    [  22] y "I brought my best tea today--"
    [  23] show yuri 2f
    [  24] show natsuki 4w at f33 zorder 3
    [  25] n "Monika!"
    [  26] n "I told you not to--"
    [  27] n 1g "Ugh..."
    [  28] n "Is she really late again?"
    [  29] show natsuki at t33 zorder 2
    [  30] show yuri at f32 zorder 3
    [  31] y 1h "Inconsiderate as usual, Natsuki."
    [  32] show yuri at t32 zorder 2
    [  33] show natsuki at f33 zorder 3
    [  34] n 4c "Excuse me?"
    [  35] show natsuki at t33 zorder 2
    [  36] show yuri at f32 zorder 3
    [  37] y 1r "Must you always interrupt my conversations with your incessant yelling?"
    [  38] show yuri at t32 zorder 2
    [  39] show natsuki at f33 zorder 3
    [  40] n 1o "What are you talking about?!"
    [  41] n 1q "You say that like I do it on a regular basis or something."
    [  42] n "I just wasn't paying attention, okay? I'm sorry."
    [  43] n 4u "Seriously... What's gotten into you lately?"
    [  44] unless n_appeal >= 2 goto [88]
    [  45] n "Look..."
    [  46] n "I did some thinking about yesterday."
    [  47] n 2q "I was a little more hostile than I meant to be..."
    [  48] n 1q "I guess I really felt threatened or something."
    [  49] n 1h "But I know this is something we're doing together."
    [  50] n 1q "Another new member wouldn't hurt, as long as they're cool..."
    [  51] n 5w "And I guess another girl would be nice this time..."
    [  52] n 5u "So..."
    [  53] show natsuki at t33 zorder 2
    [  54] show yuri at f32 zorder 3
    [  55] 
    [  56] y 2u "Natsuki..."
    [  57] 
    [  58] y 1f "Nobody cares."
    [  59] y "Why don't you go look for some coins under the vending machines or something?"
    [  60] 
    [  61] show yuri at t32 zorder 2
    [  62] show natsuki at f33 zorder 3
    [  63] n 1p "--!"
    [  64] n 1r "..."
    [  65] n 12f "..."
    [  66] show natsuki at thide
    [  67] hide natsuki
    [  68] 
    [  69] show monika 1g at l31
    [  70] m "Aw, man..."
    [  71] m "I'm the last one here again!"
    [  72] show yuri at f32 zorder 3
    [  73] y 1f "Were you practicing piano again?"
    [  74] show yuri at t32 zorder 2
    [  75] show monika at f31 zorder 3
    [  76] m 5a "Yeah..."
    [  77] m "Ahaha..."
    [  78] show monika at t31 zorder 2
    [  79] show yuri at f32 zorder 3
    [  80] y 1m "You must have a lot of determination."
    [  81] y "Starting this club, and still trying to make time for piano..."
    [  82] show yuri 1a at t32 zorder 2
    [  83] show monika at f31 zorder 3
    [  84] m 1a "Well, maybe not determination..."
    [  85] m 3a "But I guess passion."
    [  86] m "It motivates me to work hard for the festival, too."
    [  87] goto [187]
    [  88] show natsuki at t33 zorder 2
    [  89] show yuri at f32 zorder 3
    [  90] y 2n "Me?"
    [  91] y 2o "N-Nothing..."
    [  92] show yuri at t32 zorder 2
    [  93] show natsuki at f33 zorder 3
    [  94] n "..."
    [  95] show natsuki at t33 zorder 2
    [  96] show yuri at f32 zorder 3
    [  97] y 2v "Is it really that bad...?"
    [  98] show yuri at t32 zorder 2
    [  99] show natsuki at f33 zorder 3
    [ 100] n 2m "See, it <i>is</i> something."
    [ 101] show natsuki at t33 zorder 2
    [ 102] show yuri at f32 zorder 3
    [ 103] y 3p "I'll get over it!"
    [ 104] y 3y6 "It's not even anything noteworthy..."
    [ 105] y 3o "I've just been feeling a little on edge lately..."
    [ 106] y 3n "A-Anyway, we don't need to talk about it!"
    [ 107] show yuri at t32 zorder 2
    [ 108] show natsuki at f33 zorder 3
    [ 109] n 2q "Well, I just felt like I needed to bring it up."
    [ 110] n 5q "It's not like I really care or anything..."
    [ 111] show natsuki at t33 zorder 2
    [ 112] show yuri 3e
    [ 113] show monika 1g at l31
    [ 114] m "Aw, man..."
    [ 115] m "I'm the last one here again!"
    [ 116] show natsuki at f33 zorder 3
    [ 117] n 2c "Well, [player] just walked in too."
    [ 118] show natsuki at t33 zorder 2
    [ 119] show yuri at f32 zorder 3
    [ 120] y 1f "Were you practicing piano again?"
    [ 121] show yuri at t32 zorder 2
    [ 122] show monika at f31 zorder 3
    [ 123] m 5a "Yeah..."
    [ 124] m "Ahaha..."
    [ 125] show monika at t31 zorder 2
    [ 126] show yuri at f32 zorder 3
    [ 127] y 1m "You must have a lot of determination."
    [ 128] y "Starting this club, and still trying to make time for piano..."
    [ 129] show yuri 1a at t32 zorder 2
    [ 130] show monika at f31 zorder 3
    [ 131] m 1a "Well, maybe not determination..."
    [ 132] m 3a "But I guess passion."
    [ 133] m "It motivates me to work hard for the festival and..."
    [ 134] m 3n "Um..."
    [ 135] show monika at t31 zorder 2
    [ 136] show natsuki at f33 zorder 3
    [ 137] n 5s "..."
    [ 138] show natsuki at t33 zorder 2
    [ 139] show monika at f31 zorder 3
    [ 140] m 1l "Right..."
    [ 141] m "I-I forgot..."
    [ 142] show monika at thide zorder 1
    [ 143] hide monika
    [ 144] show yuri at f32 zorder 3
    [ 145] y 2v "Um, about that, Natsuki..."
    [ 146] y "We were all talking yesterday, and..."
    [ 147] y 2t "Well...we decided that we would like to support the festival as well."
    [ 148] y 2l "However...!"
    [ 149] y 2h "I understand how you feel about not wanting the club to change."
    [ 150] y "I think we all kind of feel that way."
    [ 151] y 2f "So as long as we're all working together, this club will never become something we don't want."
    [ 152] show yuri at t32 zorder 2
    [ 153] show natsuki at f33 zorder 3
    [ 154] n "..."
    [ 155] show natsuki at t33 zorder 2
    [ 156] show yuri at f32 zorder 3
    [ 157] y 2v "Um, also..."
    [ 158] y "If you help us out with the festival..."
    [ 159] y 3r "...Then I'll buy you a new manga!"
    [ 160] show yuri 3t at t32 zorder 2
    [ 161] show natsuki at f33 zorder 3
    [ 162] n 5h "..."
    [ 163] n 2z "Ahahaha!"
    [ 164] n "Sorry, that last part was really funny."
    [ 165] n 2c "Look..."
    [ 166] n "I did some thinking about yesterday."
    [ 167] n 2q "I was a little more hostile than I meant to be..."
    [ 168] n 1q "I guess I really felt threatened or something."
    [ 169] n 1h "But I know this is something we're doing together."
    [ 170] n 1q "Another new member wouldn't hurt, as long as they're cool..."
    [ 171] n 5w "And I guess another girl would be nice this time..."
    [ 172] n 5e "...But more importantly, I would hate to see the event suck just because I chose to back out!"
    [ 173] n "I'm a pro, you know!"
    [ 174] n 5c "So I'm gonna help too, and we'll make sure it's done right."
    [ 175] show natsuki at t33 zorder 2
    [ 176] show yuri at f32 zorder 3
    [ 177] y 2s "Thank goodness..."
    [ 178] y "Isn't that great, Monika?"
    [ 179] show yuri at t32 zorder 2
    [ 180] show natsuki at f33 zorder 3
    [ 181] n 2k "...Monika?"
    [ 182] show natsuki at t33 zorder 2
    [ 183] show monika 1o at f31 zorder 3
    [ 184] m "Ah--"
    [ 185] m 1n "Yeah, that's wonderful!"
    [ 186] m "It wouldn't be the same without you, Natsuki."
    [ 187] pass
    [ 188] m 5 "Anyway, [player]..."
    [ 189] m "What do you want to do today?"
    [ 190] m "I was thinking we could--"
    [ 191] show monika at t31 zorder 2
    [ 192] show yuri at f32 zorder 3
    [ 193] y 1l "We already have plans today."
    [ 194] show yuri at t32 zorder 2
    [ 195] show monika at f31 zorder 3
    [ 196] m 1r "Ah..."
    [ 197] m "Is that so, Yuri?"
    [ 198] show monika at t31 zorder 2
    [ 199] show yuri at f32 zorder 3
    [ 200] y 1y6 "That's correct."
    [ 201] y "[player] is already engaged in a novel that we're reading together."
    [ 202] y 1y5 "Aren't you glad I've already gotten him into literature, Monika?"
    [ 203] show yuri 1a at t32 zorder 2
    [ 204] show monika at f31 zorder 3
    [ 205] m 2l "I..."
    [ 206] m "I suppose..."
    [ 207] m "I was just--"
    [ 208] m 1r "Actually, it doesn't matter."
    [ 209] m 1i "It really doesn't."
    [ 210] m "You guys can do whatever you want."
    [ 211] show monika at t31 zorder 2
    [ 212] show yuri at hf32 zorder 3
    [ 213] y 2y1 "<i>(Yes!)</i>{w=0.5}{nw}"
    [ 214] y 2u "Um... Thank you for understanding, Monika."
    [ 215] unless poemwinner[2] == "natsuki" goto [219]
    [ 216] 
    [ 217] 
    [ 218] goto [219]
    [ 219] pass
    [ 220] scene bg club_day2
    [ 221] show yuri 3 at t11 zorder 2
    [ 222] with wipeleft_scene
    [ 223] call yuri_exclusive2_2_ch22
    [ 224] return
