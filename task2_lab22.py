salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
deficit = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for _ in range(months):
    deficit = spend - salary
    if deficit > 0:
        money_capital += deficit
    spend *= increase + 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))


