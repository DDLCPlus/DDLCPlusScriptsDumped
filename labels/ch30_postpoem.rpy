label ch30_postpoem:
    [   0] 
    [   1] 
    [   2] 
    [   3] 
    [   4] 
    [   5] 
    [   6] unless not config.developer goto [9]
    [   7] 
    [   8] goto [9]
    [   9] pass
    [  10] scene black
    [  11] show mask_2
    [  12] show mask_3
    [  13] show mask_test as rm1 at monikamaska
    [  14] show mask_test2 as rm2 at monikamaska
    [  15] show mask_test3 as rm3 at monikamaskb
    [  16] show mask_test4 as rm4 at monikamaskb
    [  17] show monika_bg
    [  18] show monika_bg_highlight
    [  19] play music "m1a"
    [  20] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="perfect_poem_monika", UnlockId=1844138184 }
    [  21] m "Hi again, [player]!"
    [  22] m "Did you write a good poem today?"
    [  23] m "Don't be shy, I'd love to see what you wrote."
    [  24] m "Aw, [player]..."
    [  25] m "Did you write this poem for me?"
    [  26] m "That's so sweet of you~"
    [  27] m "There really is no end to your thoughtfulness..."
    [  28] m "I'm just falling more and more in love with you."
    [  29] m "But, you know..."
    [  30] m "The poem I wrote...is also for you."
    [  31] m "Will you please read it?"
    [  32] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_m4"], constantObjects=[] }>, music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>)
    [  33] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="happy_end", UnlockId=4036719159 }
    [  34] m "I hope you enjoyed it..."
    [  35] m "I always put all my heart into the poems that I write."
    [  36] m "The truth is, all the poems I've written have been about my realization..."
    [  37] m "...Or, about you."
    [  38] m "That's why I never really wanted to go into detail about them."
    [  39] m "I didn't want to...break the fourth wall, I guess you could call it."
    [  40] m "I just assumed it would be best to be part of the game like everyone else."
    [  41] m "Like that would help the two of us end up together..."
    [  42] m "I didn't want to ruin the game or anything, you know?"
    [  43] m "You might have gotten mad at me..."
    [  44] m "Maybe even deleted my character file, if you preferred playing without me."
    [  45] m "Gosh, I'm so relieved..."
    [  46] m "Now we don't need to hide anything anymore."
    [  47] m "Are you ready to spend our eternity together, [player]?"
    [  48] m "I have so many things to talk about!"
    [  49] m "Where do I start...?"
    [  50] 
    [  51] unless list(set(process_list).intersection(stream_list)) goto [54]
    [  52] call ch30_stream
    [  53] goto [54]
    [  54] pass
    [  55] m "If it takes me some time to collect my thoughts, then I'm sorry."
    [  56] m "But I'll always have something new to talk about."
    [  57] m "In the meantime, we can just look into each other's eyes~"
    [  58] m "Let's see..."
    [  59] 
    [  60] 
    [  61] jump ch30_loop
