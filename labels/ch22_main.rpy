label ch22_main:
    [   0] scene bg club_day2
    [   1] with dissolve_scene_half
    [   2] play music "t6"
    [   3] dc "Don't Skip Previous Line on AutoSave"    # say, developer commentary
    [   4] 
    [   5] "Another day passes, and it's time for the club meeting already."
    [   6] "I've gotten a little more comfortable here over the past couple days."
    [   7] "Entering the clubroom, the usual scene greets me."
    [   8] unless renpy.random.randint(0,2) == 0 goto [12]
    [   9] show yuri half at i11 zorder 2
    [  10] show yuri_half2 at i11 zorder 1
    [  11] goto [13]
    [  12] show yuri 1s at t11 zorder 2
    [  13] pass
    [  14] y "Welcome back, [player]..."
    [  15] hide yuri_half2
    [  16] mc "Ah, hi Yuri..."
    [  17] "I'm not sure if it's me, or if it's Yuri's expression..."
    [  18] "But the weight of yesterday's quarrel still hangs in the air a little."
    [  19] y 2v "U-Um..."
    [  20] "Yuri glances over her shoulder, looking around the room."
    [  21] "Natsuki is reading manga at a desk."
    [  22] "And surprisingly, Monika isn't here yet."
    [  23] "Suddenly, Yuri takes my arm and pulls me to the corner of the room."
    [  24] show bg closet
    [  25] show yuri 2t at t11 zorder 2
    [  26] with wipeleft
    [  27] y "About yesterday..."
    [  28] y "I..."
    [  29] y 2v "I really need to apologize."
    [  30] y "Nothing like that has ever happened before..."
    [  31] y 2t "And...something just came over me, I guess..."
    [  32] y "I wasn't acting mentally sound."
    [  33] y 2w "Please don't think we're usually like this!"
    [  34] y "Not just me, but Natsuki as well..."
    [  35] show yuri 2t
    [  36] mc "Yuri..."
    [  37] mc "I'm happy that you were considerate and apologized."
    [  38] mc "You don't have to worry too much."
    [  39] mc "Even though I've only been here a couple days, I could tell something was off yesterday..."
    [  40] mc "Maybe we were just a little extra sensitive because it was our first time sharing poems."
    [  41] mc "But whatever it was..."
    [  42] mc "It didn't make me think any less of you."
    [  43] mc "I had already decided that there's no way you can be a bad person."
    [  44] mc "And now that you're apologizing, I know you really didn't mean it."
    [  45] y 3t "A-Ah..."
    [  46] y "[player]..."
    [  47] y 3u "Don't say those kinds of things so frankly..."
    [  48] y "They make me a little too happy."
    [  49] y 1s "I'm really glad that you're such an understanding person..."
    [  50] y "And I'm really glad that you joined this club."
    [  51] y "Everything is a little bit brighter with you around, and--"
    [  52] y 1t "Ah--"
    [  53] y 4c "Sorry, what am I saying right now...?"
    [  54] y "I just--"
    [  55] show natsuki 2c at f33 zorder 3
    [  56] n "Hey, have you guys seen Monika?"
    [  57] show natsuki at t33 zorder 2
    [  58] show yuri 3n at h32
    [  59] y "Ah--!"
    [  60] mc "No, I haven't..."
    [  61] mc "I was also kind of wondering where she was."
    [  62] show natsuki at f33 zorder 3
    [  63] n 5g "Man..."
    [  64] n 5c "Yuri, I'm guessing you haven't, either?"
    [  65] show natsuki at t33 zorder 2
    [  66] show yuri at f32 zorder 3
    [  67] y 4a "..."
    [  68] "Yuri is clearly taken aback by how calmly Natsuki is addressing her."
    [  69] y "N-No, I haven't..."
    [  70] show yuri at t32 zorder 2
    [  71] show natsuki at f33 zorder 3
    [  72] n 1u "Jeez, this isn't like her at all."
    [  73] n "I know it's stupid, but I can't help but worry a little bit..."
    [  74] show natsuki at t33 zorder 2
    [  75] show yuri at f32 zorder 3
    [  76] y 2t "..."
    [  77] show yuri at t32 zorder 2
    [  78] show natsuki 1h at f33 zorder 3
    [  79] n "What?"
    [  80] n "Why're you looking at me like that?"
    [  81] show natsuki at t33 zorder 2
    [  82] show yuri at f32 zorder 3
    [  83] y "U-Um..."
    [  84] y "Natsuki, about yesterday..."
    [  85] y 3w "I-I just wanted to apologize!"
    [  86] y "I promise I didn't mean any of the things I said!"
    [  87] y 3t "And I'll do my best to stay under control from now on..."
    [  88] y "So--"
    [  89] show yuri at t32 zorder 2
    [  90] show natsuki at f33 zorder 3
    [  91] n 2c "Yuri, what the heck are you talking about?"
    [  92] n "Did you do something yesterday?"
    [  93] show natsuki at t33 zorder 2
    [  94] show yuri at f32 zorder 3
    [  95] y 3f "...Eh?"
    [  96] show yuri at t32 zorder 2
    [  97] show natsuki at f33 zorder 3
    [  98] 
    [  99] n 2a "Jeez..."
    [ 100] 
    [ 101] n "Whatever's on your mind, I'm sure it was nothing."
    [ 102] n "I don't even remember anything bad happening."
    [ 103] n "You're the kind of person who worries too much about the little things, aren't you?"
    [ 104] 
    [ 105] show natsuki at t33 zorder 2
    [ 106] show yuri at f32 zorder 3
    [ 107] y 2o "..."
    [ 108] y "B-But..."
    [ 109] show yuri at t32 zorder 2
    [ 110] unless renpy.random.randint(0, 3) == 0 goto [122]
    [ 111] 
    [ 112] show natsuki 0 at i33 zorder 3
    [ 113] show n_rects_mouth as nm1 at t_natsuki_ch22_eye_1 zorder 4
    [ 114] show n_rects_mouth as nm2 at t_natsuki_ch22_eye_2 zorder 4
    [ 115] show n_moving_mouth at 75bbcd9b3f5c0d641878247b5a4f1685 zorder 4
    [ 116] n 2a "mibulls sailcloth blindsight lifeline anan rectipetality faultlessly offered scleromalacia neighed catholicate"
    [ 117] hide nm1
    [ 118] hide nm2
    [ 119] hide n_moving_mouth
    [ 120] 
    [ 121] goto [122]
    [ 122] pass
    [ 123] show natsuki at f33 zorder 3
    [ 124] n 2j "I'll accept your apology anyway, if it helps you feel better about it."
    [ 125] n "Besides, it's kinda nice to hear, since I was always afraid you secretly hated me or something like that."
    [ 126] n 2z "Ehehe."
    [ 127] show natsuki at t33 zorder 2
    [ 128] show yuri at f32 zorder 3
    [ 129] y 3q "N-No, not at all...!"
    [ 130] y "I don't hate you..."
    [ 131] show yuri at t32 zorder 2
    [ 132] show natsuki at f33 zorder 3
    [ 133] n 2l "Ahaha."
    [ 134] n "Well, you're kind of weird, but I don't hate you either."
    [ 135] show natsuki at t33 zorder 2
    [ 136] show yuri at f32 zorder 3
    [ 137] y 3t "..."
    [ 138] "Natsuki turns to me."
    [ 139] show yuri at t32 zorder 2
    [ 140] show natsuki at f33 zorder 3
    [ 141] n 2a "You're still on trial, though."
    [ 142] show natsuki at t33 zorder 2
    [ 143] mc "Hey...!"
    [ 144] "Suddenly, the door swings open."
    [ 145] show monika 1g at l41
    [ 146] m "Sorry! I'm super sorry!"
    [ 147] mc "Ah, there you are..."
    [ 148] show monika at f41 zorder 3
    [ 149] m "I didn't mean to be late..."
    [ 150] m "I hope you guys weren't worried or anything!"
    [ 151] show monika at t41 zorder 2
    [ 152] mc "Nah..."
    [ 153] mc "Well, Natsuki was."
    [ 154] show natsuki at f33 zorder 3
    [ 155] n 1p "I-I was not!!"
    [ 156] show natsuki at t33 zorder 2
    [ 157] show monika at f41 zorder 3
    [ 158] m 1k "Ahaha."
    [ 159] show monika at t41 zorder 2
    [ 160] show natsuki at f33 zorder 3
    [ 161] n 1s "...What took you so long, anyway?"
    [ 162] show natsuki at t33 zorder 2
    [ 163] show monika at f41 zorder 3
    [ 164] m 1e "Ah..."
    [ 165] m "Well, my last period today was study hall."
    [ 166] m "To be honest, I kind of just lost track of time..."
    [ 167] m "Ahaha..."
    [ 168] show monika at t41 zorder 2
    [ 169] show natsuki at f33 zorder 3
    [ 170] n 2c "That makes no sense, though."
    [ 171] n "You would have heard the bell ring, at least."
    [ 172] show natsuki at t33 zorder 2
    [ 173] show monika at f41 zorder 3
    [ 174] m 1m "I must not have heard it, since I was practicing piano..."
    [ 175] show monika at t41 zorder 2
    [ 176] show yuri at f32 zorder 3
    [ 177] y 1e "Piano...?"
    [ 178] y "I wasn't aware you played music as well, Monika."
    [ 179] show yuri at t32 zorder 2
    [ 180] show monika at f41 zorder 3
    [ 181] m 1l "Ah, don't give me more credit than I deserve."
    [ 182] m 1m "I guess I've been practicing for a while, but I'm still not really good yet."
    [ 183] show monika at t41 zorder 2
    [ 184] show yuri at f32 zorder 3
    [ 185] y 1a "Still..."
    [ 186] y "That must require a lot of dedication."
    [ 187] y "So, I'm still impressed."
    [ 188] show yuri at t32 zorder 2
    [ 189] show monika at f41 zorder 3
    [ 190] m 5 "Aw, well thanks, Yuri~"
    [ 191] show monika at t41 zorder 2
    [ 192] show natsuki at f33 zorder 3
    [ 193] n 2d "You should play something for us sometime!"
    [ 194] show natsuki at t33 zorder 2
    [ 195] show monika at f41 zorder 3
    [ 196] m "Ahaha, that's..."
    [ 197] "Monika looks at me."
    [ 198] m 1a "Well, I am working on writing a song, but it's not quite done yet..."
    [ 199] m "Maybe once I get a little bit better, I will."
    [ 200] show monika at t41 zorder 2
    [ 201] mc "That sounds cool."
    [ 202] mc "I look forward to it."
    [ 203] show monika at f41 zorder 3
    [ 204] m 1b "Is that so?"
    [ 205] m "In that case..."
    [ 206] m "I won't let you down, [player]."
    [ 207] show yuri at thide zorder 1
    [ 208] show natsuki at thide zorder 1
    [ 209] hide yuri
    [ 210] hide natsuki
    [ 211] show monika 5 at t11 zorder 2
    [ 212] "Monika smiles sweetly."
    [ 213] mc "Ah..."
    [ 214] mc "I didn't mean any pressure or anything like that!"
    [ 215] m 1a "Ahaha, don't worry."
    [ 216] m "I was hoping that I could share it with you, anyway."
    [ 217] m "I guess that's why I've been practicing so much recently."
    [ 218] mc "I see..."
    [ 219] "I'm not sure if Monika was referring to the whole club, or just me..."
    [ 220] mc "In that case, best of luck."
    [ 221] m 1j "Thanks~!"
    [ 222] m 1a "So, I didn't miss anything, did I?"
    [ 223] mc "Not...not really."
    [ 224] show monika at thide zorder 1
    [ 225] hide monika
    [ 226] "I choose not to bring up anything that the three of us talked about."
    [ 227] "Besides, Natsuki has already run off into the closet."
    [ 228] show yuri 2q at t11 zorder 2
    [ 229] y "[player]..."
    [ 230] y "Um..."
    [ 231] y "Since your compliments put me in a good mood..."
    [ 232] y "I was wondering if you would like to spend some time together today."
    [ 233] y 3o "I mean--in the club!"
    [ 234] unless poemwinner[0] == "natsuki" goto [265]
    [ 235] 
    [ 236] mc "Ah, I suppose so."
    [ 237] mc "I don't think I could say no to you, after you gave that book to me."
    [ 238] mc "Well, I guess I need to make sure Natsuki isn't waiting for me."
    [ 239] mc "After we finished reading yesterday, she--"
    [ 240] unless n_appeal >= 2 goto [258]
    [ 241] y 3r "She's fine!"
    [ 242] 
    [ 243] y 3h "She's reading over there. See?"
    [ 244] 
    [ 245] y 3f "Don't think about her so much."
    [ 246] y "She's used to being ignored."
    [ 247] y "Come on, we're going over there."
    [ 248] 
    [ 249] window hide(None)
    [ 250] 
    [ 251] stop music
    [ 252] scene black
    [ 253] window auto
    [ 254] 
    [ 255] play music "1656cc3febe7ee940a4f60f1554f9341"
    [ 256] jump ch22_main2
    [ 257] goto [263]
    [ 258] y 3r "S-She's fine!"
    [ 259] y 3h "She's reading over there."
    [ 260] y 3y6 "So it's okay, right?"
    [ 261] mc "Ah--"
    [ 262] mc "In that case, I don't see any problem..."
    [ 263] pass
    [ 264] goto [268]
    [ 265] 
    [ 266] mc "Yeah, definitely."
    [ 267] mc "I planned on it anyway."
    [ 268] pass
    [ 269] show yuri at h11 zorder 2
    [ 270] y 3y5 "Okay!"
    [ 271] y "Can we start now?"
    [ 272] y "Let's find a place to sit--"
    [ 273] y 3n "A-Ah--"
    [ 274] y "I'm being a little forceful, aren't I...?"
    [ 275] y 4c "I'm sorry!"
    [ 276] y "My heart...just won't stop pounding, for some reason..."
    [ 277] mc "Don't worry about it."
    [ 278] mc "If anything, it's nice to see you have so much energy."
    [ 279] y 3q "Y-Yeah!"
    [ 280] y "But..."
    [ 281] y 3j "I need to try to calm down."
    [ 282] y "I won't be able to focus on reading like this..."
    [ 283] mc "Take your time."
    [ 284] "Yuri takes a deep breath, then pulls a copy of the book out of her bag."
    [ 285] jump ch22_main2
