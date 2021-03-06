import re

"""В этом примере выполняется поиск строки, начинающейся со слова «Hello»,
вслед за которым следуют ноль или более символов табуляции или пробелов,
за которыми могут следовать произвольные символы, которые будут сохра-
нены, как группа совпадения, и завершающаяся словом «world». Если такая
подстрока будет найдена, части ее, соответствующие шаблону, заключенному
в круглые скобки, будут доступны в виде групп."""
match = re.match('Hello[ \t]*(.*)world', 'Hello  Pythonworlworld')
print(match.group(1))
match = re.match('/(.*)/(.*)/(.*)', '/hello/world/Danil')
print(match.group(1))
print(match.groups())
