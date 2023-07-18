def soldan_saga(s1,s2):
    if s1 == s2:
        return True
    else:
        for i in range(len(s1)):
            s1= s1[1:]+s1[0]
            if s1 == s2:
                return True
            else: continue
def sagdan_sola(s1,s2):
    if s1 == s2:
        return True
    else:
        for i in range(len(s1)):
            s1= s1[-1]+s1[len(s1)-1]
            if s1 == s2:
                return True
            else: continue
def check_cyclic_shift(s1_s2):
    if sagdan_sola(s1,s2) and soldan_saga(s1,s2):
        return True
    else: return False