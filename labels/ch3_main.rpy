label ch3_main:
    [   0] scene bg club_day
    [   1] with dissolve_scene_half
    [   2] play music "t3"
    [   3] show monika 1g at l31
    [   4] dc "Don't Skip Previous Line on AutoSave"    # say, developer commentary
    [   5] 
    [   6] unless poemwinner[0] != poemwinner[1] and poemwinner[1] != poemwinner[2] and poemwinner[2] != poemwinner[0] goto [9]
    [   7] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="poem_each_char", UnlockId=1920005095 }
    [   8] goto [9]
    [   9] pass
    [  10] m "Aw, man..."
    [  11] m "I'm the last one here again!"
    [  12] mc "Don't worry, I just walked in too."
    [  13] show yuri 1f at f32 zorder 3
    [  14] y "Were you practicing piano again?"
    [  15] show yuri at t32 zorder 2
    [  16] show monika at f31 zorder 3
    [  17] m 1l "Yeah..."
    [  18] m "Ahaha..."
    [  19] show monika at t31 zorder 2
    [  20] show yuri at f32 zorder 3
    [  21] y 1m "You must have a lot of determination."
    [  22] y "Starting this club, and now picking up piano..."
    [  23] show yuri 1a at t32 zorder 2
    [  24] show monika at f31 zorder 3
    [  25] m 1a "Well, maybe not determination..."
    [  26] m "But I guess passion."
    [  27] m "Remember that the club wouldn't be here if it wasn't for all of you."
    [  28] m 1b "And I'm super happy that you're all willing to help out for the festival, too!"
    [  29] show natsuki 1z at f33 zorder 3
    [  30] show monika at t31 zorder 2
    [  31] n "Aaah, I can't wait for the festival!"
    [  32] n "It's gonna be great!"
    [  33] show natsuki at t33 zorder 2
    [  34] show monika at f31 zorder 3
    [  35] m 1d "Eh?"
    [  36] m "Weren't you complaining about it just yesterday, Natsuki?"
    [  37] show monika at t31 zorder 2
    [  38] show natsuki 2a at f33 zorder 3
    [  39] n "Well, yeah."
    [  40] n "I'm not talking about <i>our</i> part of the festival."
    [  41] n 4l "But it's a whole day of school where we get to play and eat all kinds of delicious food!"
    [  42] show natsuki at t33 zorder 2
    [  43] mc "You sound a bit like Sayori all of a sudden..."
    [  44] show natsuki at f33 zorder 3
    [  45] n 4a "Monika! Do they usually have fried squid?"
    [  46] show natsuki at t33 zorder 2
    [  47] show monika 2a at f31 zorder 3
    [  48] m "Squid...?"
    [  49] m "That's a pretty specific thing to look forward to..."
    [  50] show monika at t31 zorder 2
    [  51] show natsuki 2k at f33 zorder 3
    [  52] n "Oh, come on."
    [  53] n "Are you saying you don't like squid?"
    [  54] n "You, of all people?"
    [  55] show natsuki at t33 zorder 2
    [  56] show monika 1d at f31 zorder 3
    [  57] m "Eh? I didn't say I don't like it."
    [  58] m "Besides, what do you mean by 'you of all people'?"
    [  59] show monika at t31 zorder 2
    [  60] show natsuki 1d at f33 zorder 3
    [  61] n "Because!"
    [  62] n "It's right in your name!"
    [  63] n 4z "Mon-ika!"
    [  64] show natsuki at t33 zorder 2
    [  65] show monika 5b at f31 zorder 3
    [  66] m "Eh?!"
    [  67] m "That's not how you say my name at all!"
    [  68] m "Also, that joke makes no sense in translation!"
    [  69] show monika at t31 zorder 2
    [  70] show natsuki at f33 zorder 3
    [  71] n 4m "...?"
    [  72] show natsuki at t33 zorder 2
    [  73] show monika 4l at f31 zorder 3
    [  74] m "Ah...never mind!"
    [  75] m "Let's just focus on our own event for now, okay?"
    [  76] show monika at t31 zorder 2
    [  77] show natsuki 2a at f33 zorder 3
    [  78] n "Ehehe."
    [  79] n "Fine, fine."
    [  80] n "Your reactions aren't as fun as Yuri's or Sayori's, anyway."
    [  81] show natsuki at t33 zorder 2
    [  82] show yuri 2h at f32 zorder 3
    [  83] y "Excuse me..."
    [  84] show yuri at t32 zorder 2
    [  85] mc "Where is Sayori, anyway...?"
    [  86] mc "Oh, there you are."
    [  87] hide monika
    [  88] hide yuri
    [  89] hide natsuki
    [  90] with wipeleft
    [  91] "Sayori is sitting at a desk in the corner of the room, looking down at nothing."
    [  92] "I walk over to her."
    [  93] mc "Hey, Sayori."
    [  94] show sayori 1k at t11 zorder 2
    [  95] "I wave my hand in front of her face."
    [  96] s 1n "Eh--?"
    [  97] mc "You're spacing out again."
    [  98] s "A-Ah..."
    [  99] s 4l "Ehehe, sorry..."
    [ 100] s "Don't mind me."
    [ 101] s 4y "You can go talk to everyone else."
    [ 102] mc "Huh..."
    [ 103] mc "Is everything alright?"
    [ 104] s 1h "O-Of course!"
    [ 105] s "Why wouldn't it be?"
    [ 106] mc "It just feels like you're a little off..."
    [ 107] mc "Sorry for assuming things."
    [ 108] s "Jeez, you worry too much about me."
    [ 109] s 4r "I'm fine, see?"
    [ 110] show sayori at h11
    [ 111] "Sayori shows me a big smile."
    [ 112] s 1a "Don't let me distract you from having fun with everyone."
    [ 113] mc "Well...alright."
    [ 114] mc "If you say so."
    [ 115] show sayori at thide zorder 1
    [ 116] hide sayori
    [ 117] "I worriedly glance at Sayori before turning back toward everyone else."
    [ 118] "But the conversation has already dispersed, with everyone back at their usual activities."
    [ 119] "Maybe I should ask Monika if she's noticed anything about Sayori recently..."
    [ 120] "Since they've been preparing for the festival, they must be spending a lot of time together."
    [ 121] "I timidly approach Monika, who is shuffling through some papers at her desk."
    [ 122] show monika 2b at t11 zorder 2
    [ 123] m "[player]! What's up?"
    [ 124] mc "Hey, this might sound a little strange, but..."
    [ 125] mc "Have you noticed anything up with Sayori recently?"
    [ 126] m 1d "Anything up with her...?"
    [ 127] m "In what way do you mean?"
    [ 128] mc "Maybe I'm reading into it a little too much, but she seems a bit downcast today..."
    [ 129] m "Oh? You think so?"
    [ 130] m "I can't say I've noticed anything about her..."
    [ 131] "Monika peers across the room at Sayori, who is idly dragging a rubber eraser up and down her desk."
    [ 132] m "Maybe there is something on her mind..."
    [ 133] m 2a "But I'm surprised I'm not the one asking you, [player]."
    [ 134] m "You certainly know her a lot better than I do."
    [ 135] mc "Yeah, but she's never really like this..."
    [ 136] mc "She's always talked to me about things that bothered her."
    [ 137] mc "But this time, when I asked her, she was really dismissive."
    [ 138] mc "...Sorry, I know it's not your problem!"
    [ 139] mc "I just wanted to ask if you knew anything, so I'll drop it now..."
    [ 140] m 1g "No, no..."
    [ 141] m "It's important to me, too."
    [ 142] m 1e "I mean, I'm also friends with her..."
    [ 143] m "And I also care about the well-being of my club members, you know?"
    [ 144] m 1i "Maybe I'll try talking to her myself..."
    [ 145] mc "Eh? Are you sure about that...?"
    [ 146] mc "She seemed like she wanted to be left alone..."
    [ 147] m "Are you sure?"
    [ 148] m "Maybe she just has a hard time bringing it up with the person of interest..."
    [ 149] mc "Person of interest...?"
    [ 150] mc "What do you mean by that?"
    [ 151] m 2e "I'm saying that maybe the thing on her mind is you, [player]."
    [ 152] mc "Me...?"
    [ 153] mc "How on Earth would you come to that conclusion?"
    [ 154] m 1j "Well..."
    [ 155] m "I probably shouldn't say too much, but..."
    [ 156] m 1a "Sayori talks about you more than anything else, you know?"
    [ 157] mc "Eh...?"
    [ 158] m "She's been so much happier ever since you've joined the club."
    [ 159] m "It's like an extra light was turned on inside of her."
    [ 160] mc "What?"
    [ 161] mc "No way..."
    [ 162] mc "Sayori...is always like that."
    [ 163] mc "She's always been full of sunshine."
    [ 164] mc "It's not any different now than it always has been."
    [ 165] m 5 "Ehehe."
    [ 166] m "You're so funny, [player]."
    [ 167] m "Have you thought that maybe you've always seen her as so cheerful..."
    [ 168] m "...because that's just how she is when she's around you?"
    [ 169] mc "..."
    [ 170] m 1n "Ah...I said too much."
    [ 171] m "I'm sorry...what do I know, anyway?"
    [ 172] m 1a "I didn't mean to jump to conclusions, so you should just forget about what I said."
    [ 173] m "I'll try to talk to her, so try not to think about it for now."
    [ 174] mc "Ah..."
    [ 175] mc "Alright..."
    [ 176] "Monika smiles meaningfully."
    [ 177] "I know she said to forget about it..."
    [ 178] "But I already know that I won't be able to get her words out of my head."
    [ 179] show monika at thide zorder 1
    [ 180] hide monika
    [ 181] "Monika stands up from her desk and walks across the room to where Sayori is sitting."
    [ 182] "I watch her kneel down next to Sayori and gently talk to her."
    [ 183] "But she's keeping her voice so quiet that I can't hear her from here."
    [ 184] "I sigh and sit myself down."
    [ 185] "I know Sayori told me not to worry about her, and to have fun with everyone else..."
    [ 186] "But that's impossible to do when she's behaving like this."
    [ 187] "Exactly how much do I care about her, that I'm letting this weigh me down so much?"
    [ 188] "Now it feels like I'm the one behaving out of the ordinary..."
    [ 189] "But there's nothing I can do besides wait for Monika."
    [ 190] unless n_appeal == 0 and y_appeal == 0 goto [193]
    [ 191] jump ch3_start_none
    [ 192] goto [212]
    [ 193] unless n_appeal > 1 goto [196]
    [ 194] jump ch3_start_natsuki
    [ 195] goto [212]
    [ 196] unless y_appeal > 1 goto [199]
    [ 197] jump ch3_start_yuri
    [ 198] goto [212]
    [ 199] unless poemwinner[1] == "natsuki" goto [202]
    [ 200] jump ch3_start_natsuki
    [ 201] goto [212]
    [ 202] unless poemwinner[1] == "yuri" goto [205]
    [ 203] jump ch3_start_yuri
    [ 204] goto [212]
    [ 205] unless poemwinner[0] == "natsuki" goto [208]
    [ 206] jump ch3_start_natsuki
    [ 207] goto [212]
    [ 208] unless poemwinner[0] == "yuri" goto [211]
    [ 209] jump ch3_start_yuri
    [ 210] goto [212]
    [ 211] jump ch3_start_none
    [ 212] pass
