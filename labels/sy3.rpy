label sy3:
    [   0] scene black
    [   1] with None
    [   2] scene bg club_day
    [   3] with Dissolve(2.0)
    [   4] play music "p7b"
    [   5] "For the first time, Sayori is the first to enter the clubroom."
    [   6] "Anxiety courses through her relentlessly. Will Yuri show up today?"
    [   7] "Sitting at a desk, she stamps her feet in an attempt to calm down."
    [   8] show sayori 1p at f11 zorder 3
    [   9] s "Why am I letting this affect me so much?"
    [  10] s 1h "I'm doing everything I can to make Yuri happy..."
    [  11] s 1k "But my best wasn't good enough."
    [  12] s 4p "But it was still my best!"
    [  13] s 1k "But I'm letting everyone down. I'm always just a disappointment."
    [  14] show sayori at thide zorder 1
    [  15] hide sayori
    [  16] "Sayori continues to wrestle with her self-deprecating thoughts. Every tiny noise causes her to lift her head in anticipation of Yuri's arrival."
    [  17] 
    [  18] "..."
    [  19] "Minutes pass, and nobody enters the clubroom."
    [  20] "Not Yuri, or Monika."
    [  21] with None
    [  22] scene bg corridor
    [  23] with dissolve_scene_full
    [  24] show monika 1p at f11 zorder 3
    [  25] m "Gosh, I'm so late..."
    [  26] m "Why did I offer to help those other students with their work?"
    [  27] m 1n "I'm such a pushover sometimes."
    [  28] m "It's going to leave such a bad impression on new club members like Yuri if I'm not the first one there."
    [  29] show monika at thide zorder 1
    [  30] hide monika
    [  31] "Monika rounds the corner, approaching the clubroom."
    [  32] "As she does so..."
    [  33] show monika 2d at f11 zorder 3
    [  34] m "Yuri...?"
    [  35] play music "p4" fadeout 2
    [  36] show monika 2d at f21 zorder 3
    [  37] show yuri 3p at f22 zorder 3
    [  38] y "Ah--"
    [  39] show monika at thide zorder 1
    [  40] hide monika
    [  41] show yuri at thide zorder 1
    [  42] hide yuri
    [  43] "Yuri jumps at the sound of Monika's voice."
    [  44] "She's sitting outside the clubroom, against the wall next to the door."
    [  45] "Embarrassed, she quickly closes the book she was reading and stands up."
    [  46] show monika 1l at f21 zorder 3
    [  47] m "Oh gosh, I'm so sorry I'm late."
    [  48] m 3n "You didn't have to wait outside for me, the door to the clubroom is open."
    [  49] show yuri 3o at f22 zorder 3
    [  50] y "It's not--"
    [  51] show monika 1m at t21 zorder 2
    [  52] "Yuri stammers, unable to explain herself."
    [  53] "She peers inside the clubroom through the window, then looks away."
    [  54] y 3v "Actually..."
    [  55] y "I was just...I was wondering if I could help you today instead!"
    [  56] m 2d "Huh? Me?"
    [  57] m "With club publicity stuff?"
    [  58] y "Yes!"
    [  59] show yuri at thide zorder 1
    [  60] hide yuri
    [  61] show monika at thide zorder 1
    [  62] hide monika
    [  63] "Monika is utterly confused."
    [  64] "Why is Yuri asking this, all of a sudden, when she was so eager to spend time with Sayori before?"
    [  65] "Did they not get along after all...?"
    [  66] "Monika looks into the clubroom herself to see Sayori sitting alone inside."
    [  67] show monika 2j at f21 zorder 3
    [  68] m "...Okay."
    [  69] m 2a "It's kind of a simple job, but I'd be happy for you to tag along."
    [  70] show yuri 3q at f22 zorder 3
    [  71] y "Me too."
    [  72] "Monika is worried, but she finds it difficult to insert herself into whatever conflict that may have arisen."
    [  73] "It's a little ironic, she realizes, that she could be so conflict-avoidant after having been in the Debate Club."
    [  74] m 2b "Okay, let's take a walk together."
    [  75] m "I just have to make copies of this new flier, then go around to the billboards and replace the old ones with the new ones."
    [  76] show monika at thide zorder 1
    [  77] hide monika
    [  78] show yuri at thide zorder 1
    [  79] hide yuri
    [  80] "Yuri nods, and the two set off."
    [  81] unless persistent.content_warnings_enabled == True goto [84]
    [  82] 
    [  83] goto [84]
    [  84] pass
    [  85] with None
    [  86] scene bg corridor
    [  87] with wipeleft_scene
    [  88] "The two walk in silence."
    [  89] "Without Sayori, Monika finds it quite difficult to strike up conversation."
    [  90] show monika 2j at f21 zorder 3
    [  91] m "So..."
    [  92] m "How's everything been going?"
    [  93] show yuri 1j at f22 zorder 3
    [  94] y "Fine."
    [  95] m 2b "That's good!"
    [  96] "Neither of them follow up with anything more."
    [  97] show monika 2m at t21 zorder 2
    [  98] "Monika tenses up at the stinted conversation."
    [  99] "How the heck does Sayori do it?"
    [ 100] m 2e "Ah...sorry I didn't see you yesterday, I went straight to the computer lab to work on the fliers."
    [ 101] y 1h "Mhm, Sayori told me."
    [ 102] m 2a "What did you two end up doing yesterday?"
    [ 103] y 1h "Just some reading."
    [ 104] m 2k "Oh, I'm glad! It's really starting to feel more like a literature club now."
    [ 105] m 1a "Yeah..."
    [ 106] m "It's kind of funny, I felt so intimidated at first when I heard about the kind of reading you were into."
    [ 107] m 3e "But you know, it's kind of stupid of me, because I'm just intimidated by things I'm not good at."
    [ 108] m "And it's silly to assume that everyone who comes to the club will just have the same interests as me."
    [ 109] m 2b "But it's so cool that you were able to get Sayori into it. It's like the club is working. I'm really happy about that."
    [ 110] y 3l "She's...not into it."
    [ 111] m 2d "Huh?"
    [ 112] y 3h "She's not into it. And I'm stupid for forcing it onto her."
    [ 113] "Yuri falls silent again, as if she started her thought but can't figure out how to continue it."
    [ 114] play music "p7b" fadeout 2
    [ 115] m 1g "Did something happen...?"
    [ 116] show yuri 3l at t22 zorder 2
    [ 117] "Yuri sighs."
    [ 118] y "No. It's just me."
    [ 119] y 3h "I just--"
    [ 120] "Yuri pauses."
    [ 121] m 1c "Hm?"
    [ 122] y 3v "I'm thinking."
    [ 123] 
    [ 124] "A moment passes in silence, then Yuri shakes her head."
    [ 125] y 3w "I shouldn't be complaining to you all of a sudden."
    [ 126] m 2d "Don't be silly, I won't think you're complaining."
    [ 127] m 2a "I just want to make sure you feel welcome."
    [ 128] m "If it's important to that, then you can tell me anything."
    [ 129] y 3t "Well-- I do feel welcome!"
    [ 130] y 4b "...Too welcome, I guess."
    [ 131] y "It's not an issue with the club. It's just an issue with me."
    [ 132] y "So I feel wrong to inconvenience you with it."
    [ 133] m 1g "Ah..."
    [ 134] "Monika pauses and thinks."
    [ 135] 
    [ 136] m 1d "Well... What if we put it this way?"
    [ 137] m 3a "It's my job as President to understand the needs of the club members, right?"
    [ 138] m "We're going to have all kinds of people joining this club...hopefully, anyway."
    [ 139] m "And learning about the diverse needs and interests of everyone will help me come up with club activities that everyone can be happy with."
    [ 140] y 4a "That everyone can be happy with?"
    [ 141] y "Not just...only some people?"
    [ 142] m 2j "Of course!"
    [ 143] m 2a "I need to be looking out for everyone. Otherwise, what kind of club would it be?"
    [ 144] y 3v "I see..."
    [ 145] "Yuri looks a little more relaxed."
    [ 146] "It signals to Monika that switching from a sympathetic approach to a pragmatic one was a good choice."
    [ 147] "Each individual truly does have their own needs."
    [ 148] y 3l "...Okay."
    [ 149] "Yuri takes a deep breath."
    [ 150] 
    [ 151] y 3h "I'm...a really weird and awkward person. I've accepted that about myself."
    [ 152] y "I just don't know how to...I guess connect with other people."
    [ 153] y 3t "How is it so easy for everyone else? How do you just...make conversation about any arbitrary topic?"
    [ 154] y 3v "I can talk for hours about the things that I'm into. Unfortunately, so much that I don't know when to stop."
    [ 155] y "But for anything else...I just have no idea what to say."
    [ 156] y "So...I understand that about myself. I'm just not good with people. I can't help it."
    [ 157] y "So it feels like whenever I'm confronted with a new social situation, I'm either ignored, or made fun of...or taken pity on."
    [ 158] y 3h "And...Sayori falls into that third category."
    [ 159] m 2i "She...what? Hold on, you're saying that Sayori is taking pity on you?"
    [ 160] "Yuri nods."
    [ 161] y 4b "I just want to be treated like a normal person!"
    [ 162] y "If you don't like me or you don't connect with my interests, then just tell me. I can accept that and move on."
    [ 163] y 3w "Sayori is...too nice to me."
    [ 164] y "I'm so stupid for not realizing that she would just go along with whatever I pushed onto her."
    [ 165] y 4c "Nobody deserves to put themselves through that kind of discomfort, just because...because they pity some weirdo who doesn't know how to make friends."
    [ 166] y "It's...the worst feeling. I hate it."
    [ 167] show monika at thide zorder 1
    [ 168] hide monika
    [ 169] show yuri at thide zorder 1
    [ 170] hide yuri
    [ 171] "Yuri's sharp words cut through the tense air."
    [ 172] "Somewhere in the middle of the conversation, the two stopped short in the hallway, prioritizing the conversation over their original task."
    [ 173] "Monika looks at Yuri. Yuri only looks down, with her fists clenched."
    [ 174] show monika 1i at f21 zorder 3
    [ 175] m "I think...I think you should tell her that."
    [ 176] show yuri 3o at f22 zorder 3
    [ 177] y "I could never say that to someone's face! It's pathetic."
    [ 178] m 2g "Sayori is different!"
    [ 179] m "Making people happy is the most important thing to her."
    [ 180] m 2e "I'm sure that's all she's trying to do."
    [ 181] m "So...if you're able to explain to her what makes you happy, then she'll do anything to make it happen."
    [ 182] y 3w "That's the problem!"
    [ 183] y 3h "What kind of friendship has one person always trying to cater to the other person's weird needs?"
    [ 184] m 1f "..."
    [ 185] y 4c "I'm sorry. I'm making myself sound so--"
    [ 186] m 2r "No...I think I'm starting to understand."
    [ 187] show monika at thide zorder 1
    [ 188] hide monika
    [ 189] show yuri at thide zorder 1
    [ 190] hide yuri
    [ 191] "Monika hesitates to finish her thought out loud."
    [ 192] "It's something that Sayori would be able to say better."
    [ 193] "Sayori is someone who will give anyone however much kindness they need in order to smile."
    [ 194] "But Yuri--who has difficulty accepting kindness--must be driving Sayori to be even more assertive in her kindness, further exacerbating the matter."
    [ 195] "Neither person is to blame, but it's an issue that can't be resolved without them understanding each other better."
    [ 196] show monika 2a at f21 zorder 3
    [ 197] m "Sayori wants to be your friend. I promise that."
    [ 198] m "It's okay for different people to have different needs."
    [ 199] m 4a "I mean, Sayori... She has her own needs, too."
    [ 200] m "But good friends work together and can be what they need for each other."
    [ 201] m 2a "You just have to have good communication and talk about it."
    [ 202] show yuri 1a at f22 zorder 3
    [ 203] y 3t "I don't have good communication--"
    [ 204] "Yuri stops and shakes her head."
    [ 205] y 3w "I'm sorry. I didn't mean to say that."
    [ 206] y "My head is just-- It's so resistant to everything."
    [ 207] y 3h "I'm...I'm pushing such a kind person away from me because of it."
    [ 208] "Yuri pauses to think."
    [ 209] 
    [ 210] y "...I'm so tired of this cycle I'm creating for myself."
    [ 211] y "I think I'm so afraid of people pushing me away that I just push them away first."
    [ 212] y 3w "How thoughtless and immature of me."
    [ 213] "Yuri takes a deep breath and exhales."
    [ 214] y 3v "I didn't mean for this to turn into a whole venting session."
    [ 215] y "But I understand now that I just need to communicate with her."
    [ 216] m 2j "Ahaha. You're totally fine."
    [ 217] m 2a "It's for the club, remember? You're just helping make the club a better place for everyone."
    [ 218] y 4b "...Yeah."
    [ 219] "Yuri falls silent again. She looks like she wants to say something."
    [ 220] 
    [ 221] y "This... This kind of critical thinking is something that I'm really bad at."
    [ 222] y "You know...about people."
    [ 223] y "So...thank you."
    [ 224] m 2j "Anytime."
    [ 225] show monika 2a at t21 zorder 2
    [ 226] "Monika smiles at Yuri."
    [ 227] show yuri 2s at t22 zorder 2
    [ 228] "For just a moment, Yuri finds it in herself to meet Monika's gaze, returning a shy smile of her own."
    [ 229] stop music fadeout 2
    [ 230] with None
    [ 231] scene black
    [ 232] with Dissolve(2)
    [ 233] jump sy4
