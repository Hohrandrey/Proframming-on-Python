from logging import root

from graphviz import Digraph

def t_1_1():
    class MyClass:
        def __init__(self):
            self.public_field = 1
            self._protected_field = 2
            self.__private_field = 3

    obj = MyClass()
    # Фильтруем служебные имена (начинающиеся с _)
    print([name for name in vars(obj) if not name.startswith('_')])


def t_1_2():

    class MyClass:
        def my_method(self):
            return "Метод вызван!"

    obj = MyClass()
    method_name = "my_method"
    # Получаем метод по имени и вызываем его
    print(getattr(obj, method_name)())


def t_1_3():

    class A:
        pass

    class B(A):
        pass

    class C(B):  # Просто наследуем от B, который уже включает A
        pass

    print("Проблема исправлена - теперь класс C наследует только от B")


def t_1_4():
    """Функция-однострочник для вывода иерархии наследования"""
    get_inheritance = lambda cls: " -> ".join([c.__name__ for c in cls.__mro__])

    # Пример использования
    print(get_inheritance(OSError))

def t_2_1():
    class HashTable:
        def __init__(self, size=10):
            self.size = size
            self.table = [[] for _ in range(size)]
            self.length = 0

        def _get_index(self, key):
            """Вычисляет индекс в таблице по ключу"""
            return hash(key) % self.size

        def __setitem__(self, key, value):
            """Устанавливает значение для заданного ключа"""
            index = self._get_index(key)
            bucket = self.table[index]

            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return

            bucket.append((key, value))
            self.length += 1

        def __getitem__(self, key):
            """Возвращает значение по ключу или вызывает KeyError"""
            index = self._get_index(key)
            bucket = self.table[index]

            for k, v in bucket:
                if k == key:
                    return v

            raise KeyError(f"Key '{key}' not found")

        def __len__(self):
            """Возвращает количество пар ключ-значение в таблице"""
            return self.length

        def __str__(self):
            """Строковое представление таблицы (для отладки)"""
            return str(self.table)

    ht = HashTable()

    ht['name'] = 'Alice'
    ht['age'] = 365
    ht[42] = 'The 42 gang'

    print(ht['name'])
    print(ht['age'])
    print(ht[42])

    try:
        print(ht['566'])
    except KeyError as e:
        print(e)

    print(len(ht))

    ht['age'] = 31
    print(ht['age'])


def draw(vertices, edges):
    # Создаём ориентированный граф
    dot = Digraph()

    # Добавляем все вершины
    for node_id, label in vertices:
        dot.node(str(node_id), label=label)

    # Добавляем все рёбра
    for source, target in edges:
        dot.edge(str(source), str(target))

    # Визуализируем граф
    dot.render('graph', format='png', cleanup=True)
    return dot


def t_4():
    class HTML:
        def __init__(self):
            self._code = []
            self._context = []

        def __getattr__(self, tag_name): #динамич теги
            return Tag(self, tag_name)

        def get_code(self): #соединение строки
            return '\n'.join(self._code)

        def _add_line(self, line, indent_level): #отступы
            self._code.append(' ' * (indent_level * 2) + line)

        def _push_context(self, tag):
            self._context.append(tag)

        def _pop_context(self):
            return self._context.pop()

    class Tag:
        def __init__(self, html, name):
            self._html = html
            self._name = name

        def __call__(self, *args, **kwargs):
            if args:
                text = args[0]
                indent_level = len(self._html._context)
                self._html._add_line(f'<{self._name}>{text}</{self._name}>', indent_level)
            else:
                return self

        def __enter__(self):
            indent_level = len(self._html._context)
            self._html._add_line(f'<{self._name}>', indent_level)
            self._html._push_context(self)
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            tag = self._html._pop_context()
            indent_level = len(self._html._context)
            self._html._add_line(f'</{tag._name}>', indent_level)

    # Пример использования
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')

    print(html.get_code())

#ЗАДАНИЕ 5

def generate_docs(module_file):
    with open(module_file, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())

    result = []
    module_doc = ast.get_docstring(tree)
    if module_doc:
        result.append(f"# Модуль {module_file}\n{module_doc}\n")

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_doc = ast.get_docstring(node)
            if class_doc:
                result.append(f"## Класс {node.name}\n{class_doc}\n")

            for item in node.body:
                if isinstance(item, ast.FunctionDef) and not item.name.startswith('_'):
                    method_doc = ast.get_docstring(item)
                    if method_doc:
                        args = [arg.arg for arg in item.args.args]
                        sig = f"{item.name}({', '.join(args)})"
                        result.append(f"* **Метод** `{sig}`\n{method_doc}\n")

        elif isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
            func_doc = ast.get_docstring(node)
            if func_doc:
                args = [arg.arg for arg in node.args.args]
                sig = f"{node.name}({', '.join(args)})"
                result.append(f"## Функция {node.name}\nСигнатура: `{sig}`\n{func_doc}\n")

    return ''.join(result)

