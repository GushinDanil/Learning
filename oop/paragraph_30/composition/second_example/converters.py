import oop.paragraph_30.composition.second_example.streams as stream
import sys

class UpperCase(stream.Processor):
    def converter(self, data: str):
        return data.upper()

class HTMLize:
    def write(self,row:str):
        print('<h1>%s</h1>'%(row.rstrip()))

if __name__ == '__main__':
    '''Для обработки потоков различных видов достаточно передать конструктору
    класса объекты требуемых типов.'''
    obj = UpperCase(open('spam.txt'), sys.stdout)
    obj2 = UpperCase(open('spam.txt'), open('spamin.txt'))
    obj.process()
    UpperCase(open('spam.txt'), HTMLize()).process()

'''Если проследить порядок выполнения этого примера, можно заметить, что
было получено два варианта преобразований – приведение символов к верхне-
му регистру (наследованием) и преобразование в формат HTML (композицией),
хотя основная логика обработки в оригинальном суперклассе Processor ничего
не знает ни об одном из них. Программному коду, выполняющему обработку,
нужны только метод write – в классах, выполняющих запись, и метод convert.
Его совершенно не интересует, что делают эти методы. Такой полиморфизм
и инкапсуляция логики составляют основу такой мощи классов.
В этом примере суперкласс Processor реализует только цикл сканирования
файла. Для выполнения более существенных действий его можно было бы рас-
ширить, чтобы обеспечить поддержку дополнительных инструментов в его
подклассах и постепенно превратить все это в полноценный фреймворк. Соз-
дав такой инструмент один раз, вы сможете многократно использовать его во
всех своих программах. Даже в этом простом примере благодаря тому, что с по-
мощью классов можно упаковать и унаследовать так много, все, что нам при-
шлось сделать, – это реализовать этап преобразования в формат HTML, а все
остальное у нас уже и так имелось.'''