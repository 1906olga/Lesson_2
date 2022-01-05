# импортируем builtins module

import builtins

# выводит список который состоит
# из атрибутов builtins function
print('The contents of the library are::')

# module Object используется как параметр
print(dir(builtins))