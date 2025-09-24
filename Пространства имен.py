"""
Программа, которая эмулирует работу с пространствами имен.

На вход подаются следующие запросы:
- create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
- add <namespace> <var> – добавить в пространство <namespace> переменную <var>
- get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из 
  пространства <namespace>, или None, если такого пространства не существует
"""


def create(namespace, parent):
    template = {'parent': parent, 'variables': set()}
    scopes[namespace] = template


def add(namespace, var):
    scopes[namespace]['variables'].add(var)


def get_scope(namespace, var):
    if namespace is None:
        return None
    if var in scopes[namespace]['variables']:
        return namespace
    else:
        return get_scope(scopes[namespace]['parent'], var)


scopes = {'global': {'parent': None, 'variables': set()}}

for _ in range(int(input())):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    if cmd == 'add':
        add(namesp, arg)
    if cmd == 'get':
        print(get_scope(namesp, arg))


# Для отладки
# scopes = {'global': {'parent': None, 'variables': {'a'}}, 'foo': {'parent': 'global', 'variables': {'b'}}}
# print()
# print(get_scope('foo', 'c'))  # None
# print(scopes)
