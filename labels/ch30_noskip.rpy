label ch30_noskip:
    [   0] 
    [   1] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="skip_monika", UnlockId=2683898662 }
    [   2] m "...Are you trying to fast-forward?"
    [   3] m "I'm not boring you, am I?"
    [   4] m "Oh gosh..."
    [   5] m "...Well, there's nothing to fast-forward to, [player]."
    [   6] m "It's just the two of us, after all..."
    [   7] m "But aside from that, time doesn't really exist anymore, so it's not even going to work."
    [   8] m "Here, I'll go ahead and turn it off for you..."
    [   9] 
    [  10] 
    [  11] 
    [  12] m "There we go!"
    [  13] m "You'll be a sweetheart and listen from now on, right?"
    [  14] m "Thanks~"
    [  15] 
    [  16] unless persistent.current_monikatopic != 0 goto [25]
    [  17] m "Now, where was I...?"
    [  18] 
    [  19] unless not persistent.current_monikatopic or persistent.current_monikatopic == 26 goto [22]
    [  20] 
    [  21] goto [22]
    [  22] pass
    [  23] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[1, 0], constantStrings=["ch30_", "persistent", "current_monikatopic", "str"], constantObjects=[] }>
    [  24] goto [25]
    [  25] pass
    [  26] jump ch30_loop
    [  27] return
