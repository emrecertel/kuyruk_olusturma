kuyruk=[]
print("Sayı eklemek için: 1")
print("Sayı çıkarmak için: 2")
print("Kuyruğu yazdırmak için: 3")
print("Çıkış için: 4")
print(" ")
secim=int(input("Seçiminizi girin: "))
def sayı_ekleme():
    sayı=int(input("Sayı girin:"))
    kuyruk.append(sayı)
    print(sayı,"KUYRUĞA EKLENDİ...")
def sayı_cıkarma():
    if len(kuyruk)==0:
        print("KUYRUK ZATEN BOŞ...")
    else:
        print(kuyruk.pop(0),"KUYRUKTAN ÇIKARTILDI...")
def yazdırma():
    print(kuyruk)

while secim !=4:
    if secim==1:
        sayı_ekleme()
        print(" ")
        print("Sayı eklemek için: 1")
        print("Sayı çıkarmak için: 2")
        print("Kuyruğu yazdırmak için: 3")
        print("Çıkış için: 4")
        print(" ")
        secim = int(input("Seçiminizi girin: "))
        continue
    elif secim==2:
        sayı_cıkarma()
        print(" ")
        print("Sayı eklemek için: 1")
        print("Sayı çıkarmak için: 2")
        print("Kuyruğu yazdırmak için: 3")
        print("Çıkış için: 4")
        print(" ")
        secim = int(input("Seçiminizi girin: "))
        continue
    elif secim==3:
        yazdırma()
        print(" ")
        print("Sayı eklemek için: 1")
        print("Sayı çıkarmak için: 2")
        print("Kuyruğu yazdırmak için: 3")
        print("Çıkış için: 4")
        print(" ")
        secim = int(input("Seçiminizi girin: "))
        continue
    else:
        print("Yanlış bir değer girdiniz tekrar deneyin")
        print(" ")
        print("Sayı eklemek için: 1")
        print("Sayı çıkarmak için: 2")
        print("Kuyruğu yazdırmak için: 3")
        print("Çıkış için: 4")
        print(" ")
        secim = int(input("Seçiminizi girin: "))
        continue