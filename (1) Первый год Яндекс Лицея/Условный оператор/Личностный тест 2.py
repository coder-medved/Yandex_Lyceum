print('Привет дорогой друг, пройди тест и узнай кто ты на тему "Жанр игр и Вид переферии".')
print('Какой жанр игр предпочитаете? (Экшн, Инди, Релакс)')
ans1 = input()
if 'Экшн' in ans1 or 'Инди' in ans1 or 'Релакс' in ans1:
    print('Какие девайсы вам нравяться? (RGB, Однотипные, Красочные, Не красивые')
    ans2 = input()
    if 'RGB' in ans2 or 'Однотипные' in ans2 or 'Красочные' in ans2 or 'Не красивые' in ans2:
        if ans1 == 'Экшн' and ans2 == 'RGB':
            print('Вы человек жесть и необращайте даже внимание на вашу красоту :)')
        elif ans1 == 'Экшн' and ans2 == 'Однотипные':
            print('Вы человек скучный и очень злой.')
        elif ans1 == 'Экшн' and ans2 == 'Красочные':
            print('Вы любите красоту и по всей видимости очень жестокий :)')
        elif ans1 == 'Экшн' and ans2 == 'Не красивые':
            print('Вы человек злость и вам всё равно на вашу переферию.')
        elif ans1 == 'Инди' and ans2 == 'RGB':
            print('Вы умный человек и любите подсветку :)')
        elif ans1 == 'Инди' and ans2 == 'Однотипные':
            print('Вы умный человек, но вы со всем скучный :(')
        elif ans1 == 'Инди' and ans2 == 'Красочные':
            print('Вы умный человек и очень ухаживаете за красотой вашего раб. места')
        elif ans1 == 'Инди' and ans2 == 'Не красивые':
            print('Вы умный человек, но по всей видимости всё равно на красоту переферии')
        elif ans1 == 'Релакс' and ans2 == 'RGB':
            print('Вы человек релакс, ваш жизнь состоит из спокойствия.')
        elif ans1 == 'Релакс' and ans2 == 'Однотипные':
            print('Вы человек спокойствие, но видимо скучный.')
        elif ans1 == 'Релакс' and ans2 == 'Красочные':
            print('Вы человек спокойствие и вы очень любите красоту вашего раб. места')
        elif ans1 == 'Релакс' and ans2 == 'Не красивые':
            print('Вы человек спокойствие, но вы со всем не следите за красотой')
    else:
        print('Некорректный ввод, пожалуйста выбирайте ответ который указан и вводите\
 ответ с большой буквы.')
else:
    print('Некорректный ввод, пожалуйста выбирайте ответ который указан и вводите\
 ответ с большой буквы.')