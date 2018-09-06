-   错误信息： SyntaxError: Non-ASCII character
    原因： 注释里有中文
    解决办法：在最开始加 `#coding=utf-8`
    python2.x 版本才有的吧。。。

-   书写问题：
    python 没有括号，以至于在写控制语句时是根据缩进来解析
    缩进很重要！

-   vscode 环境问题
    python 版本导入环境

-   vscode 编写 python 如何禁止 flake8 提示 line too long
    "python.linting.flake8Args": ["--max-line-length=248"]
