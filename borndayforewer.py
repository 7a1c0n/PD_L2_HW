while 'user isn''t right':
    year = int(input('В каком году родился А.С.Пушкин?: '))
    if year == 1799:
        break
    else:
        print('Неверный год рождения')

while 'user isn''t right':
    day = input('В какой день родился А.С.Пушкин? (ответ в формате DD.MM): ')
    if day == '26.05':
        print('Верно (по старому стилю - юлианскому календарю)')
        break
    elif day == '06.06':
        print('Верно (по новому стилю - григорианскому календарю)')
        break
    else:
        print('Неверный день рождения')
