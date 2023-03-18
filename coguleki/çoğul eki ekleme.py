kelime=input("Lütfen kelimeyi giriniz.\n")
while True:
    if kelime[-1]  in ["a" , "ı" ,"o", "u"]:
        print("sözcüğünüzün çoğul eki almış hali: {}lar".format(kelime))
    elif kelime[-2]  in ["a" , "ı" ,"o", "u"]:
        print("sözcüğünüzün çoğul eki almış hali: {}lar".format(kelime))
    elif kelime[-3]  in ["a" , "ı" ,"o", "u"]:
        print("sözcüğünüzün çoğul eki almış hali: {}lar".format(kelime))

    elif kelime[-1]  in ["e" , "i" ,"ö", "ü"]:
        print("sözcüğünüzün çoğul eki almış hali: {}ler".format(kelime))
    elif kelime[-2]  in ["e" , "i" ,"ö", "ü"]:
        print("sözcüğünüzün çoğul eki almış hali: {}ler".format(kelime))
    elif kelime[-3]  in ["e" , "i" ,"ö", "ü"]:
     print("sözcüğünüzün çoğul eki almış hali: {}ler".format(kelime))
    else:
        print("Lütfen doğru bir sözcük girin!")