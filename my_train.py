from random import*
yolcu1 = [] #yolcu bilgileri için liste oluşturuldu
#vagonlar belirlendi
vagon1 = ["vagon1",randint(70,100),randint(1,70)]
vagon2 = ["vagon2",randint(80,100),randint(1,80)]
vagon3 = ["vagon3",randint(90,100),randint(1,100)]
secim1_kisi = int(input("Hoşgeldiniz efendim. Kaç kişisiniz acaba?"))
secim1_vagon = input(
    '''Hangi vagonumuzu tercih edersiniz?
    \nİlk Vagonumuz(1)\nKapasite : {0}\nBoş Koltuk :{1}
    \nİkinci Vagonumuz(2)\nKapasite : {2}\nBoş Koltuk :{3}
    \nÜçüncü Vagonumuz(3)\nKapasite : {4}\nBoş Koltuk :{5}

 '''.format(str(vagon1[1]),str(vagon1[2]),str(vagon2[1]),str(vagon2[2]),str(vagon3[1]),str(vagon3[2])))
if secim1_vagon == "1":  #birinci tren seçildiyse
    secim1_vagon = vagon1
    if (secim1_kisi < secim1_vagon[1] - secim1_vagon[2]) and (secim1_vagon[1]*0.7 > secim1_vagon[2]):
        print("Seçim gerçekleşti.")
        yolcu1.append("Vagon ismi : Vagon1")
        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
        print("".join(yolcu1))
    #farklı seçenekler sunuldu
    if (secim1_kisi > secim1_vagon[1] - secim1_vagon[2]) or (secim1_vagon[1]*0.7 < secim1_vagon[2]):
        secim_tekrar1 = input('''
            \nMalesef bu vagonumuza yolcu alamıyoruz.
            \nDiğer seçeneklerimiz;
            \nİkinci Vagonumuz(2)\nKapasite : {0}\nBoş Koltuk :{1}
            \nÜçüncü Vagonumuz(3)\nKapasite : {2}\nBoş Koltuk :{3}
        '''.format(str(vagon2[1]),str(vagon2[2]),str(vagon3[1]),str(vagon3[2])))
        if secim_tekrar1 == "2": #ikinci tercih olarak 2. vagon geçildiyse
            secim_tekrar1 = vagon2
            if (secim1_kisi < secim_tekrar1[1] - secim_tekrar1[2]) and (secim_tekrar1[1]*0.7 > secim_tekrar1[2]):
                print("Seçim gerçekleşti.")
                yolcu1.append("Vagon ismi : Vagon2")
                yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                print("".join(yolcu1))
            #farklı seçenekler sunuldu
            if (secim1_kisi > secim_tekrar1[1] - secim_tekrar1[2]) or (secim_tekrar1[1]*0.7 < secim_tekrar1[2]):
                secim_tekrar2 = input('''
                    \nMalesef bu vagonumuza yolcu alamıyoruz.
                    \nDiğer seçeneklerimiz;
                    \nÜçüncü Vagonumuz(3)\nKapasite : {0}\nBoş Koltuk :{1}
                '''.format(str(vagon3[1]),str(vagon3[2])))
                if secim_tekrar2 == "3":
                    secim_tekrar2 = vagon3
                    if (secim1_kisi < secim_tekrar2[1] - secim_tekrar2[2]) and (secim_tekrar2[1]*0.7 > secim_tekrar2[2]):
                        print("Seçim gerçekleşti.")
                        yolcu1.append("Vagon ismi : Vagon3")
                        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                        print("".join(yolcu1))
                    if (secim1_kisi > secim_tekrar2[1] - secim_tekrar2[2]) or (secim_tekrar2[1]*0.7 < secim_tekrar2[2]):
                        print("Malesef trenimizin bu seferinde size uygun yer bulunamamıştır.")
        if secim_tekrar1 == "3": #ikinci tercih olarak 3. vagon geçildiyse
            secim_tekrar1 = vagon3
            if (secim1_kisi < secim_tekrar1[1] - secim_tekrar1[2]) and (secim_tekrar1[1]*0.7 > secim_tekrar1[2]):
                print("Seçim gerçekleşti.")
                yolcu1.append("Vagon ismi : Vagon3")
                yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                print("".join(yolcu1))
            if (secim1_kisi > secim_tekrar1[1] - secim_tekrar1[2]) or (secim_tekrar1[1]*0.7 < secim_tekrar1[2]):
                secim_tekrar2 = input('''
                    \nMalesef bu vagonumuza yolcu alamıyoruz.
                    \nDiğer seçeneklerimiz;
                    \nİkinci Vagonumuz(2)\nKapasite : {0}\nBoş Koltuk :{1}
                '''.format(str(vagon2[1]),str(vagon2[2])))
                if secim_tekrar2 == "2":
                    secim_tekrar2 = vagon2
                    if (secim1_kisi < secim_tekrar2[1] - secim_tekrar2[2]) and (secim_tekrar2[1]*0.7 > secim_tekrar2[2]):
                        print("Seçim gerçekleşti.")
                        yolcu1.append("Vagon ismi : Vagon2")
                        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                        print("".join(yolcu1))
                    if (secim1_kisi > secim_tekrar2[1] - secim_tekrar2[2]) or (secim_tekrar2[1]*0.7 < secim_tekrar2[2]):
                        print("Malesef trenimizin bu seferinde size uygun yer bulunamamıştır.")
