label ch22_m_start:
    [   0] unless y_appeal < 2 goto [16]
    [   1] m 1b "Hi again, [player]!"
    [   2] m "How's the writing going?"
    [   3] mc "Alright, I guess..."
    [   4] m 2k "I'll take that."
    [   5] m 2b "As long as it's not going bad!"
    [   6] m 2a "I'm happy that you're applying yourself."
    [   7] m "Maybe soon you'll come up with a masterpiece!"
    [   8] mc "Ahaha, I wouldn't count on that..."
    [   9] m 2a "You never know!"
    [  10] m "Want to share what you wrote for today?"
    [  11] mc "Sure... Here you go."
    [  12] "I give my poem to Monika."
    [  13] m "..."
    [  14] m "...Alright!"
    [  15] goto [16]
    [  16] pass
    [  17] 
    [  18] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [  19] m 1a "But anyway..."
    [  20] m "You want to read my poem now?"
    [  21] m "I like the way this one turned out, so I hope you do too~"
    [  22] return
