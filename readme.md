### Python学习记录
Url: https://www.liaoxuefeng.com/wiki/1016959663602400/1017092876846880

### Python笔记
1. python中加号+左右两侧类型不一致会报错
2. mac 和 Linux下可以直接通过文件运行.py文件,需要配置(在.py文件的首行加上描述:#!/usr/bin/env python3 然后给文件执行权限,授权命令: chmod a+x hello.py)
3. 

## 数据类型
1. 整数 1 -1 0
2. 浮点数 即小数, 对于特别大或者特别小的浮点数,需要用科学计数法; 把10用e替代，1.23x(10的9次幂)就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5
3. 字符串 用"" 或者 ''括起来的任意文本
    1. 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
    2. 字符串特殊处理: r'': 表示''内部的字符串默认不转义 rint(r'\\\t\\') ===> \\\t\\
    3. 字符串特殊处理: Python允许用'''...'''的格式表示多行内容
        ```
          print('''line1
            ... line2
            ... line3''')
        ```
4. 布尔值
    1. True False 注意大小写 只能是大写
    2. and运算是与运算，只有所有都为True，and运算结果才是True (类似JavaScript中的 && )
    3. or运算是或运算，只要其中有一个为True，or运算结果就是True (类似JavaScript中的 || )
    4. not运算是非运算，它是一个单目运算符，把True变成False，False变成True (类似JavaScript中的 ! )
5. 空值 用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

## 变量
1. Python变量大小写敏感
2. 常量:不能变的变量; 通常用全部大写的变量名表示常量,但事实上其实仍然是一个变量; (用全部大写的变量名表示常量只是一个习惯上的用法)
2. 除法相关的符号
    1. / 除法: 计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数; 9 / 3 ==> 3.0 
    2. // 地板除: 两个整数的除法仍然是整数, 会舍弃小数部分,只留下整数部分; 10 // 3 ===> 3 
    3. % 取余数 10 % 3 ===> 1

## 字符串
1. 字符串格式化问题
    JavaScript中: `My name is ${name}, I'm ${12}`
    python中: 'My name is %s, I'm %d' % ('Namevalue', 15)
    % 运算符就是用来格式化字符串的。在字符串内部:
    %s: 表示字符串
    %d: 表示整数
    %f: 表示浮点数
    %x: 表示十六进制整数
    有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
2. format()格式化: 用传入的参数依次替换字符串内的占位符
    print('Hello, {0}, 成绩提升了 {1}%'.format('小明', 17.25))

## list 列表 (类似JavaScript中的数组)
1. 定义: classmates = ['Johnny', 'Jack', 'Smith']
2. len() 获取列表的长度 len(classmates)  ===> 3
3. 列表的索引: ; 从0开始, 也可以从-1开始,-1代表从后往前的顺序 越界会报错
4. append(value): 向列表中追加value值
5. insert(index, value): 在列表的index位置,插入值value
6. pop(): 删除列表末尾的元素
7. pop(index): 删除指定位置的元素
8. 把某个元素替换成别的元素，可以直接赋值给对应的索引位置 classmates[0] = 'Admin'
9. 列表中的值可以是任意类型, 可以是二维列表多维列表,和JavaScript数组类似
    ```
    >>> classmates = ['Johnny', 'Jack', 'Smith']
    >>> classmates
    ['Johnny', 'Jack', 'Smith']
    >>> classmates[0]
    'Johnny'
    >>> classmates[-1]
    'Smith'
    >>> classmates[3]
    报错: IndexError: list index out of range
    >>> classmates.append('Bob')
    >>> classmates
    ['Johnny', 'Jack', 'Smith', 'Bob']
    >>> classmates.insert(1, 'Mark')
    >>> classmates
    ['Johnny', 'Mark', 'Jack', 'Smith', 'Bob']
    >>> classmates.pop()
    'Bob'
    >>> classmates
    ['Johnny', 'Mark', 'Jack', 'Smith']
    >>> classmates.pop(1)
    'Mark'
    >>> classmates
    ['Johnny', 'Jack', 'Smith']
    >>> classmates[0] = 'Admin'
    >>> classmates
    ['Admin', 'Jack', 'Smith']
    ```
## tuple 列表 (和list类似,但是tuple一旦初始化就不能修改)
1. 声明方式: classmates = ('Michael', 'Bob', 'Tracy')
2. tuple列表不能变, 所以list中增删的方法在tuple中不适用
3. 定义一个空的tuple: a = ()
4. [PS]特别注意
    ```
    # 这样定义的不是一个tuple,而是数字1
    >>> a = (1)
    # 正确定义方式
    >>> a = (1,)
    ```
5. tuple中,表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
    ```
    >>> t = ('a', 'b', ['A', 'B'])
    >>> t[2][0] = 'X'
    >>> t[2][1] = 'Y'
    >>> t
    ('a', 'b', ['X', 'Y'])
    ```
    ![avatar](https://www.liaoxuefeng.com/files/attachments/923973516787680/0)
    当我们把list的元素'A'和'B'修改为'X'和'Y'后，tuple变为：
    ![avatar](https://www.liaoxuefeng.com/files/attachments/923973647515872/0)

## 条件判断
1. if elif else  (注意点: 要少写了冒号:)
    ```
    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')
    ```

## 循环 (for...in...) (while)
  1. for...in
    ```
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
    # 会依次打印出name
    ```
  2. while循环
      只要条件满足，就不断循环，条件不满足时退出循环
      ```
        sum = 0
        n = 99
        while n > 0:
            sum = sum + n
            n = n - 2
        print(sum)
      ```
  3. break continue 在循环中的应用
    1. break: 前退出循环
        ```
          # for...in...中使用
          n = 0
          for x in [1,2,3,4,5]:
            if x == 3:
              break
            n = n + x
          print(n)

          # while中使用
          w = 5
          wsum = 0
          while w > 0:
            w = w - 1
            if w == 3:
              break
            wsum = wsum + w
          print(wsum)
        ```

    2. continue: 跳过当前的这次循环，直接开始下一次循环
        ```
          # for...in...中使用
          n = 0
          for x in [1,2,3,4,5]:
            if x == 3:
              continue
            n = n + x
          print(n)

          # while中使用
          w = 5
          wsum = 0
          while w > 0:
            w = w - 1
            if w == 3:
              continue
            wsum = wsum + w
          print(wsum)
      ```  


## dict
  dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
  1. pop(key) 删除dict中某一个key
  ```
  >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
  >>> d['Michael']
  95
  >>> d['New'] = 80
  >>> d
  {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'New': 80}
  >>> d.pop('Tracy')
  85
  >>> d
  {'Michael': 95, 'Bob': 75, 'New': 80}
  ```
  一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉; 如果key不存在，dict就会报错
  ```
  >>> d['Jack'] = 90
  >>> d['Jack']
  90
  >>> d['Jack'] = 88
  >>> d['Jack']
  88
  ```

# 判断key是否在dict中
1. 'xxx' in dict
  ```
  >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
  >>> 'Bob' in d
  True
  ```
2. 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value; 返回None的时候Python的交互环境不显示结果
  ```
  >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
  >>> d.get('Bob')
  75
  >>> d.get('Thomas') # 返回None的时候Python的交互环境不显示结果
  >>> d.get('Thomas', -1)
  -1
  ```

## set 
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合
```
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

重复元素在set中自动被过滤：
```
>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
```

add(key):添加元素到set中，可以重复添加，但不会有效果
remove(key):删除元素
```
>>> s = set([1, 2, 3])
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.remove(2)
>>> s
{1, 3, 4}
```

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
```
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```

## 函数
```
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None

函数可以同时返回多个值，但其实就是一个tuple
```
1. 定义: 通过def来定义
  ```
  def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
  ```

2. 空函数 定义一个什么事也不做的空函数，可以用pass语句
  ```
  # pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
  def nop():
    pass
  ```
  pass 可以用在def中,也可以用在判断或者其他地方,用来占位

3. 引入一个自己定义模块的函数
  ```
  from filename(文件名) import defname(函数的名称)
  ```

4. 函数返回值
  函数中可以有返回值,也可以没有. 可以有一个返回值,也可以多个
  函数如果有返回值的话,返回值返回的类型是tuple,如果只有一个返回值,可以省略括号, 多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple
  ```
  def my_abs (x):
    if x > 0:
      return x
    else:
      return -x

  def test1 (x, y):
    return x+1, y+1

  w = my_abs(12)       # 12
  a = test1(1, 2)      # (2, 3)
  b, c = test1(1, 2)   # b=2 c=3
  (d, e) = test1(1, 2) # d=2 e=3
  ```

## 函数的参数
  1. 默认参数
      和JavaScript类似, 默认参数的值赋值用等号=赋值,位置放在后面,调用的时候,与JavaScript略有不同,可以根据位置来默认赋值,也可以直接传key=value来,这样不同担心默认参数的顺序
  ```
    def my_info (name, gender, age = 18, city = 'shenzhen' ):
    print('name:', name) 
    print('gender:', gender) 
    print('age:', age) 
    print('city:', city) 

    my_info('Bob', 'Male', 20, 'Beijing')
    my_info('Alex', 'Female', 24, 'XIAN')
    my_info('Johnny', 'Male', 20)
    my_info('Amy', 'Female', city = 'Wuhan')
    my_info('Test', 'Female', city = 'Wuhan', age = 10)
    my_info('Amy', 'Female')
  ```

  2. 可变参数
      定义: 传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
      定义规则: 在函数的参数名称前面加上一个*; 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

      ```
        # 普通的函数参数,调用的时候传递的是一个tuple
        def my_sum (numbers):
          sum = 0
          for num in numbers:
            sum = sum + num * num
          return sum
        my_sum([1,2,3])

        # 可变参数, 直接以参数的形式传递进去即可
        def my_sum (*numbers):
          sum = 0
          for num in numbers:
            sum = sum + num * num
          return sum
        my_sum(1,2,3)
      ```
    
  3. 关键字参数
      定义: 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
      定义规则: 在函数的参数名称前面加上**
      ```
        # 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数,也可以传入任意个数的关键字参数
        def person (name, age, **kw):
          print('My name is %s, I\'m %d' % (name, age))
          print('Other:', kw)

        person('Johnny', 18)
        person('Johnny', 18, a = 10)
        person('Johnny', 18, a = 10, b = 'aa')

        # 关键字参数也可以简写成以下形式
        extra = {'city': 'Beijing', 'job': 'teacher'}
        person('Johnny', 18, **extra)
      ```
  
  4. 命名关键字参数
      为了解决关键字参数中存在的缺陷,函数的调用者可以传入任意不受限制的关键字参数,如果要限制关键字参数的名字，就可以用命名关键字参数
      定义规则: 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
      ```
        # 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
        def person (name, age, *, city, job):
          print(name, age, city, job)

        person('Johnny', 18, city='Shenzhen', job='dever')
        person('Johnny', 18, job='Teacher', city='Wuhan')
      ```

      如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
      ```
        def person(name, age, *args, city, job):
          print(name, age, args, city, job)

        person('Johnny', 18, 1, 2, 3, city='Shenzhen', job='dever') # result: Johnny 18 (1, 2, 3) Shenzhen dever
        person('Johnny', 18, city='Shenzhen', job='dever') # result:Johnny 18 () Shenzhen dever
      ```

      命名关键字参数可以有缺省值，从而简化调用(配合默认值参数使用)
      ```
        def person(name, age, *, city = 'Beijing', job):
          print(name, age, city, job)

        person('Johnny', 10, city='Shenzhen', job='dever') # result: Johnny 18 (1, 2, 3) Shenzhen dever
        person('Johnny', 20, job='dever') # result:Johnny 18 () Shenzhen dever
      ```

      PS: 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
  
  5. 参数组合
      在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
      参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
      ```
        def f1(a, b, c=0, *args, **kw):
          print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

        def f2(a, b, c=0, *, d, **kw):
          print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

        >>> f1(1, 2)
        a = 1 b = 2 c = 0 args = () kw = {}
        >>> f1(1, 2, c=3)
        a = 1 b = 2 c = 3 args = () kw = {}
        >>> f1(1, 2, 3, 'a', 'b')
        a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
        >>> f1(1, 2, 3, 'a', 'b', x=99)
        a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
        >>> f2(1, 2, d=99, ext=None)
        a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
      ```
      PS: 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
      ```
        >>> args = (1, 2, 3, 4)
        >>> kw = {'d': 99, 'x': '#'}
        >>> f1(*args, **kw)
        a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
        >>> args = (1, 2, 3)
        >>> kw = {'d': 88, 'x': '#'}
        >>> f2(*args, **kw)
        a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
      ```


  6. 小结总计:
      *args是可变参数，args接收的是一个tuple；

      **kw是关键字参数，kw接收的是一个dict。

      以及调用函数时如何传入可变参数和关键字参数的语法：

      可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

      关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

      使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

      命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

      定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

## 递归函数
    在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
    例如计算阶乘
    ```
      def fact(n):
        if n==1:
          return 1
        return n * fact(n - 1)
    ```

    栈溢出问题: 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
    解决递归调用栈溢出的方法是通过尾递归优化, 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

    ```
      def fact(n):
        if n==1:
          return 1
        return n * fact(n - 1)
      
      >>>fact(1000)
      由于栈溢出问题报错: RuntimeError: maximum recursion depth exceeded in comparison

      # 解决方案, 尾递归优化
      def fact(n):
        return fact_iter(n, 1)

      def fact_iter(num, product):
        if num == 1:
          return product
        return fact_iter(num - 1, num * product)

    ```

