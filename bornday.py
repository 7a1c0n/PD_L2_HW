year = int(input('В каком году родился А.С.Пушкин?: '))
if year == 1799:
    day = input('В какой день родился А.С.Пушкин? (ответ в формате DD.MM): ')
    if day == '26.05':
        print('Верно (по старому стилю - юлианскому календарю)')
    elif day == '06.06':
        print('Верно (по новому стилю - григорианскому календарю)')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
