import oop.paragraph_30.composition.first_example.employee as emp


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for item to', server)


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = emp.Server('Pat')  # Встроить другие объекты
        self.chef = emp.PizzaRobot('Bob')  # Робот по имени Bob
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)  # Активизировать другие объекты
        customer.order(self.server)  # Клиент делает заказ официанту
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':  # программный код самопроверки этого модуля
    scene = PizzaShop()  # Создать составной объект
    scene.order('Homer')  # Имитировать заказ клиента Homer
    print('...')
    scene.order("Shaggy")  # Имитировать заказ клиента Shaggy
