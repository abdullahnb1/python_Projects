def reduce_number(a):
    toplam = 0
    if a <=9:
        return a
    else: 
        for i in str(a):
            toplam += int(i)
        if toplam <= 9: return toplam
        else: return reduce_number(toplam)