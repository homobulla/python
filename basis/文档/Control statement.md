### python 中的控制流语句

#### for 循环

当在循环中进行列表的修改时，可以迭代其副本，即使用切割标识符：

```py
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
```

#### if 语句

if...elif...elif...else(非必需)

#### break 和 continue 语句, 以及循环中的 else 子句

`break`跳出当前循环，循环中可以套`else`语句用来循环那些条件为`flase`的情况，当有`break`的时候就不会执行了。

```py
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
            # 这里的else不是在上面的if里，而是在外层的for循环中，
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

#### pass 语句

`pass`语句类似于占位语句，即语法上需要有语句但真正程序什么也不做。
