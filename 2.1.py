money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 1.05  # Ежемесячный рост цен
month = 0
mani_left = 0
while money_capital > 0:
    mani_left = spend - salary
    money_capital -= mani_left
    spend *= increase
    if money_capital < 0:
        break
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
