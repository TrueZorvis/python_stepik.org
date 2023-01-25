lst_in = ['Города=about-cities',
          'Машины=read-of-cars',
          'Самолеты=airplanes']
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
dop = {item.split('=')[0]: item.split('=')[1] for item in lst_in}
menu = dict(**menu, **dop)
print(menu)
