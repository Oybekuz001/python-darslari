son=-942
if son<0:
#    print("Manfiy son")
#else :
#    print("Musbat son")


#yosh=int(input("Yoshingiz nechida ? "))
#if yosh<4:
#     narh = 0
#elif yosh<12:
#    narh = 5000
#elif yosh<18:
#    narh = 8000
#else:
#    narh = 10000
#    
#    print(f"Sizga kirish {narh} so'm")

#kun= input("Ertaga nima kun ? ")
#harorat= float(input("Havo harorati qanday ? "))

#if kun.lower()=='shanba' or kun.lower()=='yakshanba' and harorat>30:
#    print("Cho'milgani kettik !")
#elif kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat<30:
#    print("Uyda dam olamiz !")


#son=float(input('Juft son kiriting : '))
#if  son%2:
#    print("Bu son juft emas")
#else:
#    print("Rahmat")


    

#yosh=int(input("Yoshingiz nechida ? "))
#
#if yosh<=4 or yosh>=60:
#    narh=0;
#elif yosh <18:
#    narh=10000; 
#else :
#  
#    narh=20000
#print(f"Chipta {narh} so'm ")



#son=("Ikkita son kiriting")
#x=float(input("Birinchi sonni kiriting:"))
#y=float(input("Ikkinchi sonni kiriting:"))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")
    

    
#mahsulotlar=["Yog' , un , shakar , piyoz , kofe , kartoshka , shokalad , non , go'sht , mevalar"]

#bor_mahsulotlar=[]
#mavjud_emas=[]
#
#for n in range(5):
#    savat.append(input(f"Savatga {n+1} mahsulotni qo'shing :"))
#    
#    
#for mahsulot in savat :
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
        
#        mavjud_emas.append(mahsulot)
#    if mavjud_emas:
#        print("Do'konimizda quyidagi mahsulotlar yo'q:")
#        for mahsulotlar in mavjud_emas:
#            print(mahsulot)
 #       else:
#          print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
        



#butun_son=int(input("Butun son kiriting : "))
#
#for n in range(2,11):
#    if not (butun_son%n):
#        print(f"{butun_son} soni {n} ga qoldiqsiz bo'linadi.")



        
        
        
        
#son=float(input("Juft sonni kiriting : "))
#if son%2==0:
#    print("Rahmat")
#else:
#    print("Bu son juft emas")
    


#yosh=int(input("Yoshingiz nechida ? "))
#if yosh<=4 or yosh>=60:
#    narh=0
#elif yosh<18:
#    narh=10000
#else:
#    narh=20000
#    print(f"Chipta {narh} so'm")


        
        
#x=float(input("Birinchi sonni kiriting : "))
#y=float(input("Ikkinchi sonni kiriting : "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f'{x}={y}')
#else:
#    print(f"{x}={y}") 
        
        
        
mahsulotlar=['un',"yog'",'sovun',"tuxum","piyoz","kartoshka","olma","banan","uzum","qovun"]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing : "))
    
if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print("Savatingiz bo'sh")
