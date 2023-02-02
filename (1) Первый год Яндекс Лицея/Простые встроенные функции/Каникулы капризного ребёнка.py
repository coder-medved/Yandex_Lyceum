town1 = input()
town2 = input()
if town1 != town2 and (town1 == 'Тула' and town2 != 'Пенза' or
                       town2 == 'Пенза' and town1 != 'Тула'):
    print('ДА')
else:
    print('НЕТ')