cities = {'Беларусь': ['Минск', 'Витебск', 'Гомель'],
          'Польша': ['Краков', 'Варшава', 'Познань']}


def get_country(city: str):
    city_keys = list(cities.keys())
    for i in range(len(city_keys)):
        if city in cities.get(city_keys[i]):
            return city_keys[i]
    return 'Не найдено'


print(get_country('Витебск'))
print(get_country('Варшава'))
print(get_country('Новополоцк'))
