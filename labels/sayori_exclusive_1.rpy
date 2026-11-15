label sayori_exclusive_1:
    [   0] scene bg club_day
    [   1] with wipeleft_scene
    [   2] unless not renpy.music.get_playing(channel='music') == audio.t2 goto [5]
    [   3] play music "t2" fadeout 1
    [   4] goto [5]
    [   5] pass
    [   6] "Man..."
    [   7] "It looks like no one wants to be bothered today."
    [   8] "I slump down into the nearest desk."
    [   9] "How am I supposed to occupy myself with something literature-related by myself like this?"
    [  10] "I guess I could always read some of the book Yuri gave me..."
    [  11] "...But I'm feeling a little too tired to read."
    [  12] "I could probably fall asleep right now."
    [  13] "I close my eyes and end up listening in on Sayori's conversation with Monika."
    [  14] show sayori 1g at t21 zorder 2
    [  15] s "We're probably gonna seem really lame compared to all the other clubs, though..."
    [  16] show monika 2r at f22 zorder 3
    [  17] m "Hmm..."
    [  18] m 2b "Well, we can't give up."
    [  19] m "The festival is our chance to show everyone what literature is all about!"
    [  20] m 2d "The problem is that the idea of a literature club sounds too dense and intellectual..."
    [  21] m "But it's not like that at all, you know?"
    [  22] m 2a "We just need a way of showing that to everyone..."
    [  23] m "Something that speaks to their creative minds."
    [  24] show monika at t22 zorder 2
    [  25] show sayori at f21 zorder 3
    [  26] s 1i "Mmmmmmmmmmm....."
    [  27] s "That doesn't solve the problem, though!"
    [  28] show sayori at t21 zorder 2
    [  29] show monika at f22 zorder 3
    [  30] m 2d "Eh? What do you mean?"
    [  31] show monika at t22 zorder 2
    [  32] show sayori at f21 zorder 3
    [  33] s 1c "Even if we come up with the most fun thing ever..."
    [  34] s "Nobody will come in the first place if it's a literature event."
    [  35] s "So it's more important to figure out how to get people to show up in the first place, you know?"
    [  36] s 1a "And after they come, we can do the thing to speak to their creative minds."
    [  37] "...What's this?"
    [  38] "Sayori is taking this really seriously."
    [  39] "It's rare to hear her deliberating like this."
    [  40] show sayori at t21 zorder 2
    [  41] show monika at f22 zorder 3
    [  42] m 2a "Huh, that's a good point..."
    [  43] m "In that case, do you think food will do the trick?"
    [  44] show monika at t22 zorder 2
    [  45] show sayori at f21 zorder 3
    [  46] s 1n "W-What kind?!"
    [  47] show sayori at t21 zorder 2
    [  48] show monika at f22 zorder 3
    [  49] m 2b "Ah... Well, I guess we could--"
    [  50] show monika at t22 zorder 2
    [  51] show sayori 4r at f21 zorder 3
    [  52] s "Cupcakes!"
    [  53] show sayori at t21 zorder 2
    [  54] show monika 1k at f22 zorder 3
    [  55] m "Ahaha. Good thinking."
    [  56] m 1a "Natsuki would love to do that."
    [  57] show monika at t22 zorder 2
    [  58] show sayori at f21 zorder 3
    [  59] s 4x "Ah! You're right!"
    [  60] s "Natsuki makes the best cupcakes!"
    [  61] s "That works out perfectly~"
    [  62] show sayori at t21 zorder 2
    [  63] show monika at f22 zorder 3
    [  64] m 1d "That wasn't why you suggested it...?"
    [  65] show monika at t22 zorder 2
    [  66] show sayori at f21 zorder 3
    [  67] s 4q "Cupcakes speak to my creative tummy~"
    [  68] show sayori at t21 zorder 2
    [  69] show monika at f22 zorder 3
    [  70] m 1l "..."
    [  71] m "Cupcakes it is, then."
    [  72] show monika at t22 zorder 2
    [  73] show sayori at f21 zorder 3
    [  74] s 1g "I'm hungry..."
    [  75] show sayori at t21 zorder 2
    [  76] show monika at f22 zorder 3
    [  77] m 1a "Anyway, we still need to work out the details of the event itself..."
    [  78] scene black
    [  79] with close_eyes
    [  80] "I find myself smiling."
    [  81] "In the end, Sayori is still her usual self."
    [  82] "But therein lies the unexpected reason I admire her."
    [  83] "Unlike me, who has trouble finding any motivation at all..."
    [  84] "Sayori can put her mind to things and make them come to life."
    [  85] "I suppose that's why I end up letting her get on my case about things."
    [  86] "I can't help but wonder what it would be like to see the world through her eyes..."
    [  87] scene bg club_day
    [  88] show sayori 1b at face
    [  89] with open_eyes
    [  90] mc "Uwaa--!"
    [  91] "I open my eyes to find Sayori's face filling my vision."
    [  92] "I nearly fall out of my chair."
    [  93] show sayori at t11 zorder 2
    [  94] s 4q "Ehehe, sorry~"
    [  95] s 4i "Wait!"
    [  96] s 1j "Actually, I'm not sorry at all!"
    [  97] s "It's your fault for sleeping like that!"
    [  98] s "This isn't the napping club!"
    [  99] mc "Does our school have a napping club...?"
    [ 100] s 1h "You're staying up late again, aren't you?"
    [ 101] s "Now that you're in a club, you're gonna have less time for anime, you know!"
    [ 102] s "You'll need to get used to it!"
    [ 103] mc "Don't say that so loud...!"
    [ 104] "I glance over my shoulder to see if Monika overheard."
    [ 105] s 1g "It's true, though..."
    [ 106] mc "Yeah..."
    [ 107] mc "I know, I know."
    [ 108] mc "You're always looking out for me, Sayori."
    [ 109] s 4q "Ehehe~"
    [ 110] s "It's what I do best!"
    [ 111] mc "...That's a problem!"
    [ 112] mc "What about you?"
    [ 113] mc "You look out for me better than you look out for yourself."
    [ 114] mc "You're still oversleeping every day, aren't you?"
    [ 115] s 1l "Eh?"
    [ 116] s "N-Not every day!"
    [ 117] mc "That's not very convincing..."
    [ 118] mc "How many days this past week have you gotten up on time?"
    [ 119] s 1m "That's..."
    [ 120] s 1o "...It's a secret!"
    [ 121] mc "I knew it..."
    [ 122] s 5a "C'monnnn!"
    [ 123] s "At least give me the benefit of the doubt..."
    [ 124] mc "I can't even do that."
    [ 125] mc "Look, Sayori, it's written all over you."
    [ 126] s 1b "Eh...?"
    [ 127] "Sayori glances around at herself."
    [ 128] s "How is it written all over me?"
    [ 129] mc "You were clearly in a rush this morning..."
    [ 130] mc "Look, your hair is sticking out all around here."
    [ 131] show sayori at h11
    [ 132] s 1e "Ah--"
    [ 133] "I run my fingertips down the side of Sayori's hair, trying to straighten it out."
    [ 134] mc "Man, you really need a brush for this..."
    [ 135] s 1y "My hair is just really hard to get right..."
    [ 136] mc "I won't fall for that."
    [ 137] mc "There's more than just your hair."
    [ 138] mc "Look, your bow isn't straight, either."
    [ 139] mc "And there's a toothpaste stain on your collar right here."
    [ 140] "I try to wipe off the stain with my finger."
    [ 141] show sayori at s11
    [ 142] s "B-But nobody would ever notice that..."
    [ 143] mc "Of course they would."
    [ 144] mc "Nobody's gonna tell you about it because they don't want to embarrass you."
    [ 145] mc "Fortunately, I really don't care about that."
    [ 146] s 5c "Hey, you meanie..."
    [ 147] mc "And you don't even keep your blazer buttoned up."
    [ 148] mc "Seriously, Sayori..."
    [ 149] mc "Why do you think you don't have a boyfriend yet?"
    [ 150] show sayori 1h at t11 zorder 2
    [ 151] s "Eh??"
    [ 152] s "That's <i>super</i> mean!"
    [ 153] mc "Sorry, but you'll thank me later..."
    [ 154] "I start to button her blazer from the bottom."
    [ 155] mc "Once you see how much better it looks, you'll change your mind."
    [ 156] 
    [ 157] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="sayori_exclusive1", UnlockId=1148486650 }
    [ 158] 
    [ 159] scene s_cg1
    [ 160] with dissolve_cg
    [ 161] s "Ehehe~"
    [ 162] s "This is so funny."
    [ 163] mc "What is?"
    [ 164] s "Well..."
    [ 165] s "I was just thinking how weird it is to have a friend who does these kinds of things."
    [ 166] mc "Eh?"
    [ 167] mc "D-Don't say that!"
    [ 168] mc "You'll make <i>me</i> feel weird about it, stupid..."
    [ 169] s "It's okay, though."
    [ 170] s "I'm happy we're like this."
    [ 171] s "Aren't you?"
    [ 172] mc "Ah--"
    [ 173] mc "I-I guess..."
    [ 174] s "Hey, be careful..."
    [ 175] s "The button might come off!"
    [ 176] mc "Why is this one so hard to close...?"
    [ 177] "I struggle to fully close the button near her chest."
    [ 178] mc "Does this thing even fit you properly?"
    [ 179] s "Ehehe~"
    [ 180] s "It did when I bought it."
    [ 181] mc "Sigh..."
    [ 182] mc "If you ever buttoned it, you would have noticed sooner that it doesn't fit you anymore."
    [ 183] mc "What are you smiling about?"
    [ 184] s "It means my boobs got bigger again!"
    [ 185] mc "D-Don't say that out loud!!"
    [ 186] s "Ehehe~"
    [ 187] mc "Anyway..."
    [ 188] mc "You look much better now, so..."
    [ 189] mc "Ah..."
    [ 190] "...Why does it feel strange to see Sayori's blazer buttoned up like that?"
    [ 191] s "But it's so stuffy..."
    [ 192] s "Uuu..."
    [ 193] s "It's not worth it at all!"
    [ 194] "Sayori hastily unbuttons her blazer once more."
    [ 195] scene bg club_day
    [ 196] show sayori 1q at i11 zorder 2
    [ 197] with dissolve_cg
    [ 198] s "Phew!"
    [ 199] s "That's so much better~"
    [ 200] "Sayori puts her arms out and twirls around."
    [ 201] s 1a "So if I keep it unbuttoned then I won't get a boyfriend, right?"
    [ 202] mc "What kind of logic is that?"
    [ 203] mc "And why are you saying that like it's a good thing?"
    [ 204] s "Because..."
    [ 205] s 4h "...If I had a boyfriend, then he wouldn't even let you do things like this!"
    [ 206] s 4y "And you take care of me better than anyone else would, anyway..."
    [ 207] s "So that's why I'm keeping it unbuttoned!"
    [ 208] mc "Stop saying all these embarrassing things!"
    [ 209] s 1b "Eh?"
    [ 210] s "I didn't say anything embarrassing..."
    [ 211] mc "Jeez..."
    [ 212] mc "Well anyway, just focus on trying to wake up a little earlier..."
    [ 213] s 1j "Only if you focus on going to bed earlier!"
    [ 214] mc "Fine, fine..."
    [ 215] mc "It's a deal."
    [ 216] s 4q "Ehehe~"
    [ 217] s 4x "I guess we really are better at taking care of each other than we are at taking care of ourselves."
    [ 218] mc "Yeah, I guess so, huh..."
    [ 219] s 4y "So maybe you should come wake me up in the morning!"
    [ 220] mc "You're doing it again, Sayori..."
    [ 221] s 1h "Aw, but I was joking that time!"
    [ 222] mc "Man, it's impossible to tell with you sometimes."
    [ 223] show monika 3b at l31 behind sayori
    [ 224] m "Okay, everyone!"
    [ 225] mc "Eh?"
    [ 226] "Monika suddenly calls out."
    [ 227] m "Why don't we share the poems we wrote now?"
    [ 228] show sayori 4r at h11
    [ 229] s "Yay~!"
    [ 230] s 4x "[player], I can't wait to read yours!"
    [ 231] mc "Yeah, same..."
    [ 232] "I fail to sound enthusiastic, but Sayori still trots away to retrieve her poem."
    [ 233] show sayori at thide behind monika
    [ 234] return
