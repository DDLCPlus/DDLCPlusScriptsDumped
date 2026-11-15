label poemresponse_start2:
    [   0] 
    [   1] unless persistent.playthrough == 2 goto [4]
    [   2] 
    [   3] goto [5]
    [   4] 
    [   5] pass
    [   6] unless poemsread == 0 goto [9]
    [   7] 
    [   8] goto [10]
    [   9] 
    [  10] pass
    [  11] goto [44]
    [  12] 
    [  13] unless chapter == 1 and poemsread == 0 goto [17]
    [  14] "I'm definitely most comfortable sharing it with Sayori first."
    [  15] "She's my good friend, after all."
    [  16] goto [17]
    [  17] pass
    [  18] call poemresponse_sayori
    [  19] goto [46]
    [  20] 
    [  21] unless chapter == 1 and poemsread == 0 goto [25]
    [  22] "I told Natsuki I was interested in her poems yesterday."
    [  23] "It's probably only fair if I shared mine with her first."
    [  24] goto [25]
    [  25] pass
    [  26] call poemresponse_natsuki
    [  27] goto [46]
    [  28] 
    [  29] unless chapter == 1 and poemsread == 0 goto [33]
    [  30] "Yuri seems the most experienced, so I should start with her."
    [  31] "I can trust her opinion to be fair."
    [  32] goto [33]
    [  33] pass
    [  34] call poemresponse_yuri
    [  35] goto [46]
    [  36] 
    [  37] unless chapter == 1 and poemsread == 0 goto [41]
    [  38] "I should start with Monika."
    [  39] "Yesterday she seemed eager to read my poem, and I want her to know I'm putting in effort."
    [  40] goto [41]
    [  41] pass
    [  42] call poemresponse_monika
    [  43] goto [46]
    [  44] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  45] menu:    # caption above
                "Sayori" if <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[0], constantStrings=["s_readpoem", "persistent", "playthrough"], constantObjects=[] }>:  goto [12]
                "Natsuki" if <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["n_readpoem"], constantObjects=[] }>:  goto [20]
                "Yuri" if <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["y_readpoem", "y_ranaway"], constantObjects=[] }>:  goto [28]
                "Monika" if <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction], constantFloats=[], constantStrings=["m_readpoem"], constantObjects=[] }>:  goto [36]
    [  46] pass
    [  47] 
    [  48] unless poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4) goto [51]
    [  49] jump poemresponse_loop
    [  50] goto [51]
    [  51] pass
    [  52] jump poemresponse_end
