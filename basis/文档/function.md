### 函数

> 无论什么语言，函数都是重中之重. ——homobulla

#### 函数的定义

关键字`def`,在其后必须跟有函数名和包括形式参数的圆括号。函数体语句从下一行开始，必须是缩进的。
函数体的第一行语句可以是可选的字符串文本，这个字符串是函数的文档字符串，或者称为 docstring。

```py
def fib(n):
    """Print a Fibonacci series up to n."""
    a,b = 0,1
    while(a<n):
        print(a,end=' ' )
        a,b = b,a+b
    print()
```

函数内变量、参数、作用域的问题：
