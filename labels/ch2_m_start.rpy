label ch2_m_start:
    [   0] m 1b "Hi again, [player]!"
    [   1] unless n_poemearly goto [11]
    [   2] 
    [   3] m "That was kind of silly with Natsuki earlier, wasn't it?"
    [   4] m 1j "I'm glad the two of you have been getting along so well."
    [   5] mc "..."
    [   6] "That's one way of putting it..."
    [   7] m 2a "Anyway, I already read your poem, but you can go ahead and read mine now."
    [   8] m 1a "I like the way this one turned out, so I hope you do too~"
    [   9] return
    [  10] goto [31]
    [  11] m "How's the writing going?"
    [  12] mc "Alright, I guess..."
    [  13] m 2k "I'll take that."
    [  14] m 2b "As long as it's not going bad!"
    [  15] m 2a "I'm happy that you're applying yourself."
    [  16] m "Maybe soon you'll come up with a masterpiece!"
    [  17] mc "Ahaha, I wouldn't count on that..."
    [  18] m 2a "You never know!"
    [  19] m "Want to share what you wrote for today?"
    [  20] mc "Sure... Here you go."
    [  21] "I give my poem to Monika."
    [  22] m "..."
    [  23] m "...Alright!"
    [  24] 
    [  25] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [  26] m 1a "But anyway..."
    [  27] m "You want to read my poem now?"
    [  28] m "I like the way this one turned out, so I hope you do too~"
    [  29] mc "Alright, let's take a look."
    [  30] return
    [  31] pass
