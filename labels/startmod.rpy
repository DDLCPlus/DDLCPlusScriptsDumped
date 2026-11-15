label startmod:
    [   0] python:    # runs C# do_custom_dialogue_box
                TK1L2KUEKHQDXW0ATW8FH9RRGVJFBJ
    [   1] $ n_name = "Natsuki the Natsuki"
    [   2] stop music fadeout 2
    [   3] play music "p2"
    [   4] scene bg corridor
    [   5] with dissolve_scene_full
    [   6] "As I make my way through the hall, I can't help but notice some frustrated sighs coming from the clubroom."    # menu-with-caption
    [   7] scene bg club_day
    [   8] show natsuki 3o at t22
    [   9] n "Ugh why won't it work?"
    [  10] hide natsuki
    [  11] scene bg corridor
    [  12] "Through the window of the door I notice natsuki standing next to what looks like some big contraption."    # menu-with-caption
    [  13] "What the hell is that girl up to? First cupcakes and now engineering? Has she lost her mind?"    # menu-with-caption
    [  14] scene bg club_day
    [  15] with dissolve_scene_full
    [  16] mc "Hey Natsuki, what are you doing?"
    [  17] show natsuki 1p at h43
    [  18] n "OH SHIT-"
    [  19] hide natsuki
    [  20] show natsuki 3i at h43
    [  21] n "God.. don't do that dummy, you scared me."
    [  22] n "I'm currently trying to get the cloninator 9000 to work.."
    [  23] mc "Cloninator?"
    [  24] hide natsuki
    [  25] show natsuki 3j at t11
    [  26] n "Yep! Made it myself. Basically, this bad boy takes me and makes another me - I did it for help with like baking and stuff"
    [  27] hide natsuki
    [  28] show natsuki 2q at t11
    [  29] n "Although.. It doesn't seem to be working right now.."
    [  30] mc "I see. Have you tried pushing the on button?"
    [  31] stop music
    [  32] hide natsuki
    [  33] show natsuki 4n at t11
    [  34] "Natsuki stares at me, her eyes widening as the realization set in that she forgot to push the power button."    # menu-with-caption
    [  35] "Natsuki pushes the power button."    # menu-with-caption
    [  36] play music "t2"
    [  37] show clonesuki 1a at f21
    [  38] "And outcomes.... Natsuki"    # menu-with-caption
    [  39] hide natsuki
    [  40] show natsuki 3j at t11
    [  41] n "A-ha! Got it."
    [  42] Natsuki Clone "What is my purpose?"
    [  43] n "You pass Butter"
    [  44] Natsuki Clone "Oh my God."
    [  45] python:    # runs C# fix_menu_stuff
                OCYZRMRI99J25DZBEG5KCQSKFT3KEG
    [  46] jump end_game
    [  47] return
