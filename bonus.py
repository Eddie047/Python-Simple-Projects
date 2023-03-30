def calculating_bonus (salary, years_of_service):
    bonus_rate = 0.05
    if years_of_service > 5:
        bonus_amount = bonus_rate * salary
        return bonus_amount
    else:
        return 0

salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
bonus = calculating_bonus(salary, years_of_service)

if bonus > 0:
    print(f"your bonus amount is sh{bonus}")
else:
    print("you do not qualify for bonus")