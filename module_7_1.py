class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {product.split(', ')[0] for product in existing_products}

        for product in products:
            if product.name in existing_names:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                with open(self.__file_name, 'a', encoding='utf-8') as file:
                    file.write(str(product) + 'n')


# Пример использования программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Первый запуск
s1.add(p1, p2, p3)
print(s1.get_products())

# Второй запуск
s1.add(p1, p2, p3)
print(s1.get_products())