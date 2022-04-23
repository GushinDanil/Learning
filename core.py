import time,random
from make_module.func import new_func
for i in range(5):
 time.sleep(random.randint(1,3))
 print("hello world")
new_func(5)
