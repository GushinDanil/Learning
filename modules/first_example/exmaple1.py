from modules.first_example import b #1
from modules.first_example.b import spam #2
from modules.first_example.c import * #3
b.spam() #1
spam() #2
printer()  #3
printer2() #3



