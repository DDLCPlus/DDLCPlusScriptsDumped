label ch1_n_bad:
    [   0] n "..."
    [   1] mc "...?"
    [   2] unless persistent.playthrough == 2 and renpy.random.randint(0, 2) == 0 goto [21]
    [   3] 
    [   4] stop music
    [   5] 
    [   6] play sound "df8d78fc7bdb1704fb9fbdcb02627d7d"
    [   7] show n_blackeyes at i11 zorder 3
    [   8] show n_eye at neye1 zorder 3
    [   9] show n_eye as n_eye2 at neye2 zorder 3
    [  10] show blood at neye1_blood zorder 3
    [  11] show blood as blood2 at neye2_blood zorder 3
    [  12] 
    [  13] hide n_blackeyes
    [  14] hide n_eye
    [  15] hide n_eye2
    [  16] hide blood
    [  17] hide blood2
    [  18] stop sound
    [  19] play music "f64d4c7e061af1945ad8da49e8783db8"
    [  20] goto [21]
    [  21] pass
    [  22] n 2b "[player], if you're not going to take this club seriously then go home."
    [  23] mc "W-What??"
    [  24] mc "Harsh..."
    [  25] n 42c "What, you expect me to believe that you actually put effort into this?"
    [  26] n "Do you think I'm stupid?"
    [  27] mc "I'm not a writer!"
    [  28] mc "Maybe it's not very good, but yeah, I did put in effort."
    [  29] mc "We all start somewhere, right?"
    [  30] mc "If you're still proud of the first poem <i>you</i> ever wrote, then I'd like to read it."
    [  31] n 1o "!!"
    [  32] mc "Painful to think about?"
    [  33] n 1r "..."
    [  34] n 5q "Fine."
    [  35] n "Well, sorry."
    [  36] n 5c "You'll get better, anyway."
    [  37] n "I'd tell you what to improve, but you're better off just trying again."
    [  38] mc "Fair enough..."
    [  39] mc "Well, to each their own, I guess."
    [  40] n 5q "Anyway, I guess I gotta share mine now..."
    [  41] n "Knowing you, you'll probably think it's stupid."
    [  42] return
