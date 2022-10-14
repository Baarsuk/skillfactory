money = int(input('Введите сумму депозита: '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [int(per_cent.get("ТКБ")*money/100),
           int(per_cent.get("СКБ")*money/100),
           int(per_cent.get("ВТБ")*money/100),
           int(per_cent.get("СБЕР")*money/100)]

maxdeposit = max(deposit)

print('Накопленные средства за год вклада в каждом из банков составит:\n',
      'ТКБ -', deposit[0], '\n',
      'СКБ -', deposit[1], '\n',
      'ВТБ -', deposit[2], '\n',
      'СБЕР -', deposit[3])
print('Максимальная сумма, которую вы можете заработать —', maxdeposit)
