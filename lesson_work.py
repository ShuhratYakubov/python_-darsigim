# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:18:58 2023

@author: Cripton
"""

#ism = int(input( "Tug'ilgan yilingizni kiriting ? \n >>"))
#t_yil = 2023-ism
#print('Sizning yoshingiz ' , t_yil  )
  
# Amaliyot 7- chi dars 

#shahslar_0 = ["sane","mane", "coman"]
#shahslar_1 = ["robben","ribbery","lahm"]
#print( f"men hohlardimki {shahslar_0.pop(0)}  va  {shahslar_1.pop(0)} \
#      birga o'ynashini ")

 # FOR SIKLI BILAN IWLAW

dostlar = []
#print("Eng yaqin do'stlaringizni kiriting .")
#for n in range(5):
#    dostlar.append(input(f" {n+1} - do'stingizni kriting >>"))
#print(dostlar)

######### M; 9.     FOR sikli boycha amaliyot

#ismlar = [ "abbos", "umid", "shox", "iskandar", "murod"]
#for ism in ismlar:
#    print("Assalomu  alaykum {ism} ")
#    print("Xayir {ism}")
#print(f"Kod {len(ismlar)} marotaba takrorlandi ")
 

#  10 dan 100 gacha bo'lgan toq sonlar royxatini tuzing va kubini chiqaring 

#toq_sonlar= range(11,100,2)
#for son in toq_sonlar:
#    print(son **3)

#print('5 t sevimli kino filimingizni kiriting :')
#s_kinolar=[]
#for k in range(5):
#    s_kinolar.append(input(f"{k+1} - kino nominin kiriting  >>"))
#print(s_kinolar)

#n_odamlar= int(input("Bugun nechta odam bilan suhbatlashdingiz ? >>"))
#ismlar=[]
#for n in range(n_odamlar):
#    ismlar.append(input( f"Muloqotda bo`lgan {n+1} - odamingiz "))
#print(ismlar)

############   M:10    
## SHARTLAR  VA TARMOQLANISH 
        #  IF VA ELSE

#avtolar = ["bmw","audi", "pontiac","dodge"]
#for avto in avtolar:
#    if avto == 'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())


#ism= input("ismingiz nima ? >>")
#if ism.lower() !="ali":
#    print(f"Mazur tutasiz {ism.title()} bizga Ali kerak")
#else:
#    print("Salom Ali")


#parol= input("Yangi parol  kriting : ")
#if  len(parol) <=5:
#    print("Parol 5 ta sondan ko`p bo`lishifcgfc kerak")
#else:
#    print("okey")
 
# AMALIYOT;

#yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in yangi_cars:
#    if car == "gm":
#        print( car.upper())
#    else:
#        print(car.title())
 

#yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in yangi_cars:
#    if car != "gm":
#        print( car.title())
#    else:
#        print(car.upper())   

#login= input("Ismingizni kriting >>")
#if login.lower() == "cripton":
#    print("Hush kelibsiz Cripton , foydalanuvchilarni ko`rmoqchimisiz")
#else:
#    print(f"Salom {login.title()} , Hush kelibsiz" )


#x= float(input("Birirnchi sonni kirgazing >>"))
#y= float(input("Ikkinchi sonni kirgazing >>" ))
#if x==y:
#    print(f"Sonlar teng ekan  {x}={y}")


#x= float(input("Istalgan sonni kirgazing >>"))
#print(f"{x} musbat son ") if x>0 else print("{x} manfiy son")


#son = float(input("Istalgan son qiymatini kirgazing \n >>>"))
#if son >= 0:
#    print(f"Sonnin ildizi {son**0.5}")
#else:
#    print("Musbat son kirgazing ")


######## M:11

# or va elif   operatorlari

#kun = input("Bugun qanaqa kun ? \n >>> ")
#if kun.lower()=="yakshanba" or kun.lower()=="shanba":
#    print("Bugun dam olish kuni")
#elif kun.lower()=="dushanba" :
#    print("Bugun juda og`ir kun")
#else:
#    print("Bugun ish kuni")

#kun = input("Bugun qanaqa kun ? \n >>> ")
#harorat= float(input("Bugun havo harorati \n >>>"))

#if kun.lower()=="yakshanba" and harorat >=30:
#    print("BAssenga kettik")
#elif kun.lower()=="yakshanba" and harorat <=30:
#    print("Bugun savuq TV korish vaqti")


#menu = ['osh','lagmon','shashlik','sho\'rva']
#buyurtma = ['osh', 'shashlik','kabob']
#for taom in  buyurtma :
#    if taom in menu :
#        print(f' Buyurtmada {taom}  bor ')
#    else :
#        print(f'Afsuski {taom }  taom yo\'q ')

 ####   AMALIY MASHQLAR
 
# juft son kirgazish uchun so\'ro\'v 
 
#son = int(input( ' Juft sonlarni kiriting \n >>>>>'))
#if son%2 :
#    print("notog\'ri")
#else:
#    print('rahmat')

#yosh = float(input(' Yoshingiz nechada ? \n >>>'))
#if yosh <= 4 or yosh > 60:
#    print('Kirish bepul')
#elif yosh <18 :
#    print(' Kirish  10000 so\'m ' )
#else:
#    print(' Kirish 20000 so\'m ')
 
#x = float(input('Istagan soningizni kiriting \>>'))   
#y = float(input('Istagan soningizni kiriting \>>'))

#if  x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f'{x}>{y}')

#mahsulot =['un', 'go\'sht','yog\'', 'non', 'banan', ' suv', 'kola']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1} ta mahsulot qo\'shing \ >>>"))
#for mahsulotlar in savat:
#    if mahsulotlar in mahsulot:
#        print(f" Do\'konimizda  {mahsulotlar} bor ")
#    else:
#        print(f' Do\'konimizda  {mahsulotlar} yo\'q  ')

#user = ['anvar', 'ali','vali',' asad', 'umid',]
#login = input('Yangi login kriting \n >>>>>')
#if login.lower() in user :
#    print('Yangi login tanlang , bu logen band etilgan')
#else:
#    print(f'Xush kelibsiz  {login.title()} ')
    

#son = int(input("Istalgan butun son kiriting: "))

#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")   



############# M 12
# hatolar bo'yicha ishlash


#print("Lstening of teen")
#for n in range(10):
#    print(n)
#    print(n+1)
 
   


