# Ввод с проверкой на целочисленность данных:

while True:
    
    birth_month = int(input("Input your birth month:\n"))

    try:
        birth_month = int(birth_month)
    except ValueError:
        print ("This is not an integer number, try again!\n")
    else:
        break


while True:
    
    birth_day = int(input("Input your birth day:\n"))

    try:
        birth_day = int(birth_day)
    except ValueError:
        print ("This is not an integer number, try again!\n")
    else:
        break

#Анализ и вывод:


print ("Your Zodiak sign is: ")


if ( (birth_month == 3) and 21<=birth_day<=31 ) \
or ( (birth_month == 4) and 1<=birth_day<=19 ):
    print("Aries")
    
elif ( (birth_month == 4) and 20<=birth_day<=31 ) \
or ( (birth_month == 5) and 1<=birth_day<=20 ):
    print("Taurus")
    
elif ( (birth_month == 5) and 21<=birth_day<=31 ) \
or ( (birth_month == 6) and 1<=birth_day<=20 ):
    print("Gemini")
    
elif ( (birth_month == 6) and 21<=birth_day<=31 ) \
or ( (birth_month == 7) and 1<=birth_day<=22 ):
    print("Cancer")
    
elif ( (birth_month == 7) and 23<=birth_day<=31 ) \
or ( (birth_month == 8) and 1<=birth_day<=22 ):
    print("Leo")
    
elif ( (birth_month == 8) and 23<=birth_day<=31 ) \
or ( (birth_month == 9) and 1<=birth_day<=22 ):
    print("Virgo")
    
elif ( (birth_month == 9) and 23<=birth_day<=31 ) \
or ( (birth_month == 10) and 1<=birth_day<=22 ):
    print("Libra")
    
elif ( (birth_month == 10) and 23<=birth_day<=31 ) \
or ( (birth_month == 11) and 1<=birth_day<=21 ):
    print("Scorpio")
    
elif ( (birth_month == 11) and 22<=birth_day<=31 ) \
or ( (birth_month == 12) and 1<=birth_day<=21 ):
    print("Sagittarius")
    
elif ( (birth_month == 12) and 22<=birth_day<=31 ) \
or ( (birth_month == 1) and 1<=birth_day<=19 ):
    print("Capricorn")
    
elif ( (birth_month == 1) and 20<=birth_day<=31 ) \
or ( (birth_month == 2) and 1<=birth_day<=18 ):
    print("Aquarius")
    
elif ( (birth_month == 2) and 19<=birth_day<=29 ) \
or ( (birth_month == 3) and 1<=birth_day<=20 ):
    print("Pisces")
    
else:
    print("\n wait... You are an alien from another planet!!!")
