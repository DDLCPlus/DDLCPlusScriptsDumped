label ch3_start_none:
    [   0] unless not renpy.music.get_playing(channel='music') == audio.t3 goto [3]
    [   1] stop music fadeout 1
    [   2] goto [3]
    [   3] pass
    [   4] scene bg club_day
    [   5] with wipeleft_scene
    [   6] "..."
    [   7] unless not renpy.music.get_playing(channel='music') == audio.t3 goto [10]
    [   8] play music "t3"
    [   9] goto [10]
    [  10] pass
    [  11] show monika 4b at t11 zorder 2
    [  12] m "Okay, everyone!"
    [  13] "After some time passes, Monika calls out to the clubroom."
    [  14] m "Why don't we share our poems now?"
    [  15] show monika at thide zorder 1
    [  16] hide monika
    [  17] "Before I know it, everything is back to normal."
    [  18] "Everyone goes to retrieve their poems, and I do the same."
    [  19] "I make eye contact with Monika, and she smiles at me."
    [  20] "I wonder what she was talking about with Sayori..."
    [  21] return
