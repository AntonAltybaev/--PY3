money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

month, current = 0, money_capital - spend + salary
while current >= 0:
    if month != 0:
        spend *= 1 + increase
    current = current - spend + salary
    month += 1

print(month-1)  # 8