import os
import ast
from pathlib import Path
import graphviz


def visualize_project_structure(project_path='.'):
    dot = graphviz.Digraph(comment='Project Structure')

    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py'):
                module_path = Path(root) / file
                relative_path = module_path.relative_to(project_path)
                module_name = str(relative_path).replace(os.sep, '.').replace('.py', '')

                with open(module_path, 'r', encoding='utf-8') as f:
                    try:
                        tree = ast.parse(f.read())
                        dot.node(module_name)

                        for node in ast.walk(tree):
                            if isinstance(node, ast.ImportFrom):
                                if node.module:
                                    full_module = f"{node.module}"
                                    dot.edge(module_name, full_module)
                            elif isinstance(node, ast.Import):
                                for alias in node.names:
                                    dot.edge(module_name, alias.name)
                    except Exception as e:
                        print(f"Error processing {module_path}: {e}")
                        continue

    output_filename = '5.2'
    dot.render(output_filename, format='png', view=True)
    print(f"Project structure visualization saved as {output_filename}.png")

#ЗАДАНИЕ 6

# Библиотека встроенных операций
def add(vm):
    b = vm.stack.pop()
    a = vm.stack.pop()
    vm.stack.append(a + b)

def dot(vm):
    value = vm.stack.pop()
    print(value)

LIB = {
    '+': add,
    '-': None,
    '*': None,
    '/': None,
    '%': None,
    '&': None,
    '|': None,
    '^': None,
    '<': None,
    '>': None,
    '=': None,
    '<<': None,
    '>>': None,
    'if': None,
    'for': None,
    '.': dot
}

OP_NAMES = {
    0: 'push',
    1: 'op',
    2: 'call',
    3: 'is',
    4: 'to',
    5: 'exit'
}

class VM:
    def __init__(self, code):
        self.stack = []
        self.code = code
        self.pc = code[0]  # точка входа

    def run(self):
        while self.pc < len(self.code):
            instr = self.code[self.pc]
            op_code = instr & 0b111
            arg = instr >> 3
            op = OP_NAMES.get(op_code, None)

            if op == 'push':
                self.stack.append(arg)

            elif op == 'op':
                lib_op = list(LIB.keys())[arg]
                func = LIB.get(lib_op)
                if func:
                    func(self)
                else:
                    raise RuntimeError(f"Operation '{lib_op}' not implemented")

            elif op == 'exit':
                break

            else:
                raise RuntimeError(f"Unknown operation: {op}")

            self.pc += 1

def disasm(code):
    OP_NAMES = {
        0: 'push',
        1: 'op',
        2: 'call',
        3: 'is',
        4: 'to',
        5: 'exit',
    }

    LIB_NAMES = [
        '+', '-', '*', '/', '%',
        '&', '|', '^',
        '<', '>', '=',
        '<<', '>>',
        'if', 'for', '.'
    ]

    entry = code[0]
    print("entry:")

    i = entry
    while i < len(code):
        instr = code[i]
        op_code = instr & 0b111          # 3 младших бита — код операции
        arg = instr >> 3                 # Остальные 29 бит — аргумент
        opname = OP_NAMES.get(op_code, f"unknown({op_code})")

        # Отображение инструкции
        if op_code == 1:  # op
            if arg < len(LIB_NAMES):
                op_arg = LIB_NAMES[arg]
            else:
                op_arg = f"<unknown op {arg}>"
            print(f"  {i:>3}: {opname} '{op_arg}'")
        else:
            print(f"  {i:>3}: {opname} {arg}")

        if opname == "exit":
            break
        i += 1


def main():
    """
    print("Задание 1.1:")
    t_1_1()

    print("\nЗадание 1.2:")
    t_1_2()

    print("\nЗадание 1.3:")
    t_1_3()

    print("\nЗадание 1.4:")
    t_1_4()

    print("\nЗадание 2.1:")
    t_2_1()

    print("\nЗадание 3.1:")
    draw([(1, 'v1'), (2, 'v2')], [(1, 2), (2, 3), (2, 2)])


    print("\nЗадание 4:")
    t_4()


    print("\nЗадание 5.1:")
    print(generate_docs("example.py"))

    print("\nЗадание 5.2:")
    visualize_project_structure()
    """
    print("\nЗадание 6.1:")
    disasm([0, 16, 16, 1, 121, 5])

    print("\nЗадание 6.2:")
    code = [0, 16, 16, 1, 121, 5]  # push 2, push 2, op '+', op '.', exit
    vm = VM(code)
    vm.run()

if __name__ == "__main__":
    main()