label ch3_m_start:
    [   0] m 2a "Hi [player]~"
    [   1] m "Have you thought about what you want to submit to perform at the festival?"
    [   2] mc "Well..."
    [   3] "Being in this club is one thing, but performing in front of a bunch of people..."
    [   4] mc "...I'll have to give it some more thought."
    [   5] m 2b "Okay, no pressure!"
    [   6] m "But whatever you do, I'm sure it'll turn out great."
    [   7] m "It would also make me happy to see."
    [   8] m 2k "Ahaha!"
    [   9] unless n_poemearly goto [14]
    [  10] 
    [  11] m 1a "Anyway, I already read your poem, but you can go ahead and read mine now."
    [  12] return
    [  13] goto [25]
    [  14] m 1a "Anyway, let's take a look at today's poem!"
    [  15] mc "Sure..."
    [  16] "I let Monika take the poem I'm holding in my hands."
    [  17] m "..."
    [  18] 
    [  19] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["nextscene"], constantObjects=[] }>
    [  20] m 1a "Anyway...!"
    [  21] m "I'll share my poem with you now, alright?"
    [  22] mc "Er..."
    [  23] mc "Alright..."
    [  24] return
    [  25] pass
