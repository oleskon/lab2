salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен
month = 10
mani_nado = 0
money_capital = 0
while month > 0:
    mani_nado = spend - salary
    money_capital += mani_nado
    spend *= increase
    month -= 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
