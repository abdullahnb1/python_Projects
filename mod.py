def mod(a,mod):
    if a>mod: a-=mod;return mod(a-mod,mod)
    else: print(a)