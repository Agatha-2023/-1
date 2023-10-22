salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
m_count = 1  # Счетчик месяцев
money_capital = 0

while m_count < 11:
    money_capital = money_capital + spend - salary
    spend *= (1 + increase)
    m_count += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
