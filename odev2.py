#1- bir aracın yakıt tipine göre(benzin,dizel, lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulama yapınız.
benzin=39.45
dizel= 41.71
lpg= 20.28
yakit_tipi=input("yakıt tipinizi giriniz")
alinan_yol= int(input("aldığınız yolu giriniz"))
if(yakit_tipi=="benzin"):
    print(alinan_yol*benzin)
elif(yakit_tipi=="dizel"):
    print(alinan_yol*dizel)
elif(yakit_tipi=="lpg"):
    print(alinan_yol*lpg)
else:
    print("hata oluştu")

#2-bir öğrencinin 2 vize 1 final notunu alarak ortalam hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.

vize1= int(input("1. vize notunuzu giriniz"))
vize2= int(input("2. vize notunuzu giriniz" ))
final= int(input("final notunuzu giriniz"))
ortalama= (vize1+vize2+final)/3
if(90<=ortalama<=100):
    print("AA")
elif(80<=ortalama<=89):
    print("BA")
elif(70<=ortalama<=79):
    print("BB")
elif(60<=ortalama<=69):
    print("CB")
elif(50<=ortalama<=59):
    print("CC")
elif(40<=ortalama<=49):
    print("DC")


    




