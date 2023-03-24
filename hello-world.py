#my_cars = cars[:]
#print(my_cars)
#mehmonlar =['ali','vali','toxir','zokir']
#for a in mehmonlar:
 #   print(f"Hurmatli { a } aka sizni 20- kuni toyga taklif qilmiz")
  #  print("Hurmat bilan palonchievlar honadoni\n")
#mashinalar = ( 'bmw', 'audi' , 'volvo', 'tesla')
#for mashin in mashinalar :
 #   print(f"Sizga tavsiya etadigan mashinalarim {mashin}")
  #  print("hurmatli mijoz istaganingizni tanlang\n")
#sonlar = [ 1,2,3,4,5,6,7,8,9]
#for son in sonlar:
 #   print( f"{son} - ning kvadrati {son **2} gaten\n")
#sonlar = list(range(0,20))
#soning_kvadrati = []
#for son in sonlar :
 #   soning_kvadrati.append(son**2)
 #   print(sonlar)
 #   print(soning_kvadrati)
#dostlar = []
#print( "5 ta eng yaqin dostingiz kim ?")
#for n in range(5) :
 #   dostlar.append(input(f"{n+1} - inchi dostingizni ismini yozing : "))
#print(dostlar)
#avtolar = ['audi ', 'bmw' , 'ferrari', 'tesla']
#for avto in avtolar :
 #   print(avto.title())
#print(avtolar)
#for avto in avtolar :
   # if avto == 'bmw' : 
  #   print(avto.upper())
 #   else :
#     print(avto.title())
#ism = input("Ismingiz nima ? \n>>>>>>")
#if ism.lower() != 'ali':
 #else :
    #print("Salom , Ali")
#javob = float(input(f"12*6 nechi ? >>>  "))
#if javob !=72:
 #    print("Noto'g'ri javob ")
#else :
  #  print( "To'g'ri javob ")
#yosh = int(input("yoshingiz nechada ? =="))    
##if yosh >=18 :
 #   print("Xush kelibsiz")
# else:
#    print("Krish mumkin emas")
#login = input("Yangi logen kriting : ")
#if len(login)<= 5 :
 #   print("Xato , logen 5 ta dan ko'p son bo'lishim kerak")
#yil = int( input("Tug'ulgan yilingizni kriting ? "))
#if 2022-yil <=18:
  #  print("Sizga kirish mumkin emas")
 #   print(f"Yoshingiz {2022-yil} da , siz 18 yoshdan kchiksiz ")
#else :
   # print("Hush kelibsiz ")
#yil = int(input("Tug'ulgan yilingiz ? >>>"))
#if yil-2022 >= 40 : print("Sizning yoshingiz juda katta !")
#else: print(" Sizning yoshingiz tog'ri keladi")
#x,y = 70 ,50
#print("y<x") if x>y  else print("y>x")
#yosh = int(input("Yoshingiz nechada ? \n>>>>"))
#if yosh <= 4:
 #   print("Sizga kirish bepul !")
#elif yosh <= 12 :
#    print("Sizga kirish '5000 so'm' .")
#else :
#    print("Sizga kirish '10000 so'm '")
#Bugungi_kun = input("Bugungi kun ?  \n>>>>")
#if Bugungi_kun.lower() == "shanba" or Bugungi_kun.lower() =="yakshanba" :
   #print("Bugun dam olish kuni ")
#else:
    #print("Bugun iw kuni")
#kun = input("Bugungi hafta kuni ? \n>>>>")
#harorat = float(input("bugungi harorat ? \n >>>>"))
#if( kun.lower()=='yakshanba' or kun.lower()== 'shanba' )  and harorat >= 40 :
#    print("Kettik basseynga ")
#elif (kun.lower()=='yakshanba' or kun.lower() == 'shanba') and harorat < 40:
#   print('Uyda "Play Station " oynaymiz ')
#narh = 10000 # mijoz olgan taom narxi 
#salat = True # mijoz salat  olganligi uchun true 
#choy = True # mijoz choy olmaganligi uchun false
#if choy and salat :
 #   narh = narh+ 10000
#elif choy or salat:
#    narh =narh+ 5000
#print(f"Jami {narh} ming bo'ldi ")
#menu = ['osh', 'somsa' , 'shashlik', "lag'mon"]
#ovqat = input("Nima taom buyurasiz ? \n>>>>>")
#if ovqat.lower() in menu :
 #   print("Siz tanlagan taom bor")
#else :
 #   print("Siz tanlagan taom afsuski yo'q ")
#menu = ['somsa', 'shashlik', 'lavash', 'gril', 'pizza']
#buyurtma =['somsa', 'lagmon','pizza']
#if buyurtma :
 # for taom in buyurtma :
  #  if taom in menu :
   #     print(f"Menuda {taom} bor")
    #else:
     #   print(f"Menuda bu {taom} yo'q")
#mevalar = {"olma":5000 ,"shaftoli":10000 , "nok": 20000 } #lug'atlar bilan ishlash     
#print(f"Olmani narxi {mevalar['olma']} so'm ")
#print(f"Shaftoli narxi {mevalar['shaftoli']}so'm ")
#print(f"Nok qimmatroq {mevalar['nok']} so'm")
#talaba_0 = {"ism_f":"abbos amandullayev","yosh":21, "t_yil":2001 }
#print(f"Isim sharfi {talaba_0['ism_f'].title()},\
     #yoshi {talaba_0['yosh']} ,\
     #tug'ulgan yili {talaba_0['t_yil]}")
