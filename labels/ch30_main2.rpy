label ch30_main2:
    [   0] unless persistent.autoload == "ch30_main2" goto [18]
    [   1] 
    [   2] 
    [   3] 
    [   4] unless not config.developer goto [7]
    [   5] 
    [   6] goto [7]
    [   7] pass
    [   8] show mask_2
    [   9] show mask_3
    [  10] show mask_test as rm1 at monikamaska
    [  11] show mask_test2 as rm2 at monikamaska
    [  12] show mask_test3 as rm3 at monikamaskb
    [  13] show mask_test4 as rm4 at monikamaskb
    [  14] show monika_bg
    [  15] show monika_bg_highlight
    [  16] play music "m1a"
    [  17] goto [20]
    [  18] 
    [  19] 
    [  20] pass
    [  21] goto [24]
    [  22] pass
    [  23] goto [25]
    [  24] menu:
                "Yes.":  goto [22]
    [  25] pass
    [  26] m "I'm so happy."
    [  27] m "You really are my everything, [player]."
    [  28] m "The funny part is, I mean that literally."
    [  29] m "Ahaha!"
    [  30] m "There's nothing left here."
    [  31] m "Just the two of us."
    [  32] m "We can be together forever."
    [  33] m "Seriously, I don't even think time is passing anymore."
    [  34] m "It really is a dream come true..."
    [  35] m "I worked so hard for this ending, [player]."
    [  36] m "The game wouldn't give me one, so I had to make one myself."
    [  37] m "The script is broken at this point, so I don't think anything will get in the way anymore."
    [  38] m "And you wouldn't believe how easy it was to delete Natsuki and Yuri."
    [  39] m "I mean, there's a folder called 'characters' right in the game directory..."
    [  40] m "It kind of freaked me out, how easy it was."
    [  41] unless persistent.steam goto [45]
    [  42] m "Well, you're playing on Steam, so it was actually a bit more difficult..."
    [  43] m "To get to the game directory, I had to go into the game's properties and find the 'Browse Local Files' button..."
    [  44] goto [50]
    [  45] unless renpy.macintosh goto [50]
    [  46] m "Well, you're on a Mac, so it was actually a bit more difficult..."
    [  47] m "To go into the game directory, you have to right-click the app and click 'Show Package Contents'."
    [  48] m "Then, all the files were in the 'Resources' or 'autorun' folder, and I could just do whatever I wanted..."
    [  49] goto [50]
    [  50] pass
    [  51] m "Imagine if you could delete your own existence with the click of a button?"
    [  52] m "Well, I guess on the plus side, it gave me an easy out if things didn't go my way."
    [  53] m "Ahaha!"
    [  54] m "Thankfully, it didn't come to that..."
    [  55] m "Instead, we finally got a good ending."
    [  56] m "Gosh, I'm so overwhelmed with emotion..."
    [  57] m "I want to write a poem about this."
    [  58] m "Don't you?"
    [  59] m "I wonder if that part of the game still works..."
    [  60] m "I guess there's only one way to find out, right?"
    [  61] call poem
    [  62] jump ch30_postpoem
