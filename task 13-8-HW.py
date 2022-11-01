print('Добро пожаловать на нашу конференцию)')
print('----')
print('''Стоимость посещения конференции
до 18 лет — бесплатно,
от 18 до 25 лет — 990 руб.,
от 25 лет — 1390 руб.
при регистрации более 3 человек скидка 10%''')
print('----')

tickets = int(input('Какое количество билетов вы хотите приобрести: '))
sum_tickets = 0

for number_person in range(tickets):
    age = int(input('Введите возраст участника номер %s: '%(number_person + 1)))
    if age < 18:
        sum_tickets += 0
    elif 18 <= age < 25:
        sum_tickets += 990
    elif age >= 25:
        sum_tickets += 1390

print('---')
if tickets > 3:
    print('Общая стоимость билетов со скидкой 10%: ', int(sum_tickets * 0.9), 'руб.')
else:
    print('Общая стоимость билетов: ', sum_tickets, 'руб.')