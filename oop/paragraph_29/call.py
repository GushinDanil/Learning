"""Метод __call__ вызывается при обращении к экземпляру как к функции. Это
не повторяющееся определение – если метод __call__ присутствует, интерпре-
татор будет вызывать его, когда экземпляр вызывается как функция, переда-
вая ему любые позиционные и именованные аргументы:"""

class Callee:
    def __call__(self, *args, **kwargs):
        print('Called: ', args, kwargs)

C=Callee()
C(1,2,3)
C(1,2,3,x=4,y=5)

"""Суть состоит в том, что классы и экземпляры, имеющие метод __call__, под-
держивают тот же синтаксис и семантику передачи аргументов, что и обычные
функции и методы.
Реализация операции вызова, как в данном примере, позволяет экземплярам
классов имитировать поведение функций, а также сохранять информацию
о состоянии между вызовами (похожий пример мы видели в главе 17, когда ис-
следовали области видимости, но теперь вы больше знаете о перегрузке опера-
торов)"""


"""метод __call__ может оказаться удобнее при взаимодействии с при-
кладными интерфейсами, где ожидается функция, – это позволяет создавать
объекты, совместимые с интерфейсами, ожидающими получить функцию, ко-
торые к тому же способны сохранять информацию о своем состоянии между
вызовами. Фактически этот метод занимает третье место среди наиболее часто
используемых методов перегрузки операторов –
после конструктора __init__
и методов форматирования __str__ и __repr__."""



"""Поскольку метод __call__ позволяет присоединять
информацию о состоянии к вызываемым объектам, этот прием является есте-
ственным для реализации функций, которые должны запоминать и вызывать
другие функции."""