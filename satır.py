def satir_okuma():
    dosya = open("seminer.txt","r",encoding="utf-8")
    for satir in dosya:
        print(satir)
print(satir_okuma())