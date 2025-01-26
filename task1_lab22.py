money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
budget = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    month +=1
    if month == 1:
        budget = money_capital + salary - spend
    else:
        budget = budget - spend + salary
        spend *= (increase + 1)
    if budget < spend:
        break
print("Количество месяцев, которое можно протянуть без долгов:", month)
