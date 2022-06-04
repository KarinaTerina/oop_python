class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units
    def describe_shop(self):
        return f'{self.shop_name}, {self.store_type}.'
    def open_shop(self):
        return 'Онлайн-магазин відкритий!'
    def set_number_of_units(self):
        return f'Кількість видів: {self.number_of_units}.'
    def increment_number_of_units(self, number):
        return self.number_of_units + number

store = Shop('Matadoor','магазин дверей')
print(store.shop_name)
print(store.store_type)
print(store.describe_shop())
print(store.open_shop())
store_window = Shop('Steko','магазин вікон')
print(store_window.describe_shop())
store_market = Shop('Niva','продуктовий магазин')
print(store_market.describe_shop())
store_rozetka = Shop('Rozetka','інтернет-магазин')
print(store_rozetka.describe_shop())
print(store.number_of_units)
store.number_of_units = 1
print(store.number_of_units)
store.number_of_units = 7
print(store.set_number_of_units())
print(store.increment_number_of_units(7))

class Discount(Shop):
    def __init__(self,discount_products):
        self.discount_products = discount_products
    def get_discounts_products(self):
        return f'Товари зі знижкою: {self.discount_products}.'
store_discount = Discount('вікно, електроніка')
print(store_discount.get_discounts_products())