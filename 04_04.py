class Category:

    categories = []

    @classmethod
    def add(cls, category_name: str):
        if category_name not in cls.categories:
            cls.categories.append({'name': category_name, 'is_published': False})
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
                cls.categories.append({'name': new_category_name, 'is_published': False})
            else:
                raise ValueError
        else:
            cls.categories[index]['name'] = new_category_name

    @classmethod
    def make_published(cls, index: int):
        if index < len(cls.categories):
            cls.categories[index]['is_published'] = True
        else:
            raise IndexError

    @classmethod
    def make_unpublished(cls, index: int):
        if index < len(cls.categories):
            cls.categories[index]['is_published'] = False
        else:
            raise IndexError


print(Category.categories)
Category.add('Кот')
Category.add('Пес')
Category.add('Тюлень')
print(Category.categories)
# Category.add('Кот')
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
Category.make_published(1)
Category.make_published(2)
print(Category.categories)
# Category.make_published(4)
Category.make_unpublished(2)
print(Category.categories)