if secim1_vagon == "2": #ikinci tren seçildiyse
    secim1_vagon = vagon2
    if (secim1_kisi < secim1_vagon[1] - secim1_vagon[2]) and (secim1_vagon[1]*0.7 > secim1_vagon[2]):
        print("Seçim gerçekleşti.")
        yolcu1.append("Vagon ismi : Vagon2")
        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
        print("".join(yolcu1))
    if (secim1_kisi > secim1_vagon[1] - secim1_vagon[2]) or (secim1_vagon[1]*0.7 < secim1_vagon[2]):
        secim_tekrar1 = input('''
            \nMalesef bu vagonumuza yolcu alamıyoruz.
            \nDiğer seçeneklerimiz;
            \nBirinci Vagonumuz(1)\nKapasite : {0}\nBoş Koltuk :{1}
            \nÜçüncü Vagonumuz(3)\nKapasite : {2}\nBoş Koltuk :{3}
        '''.format(str(vagon1[1]),str(vagon1[2]),str(vagon3[1]),str(vagon3[2])))
        if secim_tekrar1 == "1": #ikinci seçim olarak 1. vagon seçildiyse
            secim_tekrar1 = vagon1
            if (secim1_kisi < secim_tekrar1[1] - secim_tekrar1[2]) and (secim_tekrar1[1]*0.7 > secim_tekrar1[2]):
                print("Seçim gerçekleşti.")
                yolcu1.append("Vagon ismi : Vagon1")
                yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                print("".join(yolcu1))
            if (secim1_kisi > secim_tekrar1[1] - secim_tekrar1[2]) or (secim_tekrar1[1]*0.7 < secim_tekrar1[2]):
                secim_tekrar2 = input('''
                    \nMalesef bu vagonumuza yolcu alamıyoruz.
                    \nDiğer seçeneklerimiz;
                    \nÜçüncü Vagonumuz(3)\nKapasite : {0}\nBoş Koltuk :{1}
                '''.format(str(vagon3[1]),str(vagon3[2])))
                if secim_tekrar2 == "3":
                    secim_tekrar2 = vagon3
                    if (secim1_kisi < secim_tekrar2[1] - secim_tekrar2[2]) and (secim_tekrar2[1]*0.7 > secim_tekrar2[2]):
                        print("Seçim gerçekleşti.")
                        yolcu1.append("Vagon ismi : Vagon3")
                        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                        print("".join(yolcu1))
                    if (secim1_kisi > secim_tekrar2[1] - secim_tekrar2[2]) or (secim_tekrar2[1]*0.7 < secim_tekrar2[2]):
                        print("Malesef trenimizin bu seferinde size uygun yer bulunamamıştır.")
        if secim_tekrar1 == "3": #ikinci tercih olarak 3. vagon geçildiyse
            secim_tekrar1 = vagon3
            if (secim1_kisi < secim_tekrar1[1] - secim_tekrar1[2]) and (secim_tekrar1[1]*0.7 > secim_tekrar1[2]):
                print("Seçim gerçekleşti.")
                yolcu1.append("Vagon ismi : Vagon3")
                yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                print("".join(yolcu1))
            if (secim1_kisi > secim_tekrar1[1] - secim_tekrar1[2]) or (secim_tekrar1[1]*0.7 < secim_tekrar1[2]):
                secim_tekrar2 = input('''
                    \nMalesef bu vagonumuza yolcu alamıyoruz.
                    \nDiğer seçeneklerimiz;
                    \nBirinci Vagonumuz(1)\nKapasite : {0}\nBoş Koltuk :{1}
                '''.format(str(vagon1[1]),str(vagon1[2])))
                if secim_tekrar2 == "1":
                    secim_tekrar2 = vagon1
                    if (secim1_kisi < secim_tekrar2[1] - secim_tekrar2[2]) and (secim_tekrar2[1]*0.7 > secim_tekrar2[2]):
                        print("Seçim gerçekleşti.")
                        yolcu1.append("Vagon ismi : Vagon1")
                        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                        print("".join(yolcu1))
                    if (secim1_kisi > secim_tekrar2[1] - secim_tekrar2[2]) or (secim_tekrar2[1]*0.7 < secim_tekrar2[2]):
                        print("Malesef trenimizin bu seferinde size uygun yer bulunamamıştır.")
