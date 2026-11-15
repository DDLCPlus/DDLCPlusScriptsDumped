label credits2:
    [   0] unless persistent.clearall goto [4]
    [   1] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="dan_message", UnlockId=2651756116 }
    [   2] show poem_end_clearall
    [   3] goto [6]
    [   4] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="final_message", UnlockId=1002469327 }
    [   5] show poem_end
    [   6] pass
    [   7] jump postcredits_loop
