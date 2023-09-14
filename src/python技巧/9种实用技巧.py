# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 9种实用技巧.py
@time: 2023/9/7 10:59
"""

# 1. 整理字符串输入（translate）： 通常情况下，将字符转换为小写或大写就够了，有时你可以使用正则表达式模块「Regex」完成这项工作。但是如果问题很复杂，可能有更好的方法来解决：
user_input = """ This    
string has some whitespaces ...
"""

character_map = {
    ord('\t'): ' ',
    ord('\n'): ' ',
    ord('\r'): None,
}

new_user_input = user_input.translate(character_map)
print(new_user_input)

# 2. 迭代器切片（slice）： 如果对迭代器进行切片操作，会返回一个「TypeError」，提示生成器对象没有下标，但是我们可以用一个简单的方案来解决这个问题
tests = [1, 2, 3, 4]
for val in tests[0:3]:
    print(val)
import itertools

s = itertools.islice(range(50), 10, 20)
for val in s:
    print(val)

# 3. 跳过可迭代对象的开头（dropwhile）:有时你要处理一些以不需要的行（如注释）开头的文件。「itertools」再次提供了一种简单的解决方案：
string_from_file = """// Author: ...  
// License: ...  
//  
// Date: ...  
Actual content... 
"""


def is_positive(n):
    result = n.startswith('//')
    print(n, '==>', result)
    return result


# dropwhile使用时，有点坑，必须从一开始一直是true，直到false，之后就算再有true，也无法进行过滤
for line in itertools.dropwhile(lambda t: t.startswith('//'), string_from_file.split('\n')):
    print(line)


# for line in itertools.dropwhile(is_positive, string_from_file.split('\n')):
#     print(line)

# 4. 只包含关键字参数的函数（kwargs）
def test(*, a, b):
    pass


# test('value for a', 'value for b') # 异常
test(a='valuea', b='valueb')


# 5. 上下文管理：创建支持「with」语句的对象
class Connection:
    def __init__(self):
        self.i = 0

    def __enter__(self):
        print('Initialize connection...')

    def __exit__(self, type, value, traceback):
        print('Close connection...')


with Connection() as c:
    # __enter__() executes
    print('hahh')
    # conn.__exit__() executes
# 更简单
from contextlib import contextmanager
@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'<{name}2>')
with tag('h1'):
    print("This is Title.")

# 6. 用「slots」节省内存：Python 使用字典来表示类实例的属性，这使其速度很快，但需要使用大量内存，且内存使用效率却不是很高，
class Person:
    # 定义「slots」属性时，python没有使用字典来表示属性，而是使用小的固定大小的数组，大大减少了每个实例所需的内存
    # 缺点是：不能声明任何新的属性，只能使用「slots」上现有的属性。而且，带有「slots」的类不能使用多重继承
    __slots__ = ["first_name", "last_name", "phone"]
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

# 7. 限制「CPU」和内存使用量： 直接将内存和cpu限制为某个确定的数据
import signal
import resource
import os
# To Limit CPU time
def time_exceeded(signo, frame):
    print('CPU exceeded...')
    raise SystemExit(1)
def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)
# To limit memory usage
def set_max_memory(size):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (size, hard))

# 8. 控制可以/不可以导入什么：所有成员都会被导出（除非我们使用了「all」）
def foo():
    pass
def bar():
    pass
__all__ = ["bar"] # 可以让「all」为空，这样就不会导出任何东西。当导入这个模块时，会造成「AttributeError」

# 9. 实现比较运算符的简单方法：「functools.total_ordering」,如 （lt , le , gt , ge）
from functools import total_ordering
@total_ordering
class Number:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value
print(Number(20) > Number(3))
print(Number(1) < Number(5))
print(Number(15) >= Number(15))
print(Number(10) <= Number(2))

















