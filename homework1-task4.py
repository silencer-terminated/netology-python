# Проверка вводимых данных на числовые/целочисленные значения, проценты берутся с точностью до десятых

while True:
    
    salary_monthly = input("How much do you earn per month? Please enter a whole number here.\n")

    try:
        salary_monthly = int(salary_monthly)
    except ValueError:
        print ("This is not a valid number, try again!\n")
    else:
        break

while True:
    
    spend_mortgage = input("How much do you spend for mortgage payment, % from salary?\n")

    try:
        spend_mortgage = round(float(spend_mortgage), 2)
    except ValueError:
        print ("This is not a valid number, try again!\n")
    else:
        break

while True:
    
    spend_blackjackandhookers = input("How large are your other expenses, % from salary?\n")

    try:
        spend_blackjackandhookers = round(float(spend_blackjackandhookers), 2)
    except ValueError:
        print ("This is not an valid number, try again!\n")
    else:
        break

while True:
    
    bonus_times = input("How many times does your boss pay you a bonus?\n")

    try:
        bonus_times = int(bonus_times)
    except ValueError:
        print ("This is not a valid number, try again!\n")
    else:
        break

# Проверка, не платят ли отрицательные премии:
if bonus_times < 0:
    print ("Wow-wow, are you sure your bonus is negative? Chack again and restart!")
    raise SystemExit


#Проверка, не превышают ли траты на ипотеку и жизнь 100% от ЗП:
if (spend_mortgage + spend_blackjackandhookers) > 100:
    print ("You have some crazy finances! Please review your input for spending percentage!")
    raise SystemExit

#N.B.! Half of the bouns is always spent for vacation rest


# Расчёт:
leftovers_total = round((12 * salary_monthly)*(1 - (spend_mortgage + spend_blackjackandhookers)/100) + (bonus_times * 0.5 * salary_monthly), 2)
mortgage_wasted = round(12 * salary_monthly * (spend_mortgage/100), 2)

print ("Your yearly retirement savings are:\n", leftovers_total)
print ("Your yearly mortgage spending is:\n", mortgage_wasted)
