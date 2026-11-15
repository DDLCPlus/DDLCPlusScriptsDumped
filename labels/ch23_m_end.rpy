label ch23_m_end:
    [   0] 
    [   1] window hide
    [   2] play sound "page_turn"
    [   3] with None
    [   4] show paper_glitch zorder 10
    [   5] with Dissolve(1)
    [   6] play music "g2"
    [   7] unless renpy.windows and renpy.game.preferences.fullscreen goto [12]
    [   8] 
    [   9] scene bsod
    [  10] 
    [  11] goto [14]
    [  12] show black zorder 1
    [  13] 
    [  14] pass
    [  15] window show(None)
    [  16] show monika 1d at i11 zorder 11
    [  17] 
    [  18] 
    [  19] m "Jeez! That really startled me!{fast}"
    [  20] window auto
    [  21] m "Um..."
    [  22] m 1m "Well, I guess I kinda messed up at, uh... 'writing' this poem."
    [  23] m "I was just trying to..."
    [  24] m 1i "...Never mind."
    [  25] m "Let's just move on..."
    [  26] stop music
    [  27] return
