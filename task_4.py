class Customer:

    def __init__(self, name: str):
        self.name = name
        self.__discount = 10

    def set_discount(self, new_value: int):
        if new_value > 80:
            self.__discount = 80
        return self.__discount

    def get_price(self, price: int) -> float:
        new_price = original_price - round((price / 100 * self.__discount), 2)
        return new_price


customer = Customer('Иван Иванович')

original_price = 85

print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)

customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