if secim1_vagon == "3": #üçüncü tren seçildiyse
    secim1_vagon = vagon3
    if (secim1_kisi < secim1_vagon[1] - secim1_vagon[2]) and (secim1_vagon[1]*0.7 > secim1_vagon[2]):
        print("Seçim gerçekleşti.")
        yolcu1.append("Vagon ismi : Vagon3")
        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
        print("".join(yolcu1))
    if (secim1_kisi > secim1_vagon[1] - secim1_vagon[2]) or (secim1_vagon[1]*0.7 < secim1_vagon[2]):
        secim_tekrar1 = input('''
            \nMalesef bu vagonumuza yolcu alamıyoruz.
            \nDiğer seçeneklerimiz;
            \nBirinci Vagonumuz(1)\nKapasite : {0}\nBoş Koltuk :{1}
            \nÜçüncü Vagonumuz(2)\nKapasite : {2}\nBoş Koltuk :{3}
        '''.format(str(vagon1[1]),str(vagon1[2]),str(vagon2[1]),str(vagon2[2])))
        if secim_tekrar1 == "1": #ikinci seçim olarak 1. vagon seçildiyse
            secim_tekrar1 = vagon1
            if (secim1_kisi < secim_tekrar1[1] - secim_tekrar1[2]) and (secim_tekrar1[1]*0.7 > secim_tekrar1[2]):
                print("Seçim gerçekleşti.")
                yolcu1.append("Vagon ismi : Vagon1")
                yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                print("".join(yolcu1))
            if (secim1_kisi > secim_tekrar1[1] - secim_tekrar1[2]) or (secim_tekrar1[1]*0.7 < secim_tekrar1[2]):
                secim_tekrar2 = input('''
                    \nMalesef bu vagonumuza yolcu alamıyoruz.
                    \nDiğer seçeneklerimiz;
                    \nÜçüncü Vagonumuz(2)\nKapasite : {0}\nBoş Koltuk :{1}
                '''.format(str(vagon2[1]),str(vagon2[2])))
                if secim_tekrar2 == "2":
                    secim_tekrar2 = vagon2
                    if (secim1_kisi < secim_tekrar2[1] - secim_tekrar2[2]) and (secim_tekrar2[1]*0.7 > secim_tekrar2[2]):
                        print("Seçim gerçekleşti.")
                        yolcu1.append("Vagon ismi : Vagon2")
                        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                        print("".join(yolcu1))
                    if (secim1_kisi > secim_tekrar2[1] - secim_tekrar2[2]) or (secim_tekrar2[1]*0.7 < secim_tekrar2[2]):
                        print("Malesef trenimizin bu seferinde size uygun yer bulunamamıştır.")
        if secim_tekrar1 == "2": #ikinci tercih olarak 2. vagon geçildiyse
            secim_tekrar1 = vagon2
            if (secim1_kisi < secim_tekrar1[1] - secim_tekrar1[2]) and (secim_tekrar1[1]*0.7 > secim_tekrar1[2]):
                print("Seçim gerçekleşti.")
                yolcu1.append("Vagon ismi : Vagon2")
                yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                print("".join(yolcu1))
            if (secim1_kisi > secim_tekrar1[1] - secim_tekrar1[2]) or (secim_tekrar1[1]*0.7 < secim_tekrar1[2]):
                secim_tekrar2 = input('''
                    \nMalesef bu vagonumuza yolcu alamıyoruz.
                    \nDiğer seçeneklerimiz;
                    \nBirinci Vagonumuz(1)\nKapasite : {0}\nBoş Koltuk :{1}
                '''.format(str(vagon1[1]),str(vagon1[2])))
                if secim_tekrar2 == "1":
                    secim_tekrar2 = vagon1
                    if (secim1_kisi < secim_tekrar2[1] - secim_tekrar2[2]) and (secim_tekrar2[1]*0.7 > secim_tekrar2[2]):
                        print("Seçim gerçekleşti.")
                        yolcu1.append("Vagon ismi : Vagon1")
                        yolcu1.append("\nYolcu sayısı : " +str(secim1_kisi))
                        print("".join(yolcu1))
                    if (secim1_kisi > secim_tekrar2[1] - secim_tekrar2[2]) or (secim_tekrar2[1]*0.7 < secim_tekrar2[2]):
                        print("Malesef trenimizin bu seferinde size uygun yer bulunamamıştır.")

                    