#print(f"Talaba {talaba_1['ism'].title()} hozigi vaqtda {talaba_1['kurs']}")
#get metodi bilan ishlash
#telefonlar ={ 
   #"ali":"galaxy s10+",
   #"vali":"ipxone 14 pro",
  # "g'ani": "nokia lumiya ",
 #  " abbos": "redmi s2"  }
#phone = telefonlar["abbos"]
#print(f"Abbosnin telefoni {telefonlar[" abbos"]}")
           
         #####   14 - Darslik lug'atlar  :
#en_uz = {'apple':'olma', 'banana': 'banan',  'abricos': "o'rik"}
#print(en_uz)
#print(en_uz['banana'])
#meva = {'olma':5000 ,' banan': 20000 , 'shaftoli' : 15000 }
#print(f"Shaftolining narhi {meva['shaftoli']}  so'm. ")
   # lug'atda turli hil o'zgaruvchilarni saqlashimiz mumkin !
#
#talaba = {'ismi' : 'Abbos' , ' t_yil': 2000 , ' yoshi': 22 }
#print(f"Talabaning ismi {talaba['ismi'].title()} ,\
     # tug'ulgan yili {talaba[' t_yil']} ,\
     # yoshi {talaba[' yoshi']})
#talaba_0 = { 
   # 'ism':'abbos',
  #  't_yil':2000 ,
  #  'fakulteti' : "KT",
 #   'kurs': 3 }      
#print(talaba_0.items())
#for key , value in talaba_0.items():
  #  print(f"kalit:{key}")
 #   print(f"qiymat : {value} \n")
#telefonlar={
    #"ali":"iphone",
    #"vali":"samsung",
    #"murod":"redmi",
    #"abbos":"nokia"
   # }
#for keys,value in telefonlar.items():
  #  print(f"{keys.title()} - ning telefoni {value}\n")
#maxsulotlar = {
    #"olma":7000,
    #"o'rik":10000,
   # "shaftoli":20000,
  #  "nok":15000
 #   }
#print("Do'kondagi maxsulotlar :")
#for mahsulot in maxsulotlar.keys():
 #   print(mahsulot.title())
#bozorlik = ['banan', 'olma', 'nok', 'non']   
#for maxsulot in maxsulotlar :
  #  if maxsulot in bozorlik :
 #       print(f"{maxsulot.title()} {maxsulotlar[maxsulot]} so'm .")
#for buyum  in bozorlik :
 #   if buyum not in maxsulotlar :
#        print(f"Iltimos ,do'koningizga {buyum} ham olib keling !")
#print(" Telefon nomlari :")
#for telefon in telefonlar.values():
 #   print(telefon)
#toys = {"ball", "lamp", "phone", "ball"}

#### NESTING ##### 
# Lug'atlar  ro'yhatlar  
#cars_0 = {
    #"model": "nexia 3",
    #"rangi": "qizil",
   # "yili": 2019,
  #  "narxi": 10000
 #   }
#cars_1 = {
   # "model": "lacetti",
   # "rangi": "qora",
   # "yili": 2015,
  #  "narxi": 11000
 #   }
#cars_2 ={
   # "model":"gentra",
  #  "rangi":"oq",
  #  "yili":2020,
 #   "narxi": 14000
#    }
#car = cars_0
#print(f" Nomi {car['model'].title()} ,"
   #   f"{car['rangi']} rang , "
  #    f" Narxi {car['narxi']} $ , "
 #     f" Yili {car['yili']}")

#car = cars_1
#print(f" Nomi {car['model'].title()} ,"
  #    f"{car['rangi']} rang , "
 #     f" Narxi {car['narxi']} $ , "
 #     f" Yili {car['yili']}")

#car = cars_2
#print(f" Nomi {car['model'].title()} ,"
#      f"{car['rangi']} rang , "
#      f" Narxi {car['narxi']} $ , "
#      f" Yili {car['yili']}")
#cars = [cars_0, cars_1, cars_2]
#for car in cars:
   # print(f" Nomi {car['model'].title()} ,"
  #      f"{car['rangi']} rang , "
 #       f" Narxi {car['narxi']} $ , "
#        f" Yili {car['yili']}")
#print(f"{cars[0]['model'].title()} "
#      f"{cars[0]['rangi']}")   
  # FOR SIKLODA IWlash
#malibus = []
#for N in range(10) :
   # new_car={ 
       # "model": "malibu",
      # "rangi": None,
     #   "yili": 2022 ,
    #    "km": None ,
   #     "narxi": None ,
  #      "karobka":"mexanika"}
 #   malibus.append(new_car)

#for malibu in malibus[:3]:
 #   malibu["rangi"]= "qora"
#for malibu in malibus:
 #   print(malibu)    
#for malibu in malibus[3:7]:
 #   malibu['rang']="oq"
#for malibu in malibus [7:]:
 #   malibu ["rang"]= "qizil"
#    malibu['karobka']= 'avtomat'
#for malibu in malibus:
 #   print(malibu)
#for malibu in malibus:
   # if malibu['karobka']=='avtomat':
   #    malibu['narx'] = 35000
  #  else : 
 #       malibu['narx']= 30000
#for malibu in malibus:
#    print(malibu)

  ##### LUG`AT ICHIDA RO`YHAT ####

emodji =" 😱"