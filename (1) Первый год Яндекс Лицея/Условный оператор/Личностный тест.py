print('Мечтаете ли вы изучить Python?')
answer1 = input()
print('Мечтаете ли вы изучить C++?')
answer2 = input()
if answer1 == 'Да' and answer2 == 'Да':
    print('Ого, да вы будущий квантовый компьютер!')
elif answer1 == 'Нет' and answer2 == 'Нет':
    print('Да ну тебя, это очень интересно!')
elif answer1 == 'Нет' and answer2 == 'Да':
    print('Вы очень сильный программист.')
elif answer1 == 'Да' and answer2 == 'Нет':
    print('Вы будущий программист сильной среды.')
else:
    print('Ответы должны быть только Да или Нет!')