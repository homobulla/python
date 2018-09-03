### number and string

#### number 计算 大致类似于 js

#### 一些不同之处

有 floast 和 int 类型
除了 int 和 float，Python 还支持其它数字类型，例如 Decimal 和 Fraction。Python 还内建支持 复数 ，使用后缀 j 或 J 表示虚数部分（例如，3+5j）。

```py
8 / 8
# 1.0  / 永远返回一个float
8 // 5 # 1
8 // 5 # 1.0 // 永远返回小数点之前的整数，至于是float 还是 int ，取决于除数和被除数的类型
8 % 5 # 3 % 求摸操作符 ,返回类型同上
# 整数和浮点数的混合计算中，整数会被转换为浮点数
```

#### string

单双引号，字符转义`\`,如果你前面带有 \ 的字符被当作特殊字符，你可以使用 原始字符串，方法是在第一个引号前面加上一个 r:

```py
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

python 提供了类似 html 的`<pre>`标签的功能，可以保留换行符和空格，一是使用三引号： `"""..."""` 或者 `'''...'''`,其中可以用 \ 来去除换行。

```py
>>> print ('''\
demo
	this is line one        happy
	this is line two        sad''')
demo
	this is line one        happy
	this is line two        sad
>>> print ('''
demo
	this is line one        happy
	this is line two        sad''')

demo
	this is line one        happy
	this is line two        sad
>>>
```

用`+`来链接字符和表达式，用`*`来重复字符串,字符同样可以被检索，（支持正负）以及切片，

```py
>>> homobulla[:1] + homobulla[1:]
'homobulla'
>>> homobulla[:4] + homobulla[4:]
'homobulla'
```

<b>字符串不可变</b>,内置函数 len() 返回字符串长度:

```py
>>> word[0] = 'J'
  ...
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
  ...
TypeError: 'str' object does not support item assignment
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

#### list

复合数据类型之一：列表，基本就是 js 的数组，切片，赋值，浅拷贝，嵌套等等。

`range(int1,int2,int3)`函数生成一个可迭代列表，`list()`也是一个迭代器

```py
>>> list(range(0,101,10))

[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```
