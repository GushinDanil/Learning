'''создание объекта класса( при помощи инструкции class)
создаётся объект класса и присваивается к имени указанному в заголовке инструкции'''


class FirstClass:
    data = 'XXX'

    def setdata(self, val):
        self.data = val

    def display(self):
        print(self.data)


'''создание объектов экземпляров (при вызове объекта класса как функции)'''
first = FirstClass()
second = FirstClass()
first.setdata(123)
FirstClass.setdata(second, 999)  # эквивалентно
'''сначала поиск выполняется в атрибутах экземляра потом в атрибутах класса
поэтому ХХХ мы не увидим в значениях'''
print(first.data)
print(second.data)

first.my_name = 'Danil'  # создание атрибута за пределами инструкции class


class SecondClass(FirstClass):  # наследует setdata,data="XXX" и изменяет display
    def display(self): # переопределение
        print('Current value = %s'%self.data)


obj1 = SecondClass()
obj1.display()


obj2 = SecondClass()
obj2.setdata('obj2')
obj2.display()

