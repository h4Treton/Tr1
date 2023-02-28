class Category:

    categories = []

    @classmethod
    def add(cls, category_name: str):
        if category_name not in cls.categories:
            cls.categories.append(category_name)
            return len(cls.categories) - 1
        else:
            raise ValueError

    @classmethod
    def get(cls, index: int):
        if index < len(cls.categories):
            return cls.categories[index]
        else:
            raise IndexError

    @classmethod
    def delete(cls, index: int):
        if index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index: int, new_category_name: str):
        if index >= len(cls.categories):
            if new_category_name not in cls.categories:
                cls.categories.append(new_category_name)
            else:
                raise ValueError
        else:
            cls.categories[index] = new_category_name


print(Category.categories)
Category.add('Кот')
Category.add('Пес')
Category.add('Тюлень')
print(Category.categories)
#Category.add('Кот')
print(Category.get(0))
print(Category.get(1))
Category.delete(1)
print(Category.categories)
Category.add('Слон')
print(Category.categories)
Category.update(2, 'Слониха')
print(Category.categories)
Category.update(5, 'Голубь')
print(Category.categories)
