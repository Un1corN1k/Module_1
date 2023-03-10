summa = 25000  #int(input("Введіть суму грошей, яку хочете покласти на депозит\n"))
months = 15  #int(input("На скільки місяців хочете покласти?\n"))
addition = 25000  #int(input("Скільки грошей ви будете додавати кожного місяця?\n"))
percents = 15
tax = 18
war_collect = 1.5
summa_months = 0
summa_total = 0
number_months = 0

print(f"Сума коштів витрачених на депозит терміном {months} місяців, з початковим внеском у розмірі: {summa} UAH "
      f"та щомісячним поповненям в розмірі {addition} UAH, складе: {summa + (addition * (months - 1))} UAH")


clear_percents = percents - ((percents/100) * (tax + war_collect))
for months_i in range(1, months + 1):
    number_months = months_i
    summa_months += summa * (1 + (percents / 100)) ** (1 / (clear_percents / 1))
    summa_total = summa_months * (1 + (percents / 100)) ** (1 / (clear_percents / 1))
    print(f"Сума балансу станом на: {number_months} місяць, становить: {round(summa_total, 2)} UAH")
total_summa_cl = summa_total - (summa + (addition * (months - 1)))


print(f'Сума грошей яку ви отримаєте наприкінці депозиту: {round(summa_total, 2)} UAH')
print(f"Ваш чистий дохід з вирахуванням податків становить: {round(total_summa_cl, 2)} UAH")

