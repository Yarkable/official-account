# Python学习笔记

## 易错点和难点集锦

***

* 输入输出问题

    * 用input输入的是字符
```python
a=input()
b=input()
print('a+b=',a+b)
#这时会输出a+b=xx,但是input返回的ab是str型数据，不是数字
#所以输入a=2，b=3，结果是23，必须强制转换数据类型int(a)才能得到5
#print函数中起连接作用的逗号输出是一个空格
```

***

* 转义字符

    * 遇到特殊的字符时输出需用转义符`\`转义,例如`'I\'m \"OK\"!'`输 出的就是I'm ok!
    * 可以在字符串前面加上`r`默认里面的字符串不转义

    `print(r'\\\t\\')`输出`\\\t\\`
    * `\n`用来表示换行，但是有时需要太多换行了则可以用`'''···'''`的形式来表示多个换行输出（三个单引号）

***

* 数据类型
    * 布尔型
        * 注意布尔型的大小写，是`True`和`False`
        * 布尔型的运算符有`and`、`or`、`not`，分别代表与或非
        * not一般是单目运算符，其他两个都是双目运算符，可以使用`not False`表示True
    * 空值
        * python里的空值用None表示，相当于js和C语言里的null，不能认为空值为0，None是一个特殊的空值

* python里的常量全部用大写表示，如PI=3.1415936，和C语言差不多
* python的除法
    * `/`是通用除法，取得的结果为浮点型数据，即使是`9/3`得到的结果也是3.0
    * `//`的结果是整数，即他会舍弃小数位，只取整数位的值
    * `%`取余

***

* 编码问题
    * python的字符串类型为str，在内存中以unicode表示，传输或者写入磁盘时则需要将str变成以字节为单位传输的bytes
    * Python对bytes类型的数据用带b前缀的单引号或双引号表示,例如
    x = b'ABC'
    * 用encode()方法可以将str编码成指定的bytes，例如
    ```python
        x='ABC'
        x.encode('utf*8')
        #那么输出的是b'ABC'
    ```
    * 相反地，如果我们从硬盘上读取了字节流，想变成str，则使用decode()方法
    ```python
    b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf*8')
    #输出为：'中文'
    ```
    * 还得注意中文的编码，中文一定要用utf*8编码，不能用asci码，否则会出现乱码
    * 用len()方法计算的是str的字符数，若括号内为bytes，则计算的是字节数
    ```python
    len('中文'.encode('utf*8'))
    #或者
    len(b'\xe4\xb8\xad\xe6\x96\x87')
    #输出：6  
    #所以一般中文字经过utf*8编码后，占三个字节，一个英文字母占一个字节
    ```
    * 一般为了防止乱码，在py文件的最头部加上
    `#*** coding: utf*8 ***`表明是在utf*8编码下的文件

***

* 格式化输出
    * python的格式化输出和C语言的是一样的，就是有些差别而已，下面给出对照
    ```c
    //C语言
    x=100;
    printf("x=%d",x);
    ```
    ```python
    #python
    x=100
    print('x=%d' %x)
    ```

***

* list(相当于C语言的数组)
    * 在python里面叫做列表，表示形式为[' ',' ',' ']
    * 与C语言不同之处
        * 这个list的内容是可变的，因此可以用很多种*方法*对他进行修改
        * 另一个不同之处就是python可以直接用list[-1]访问倒数第一个元素，以此类推，list[-n]访问倒数第n个元素，只要不越界就可以了
        * 若要修改元素值，直接用list[i]='xx'即可替换掉原先的值
        * list的元素可以是不同类型的值，而C语言的数组只能是一种类型
        * list的元素也可以是另一个list，这点就相当于C语言的多维数组
    * list的各种*方法*
        * len(list)获取当前list的成员个数
        * list.append('xx')表示在list的末尾加入一个xx元素
        * list.insert(i,'xx')将xx元素插入到索引号为 i 的位置
        * list.pop(i)删除list索引号为 i 处的元素
        * list可以用`+`将两个list相连起来

    ```python
    l=[1,2,3]
    t=[0]+l+[4]
    t
    [0,1,2,3,4]
    ```

***

* tuple(元祖，比list更像C语言的数组)
    * 形式为(' ',' ',' ')
    * 不像list有那么多的*方法*，tuple的内容也不可以修改，但是还是可以用tuple[-n]的方法来获取倒数第n个元素的值
    * 因为不能够修改值，所以更加安全，因此能用tuple就不要用list
    * tuple有个**陷阱**，即定义tuple时必须确定下来tuple的值，定义空的tuple直接tuple(),但是定义只有一个值的tuple必须要用tuple=(1,)，
    不加逗号则输出的不是一个tuple，而是一个整数，因为tuple=(1)的括号也可以表示数学中的小括号，python规定没有逗号时就视为数学的小括号

***

* 条件判断语句
    * python的条件语句一般形式为 `if···elif···else`
    * 不像C语言使用大括号表示代码块，python表示代码块用的是`:`和缩进，并且if后面的条件也不需要打括号（打括号也不会报错）

***

* 循环语句
    * 在python中，有两种循环，一种是for···in···，一种是while···
    * for···in···循环
        * 这种循环是对list和tuple而言的，对他们的每一个元素进行迭代
        * 一般数据量大的时候，用range(i)函数可以创造一个从0到i*1的序列，例如range(5)是0，1，2，3，4，若用list(range(5))函数可以输出[0,1,2,3,4]
        * 注意python的自增自减不能够用i++，只能i=i+1
    * while循环
        * 与C语言相当，结构为`while(True)···//code`
    * break和continue语句
        * 只能用于循环中，不能随便乱用

***

* dict--python内置的字典
    * 相当于json吧？！使用的是键-值（key-value）的结构体系，比list查找数据更加快捷方便，结构为`s={'Michael': 95, 'Bob': 75, 'Tracy': 85}`
    * 就像查字典时用部首偏旁检索比一个字一个字找快得多的多，查找dict中的元素的值也只需要给出键（key）就可，和json一样，如果值（value）为字符时需要打上单引号
    * 检索的时候只需用key即可`s['Micheal']`输出 95
    * dict的各种方法
        * 给dict中增加不存在的key，直接给该不存在的key赋值即可，例如`s['kai']='excellent'`，但是由于一个key只对应一个value，所以给同一个key赋值时以最后的value为准
        * 对dict里不存在的key取值时会报错，因此可以用`'key' in dict`的方法判断key是否在dict中，；例如`'Micheal' in s`返回的就是`True`
        * 还有一种方法判断key是否在dict中，用`dict.get('key',ReturnValue)`，如果key存在的话则返回value，若不存在则返回None，但是返回None时交互环境是不会显示出来的，所以一般自定一个ReturnValue供返回
        * dict.pop('key')方法删除对应的key
    * 要注意dict中的key都是不可变的对象，list不能够作为dict的key，并且dict中的key是无序的

***

* set--储存key的一个集合
    * set就像是数学中的无序、没有重复值的集合，里面储存的是key，但是不储存value，形式为{'key','key','key'},set也是不可变的对象
    * 创建一个set需要以一个list作为输入集合，创建形式为`s=set(list)`，并且list中如果有重复元素则会被重合，给出下列例子
    ```python
    s=set([1,2,3,4,5])
    s
    {1,2,3,4,5}  #输出是一个set形式的数据
    s=set([1,2,3,3,4,5,5])
    s
    {1,2,3,4,5}  #重复的key被重合了
    ```
    * set的各种方法
        * s.add(key)可以向set中增加key，但是增加相同的key无效
        * s.remove(key)删除set中的key
        * 由于set可以看成是数学集合，所以拥有交集`&`和并集`|`等操作

    ```python
    s1=set([1,2,3])
    s2=set([2,3,4])
    s1&s2
    #{2,3}
    s1|s2
    #{1,2,3,4}
    ```

***

* 函数
    * 自定义函数用的是def functionName(argument):···pass，自定义一个求绝对值的函数，且和C语言不同，这里的参数不用加上类型
    ```python
    def abs(n):
        if n>=0:
            return n
        else:
            return -n
    ```
    * 函数运行到return处停止运行，如果没有确定的返回值则返回None，并且如果没想好函数主体可以用`pass`表示空函数，日后想起来再填补
    * python的返回值可以是一个tuple，此tuple可以省略括号，所以给人的感觉是python可以返回多个值
    * 函数的参数：
        * 同上，参数不用像C语言那样加上类型
        * 有必选参数和默认参数，一个实参对应着一个必选参数，不能多也不能少。默认参数就是给定参数一个具体的值，以后调用时就以该值作为值，形如求x^2的函数

    ```python
    def sqr(n,x=2):
        s=1
        while x>0:
            x=x*1
            s=s*n
        return s
    #这样子以后调用sqr(5)就相当于调用sqr(5,2)了
    ```
    * 再谈默认参数
        1. 默认参数一般放在必选参数的后面，否则python会报错
        2. 默认参数有时也会出错，另外，如果传入的参数不想按照默认参数来定，可以自行添加该参数对应的值
    * 可变参数
        1. 有时候一个具体问题的参数个数会变化，这时就可以用可变参数（参数的个数可变）
        2. 由于参数不确定，所以在定义时将这些参数作为一个list或者tuple，这是原始的方法，例如定义一个函数求a^2+b^2+c^2···

    ```python
    #原始方法
    def calc(num):
        sum=0
        for i in num:
            sum=sum+i*i
        return sum
    #调用函数
    #调用的时候要把数据组装成一个list或者tuple来进行参数传递
    calc([1,2,3])
    calc((1,2,3))
    #这两种都是合法的
    ```
        3. 在上一题中，若是在形参num前面加一个`*`，那么，这个参数就变成了可变参数，这种方法是十分方便的，对上一题用可变参数实现如下

    ```python
    def calc(*num):
        sum=0
        for i in num:
            sum=sum+i*i
        return sum
    #此时在函数内部num接收到的就是一个lsit或tuple
    #调用函数
    cal(1,2,3)
    cal()
    #调用函数时，可以传入任意个参数，0个也是可以的
    #要是已经有了一个list或者tuple，想把他作为可变参数，也可以直接在调用时向list（tuple）前加个*
    num=[1,2,3]
    #传统
    calc(num[0],num[1],num[2])
    #可变参数
    calc(*num)
    #可以看出，*的作用就是将list或tuple中的所有参数作为可变参数传入函数
    ```
    * 关键字参数
        1. 和可变参数的原理差不多，可变参数是将参数在内部组装成list或tuple，而关键字参数是将参数在内部组装成一个dict
        2. 关键字参数的作用在于补充说明，关键字函数允许传入任意个含参数名的函数，因此除了必选参数外，还可以用关键字参数补充信息
        3. 可变参数的形式为在参数前加上`*`，关键字函数就在参数前加上`**`，用一个例子就知道怎么回事了

    ```python
    #定义函数
    def foo(name,age,**args):
        print('name',name,'age',age,'others',args)
    #调用时
    foo('kai',18,city='shangrao')
    #输出
    name kai age 18 others {'city': 'shangrao'}
    #可以看出，关键字参数将我们输入的city组装成了一个dict
    #同样的，要是已经有了一个dict想传入，与可变参数的方法一样
    dict={'city':'shangrao'}
    foo('kai',18,**dict)
    #输出同样的结果
    ```
    * 命名关键字参数
        1. 和关键字参数差不多，关键字函数可以添加无穷多个参数值整合成dict，命名关键字参数限制了关键字参数的名字，只让特定参数名的参数传入
        2. 形式和关键字参数在前面加`**`不同，命名关键字函数常用`*`分隔，在`*`后的即是命名关键字参数
        3. 注意事项：
            * 若是在函数定义中已经有了一个可变参数，则后面跟着的命名关键字参数不需要再加`*`来分隔
            * 命名关键字参数必须传入参数名，这点和位置参数不同，即在调用的时候必须以`arg='··'`的形式传入命名关键字参数
            * 如果在命名关键字参数中有默认参数，调用时一样可以省略该参数
    * 参数组合
        * 介绍完了`必选参数`、`默认参数`、`可变参数`、`关键字参数`、`命名关键字参数`，在传入参数时，若在定义函数时，上述的参数种类都存在，则按照上述顺序传入参数
        * 下面借用廖老师的例子来说明调用函数时，函数的参数均可以用tuple和list来表达

    ```python
    #比如定义一个函数，包含上述若干种参数：
    def f1(a,b,c=0,*args,**kw):
    print('a =',a,'b =',b,'c =',c,'args =',args,'kw =',kw)
    def f2(a,b,c=0,*,d,**kw):
    print('a =',a,'b =',b,'c =',c,'d =',d,'kw =',kw)
    #在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
    >>> f1(1,2)
    a=1 b=2 c=0 args=() kw={}
    >>> f1(1,2,c=3)
    a=1 b=2 c=3 args=() kw={}
    >>> f1(1,2,3,'a','b')
    a=1 b=2 c=3 args=('a','b') kw={}
    >>> f1(1,2,3,'a','b',x=99)
    a=1 b=2 c=3 args=('a','b') kw={'x': 99}
    >>> f2(1,2,d=99,ext=None)
    a=1 b=2 c=0 d=99 kw={'ext': None}
    #最神奇的是通过一个tuple和dict，你也可以调用上述函数
    >>> args=(1,2,3,4)
    >>> kw={'d': 99,'x': '#'}
    >>> f1(*args,**kw)
    a=1 b=2 c=3 args=(4,) kw={'d': 99,'x': '#'}
    >>> args=(1,2,3)
    >>> kw={'d': 88,'x': '#'}
    >>> f2(*args,**kw)
    a=1 b=2 c=3 d=88 kw={'x': '#'}
    #所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。    
    ```
    * 递归函数
        * 和C语言中的递归一样，只是要注意python的语法，另外递归还涉及到了栈溢出的概念，即可以对递归进行`尾递归优化`，就是返回值不能带有运算符号，否则会导致栈溢出，例如用常规方法进行10000！就会栈溢出，这种方法有兴趣去百度一下
        * 但是遗憾的是python也没有针对尾递归做出优化，所以用了尾递归后仍会栈溢出

***

*  python的高级特性
    * 切片（Slice）
        * 意义就是用更简单的方法取list或tuple的部分元素
        * 原始方法要不断循环才能取得list或tuple的值，用python内置的切片符`:`即可快速操作

    ```python
    l=[1,2,3,4,5,6]    
    #原始方法取前三个值,用一个新的list接收取下来的值
    t=[]
    n=3
    for i in range(n):
        t.append(l[i])
    #用切片表示的是从list的0号索引取到3号索引（不包括三号）
    l[0:3]
    l[:3]   #从0开始取的话0可以不写
    #也可以由负检索从倒数第几位开始取
    l[-2:]  #输出（5，6）
    #也可以给定隔几位输出一个
    l[::2]  #表示检索所有数，每两个取一个
    l[::-1] #反过来取，abc则变成cba
    l[:]    #啥也不做，直接复制一个list
    ```
        * 切片的对象不止list和tuple，也可以对字符串进行切片

    ```python
    >>> l='abcdef'
    >>> l[:6:2]
    'bdf'
    ```
    * 迭代（iteration）
        * 通过for循环来遍历一个list或tuple，这种遍历称为迭代
        * 其实，只要是可迭代对象就可以用for循环迭代，dict是可迭代对象，字符串是可迭代对象，可以用collections中的Iterable判断对象是不是可迭代对象

    ```python
    from collections import Iterable
    isinstance('abc',Iterable)
    #True,表示str是可迭代对象
    for ch in 'abc':
        print(ch)
    #a
    #b
    #c
    ```
        * 对dict的迭代，默认情况下，迭代的是其中的key，但是也可以迭代value或者key—value

    ```python
    #由于dict在python中是无序的，所以迭代出来的结果跟想象的会不一样
    dict={'a':1,'b':2,'c':3}
    for key in dict:
        print(key)
    #可能会输出acb，也可能是abc
    #其中的变量key可以换成其他值，因为默认下迭代的就是key
    for value in dict.values():
        print(value)
    #同样，变量value也可以换成其他量，后面的values()一定要有括号
    for k,v in dict.items():
        print(k,v)
    #这是同时迭代key和value的方法
    #python中，for循环同时引用了两个变量是很常见的，这点和C语言不同，要适应一下
    ```
        * 要想对list中的元素用下标循环输出，可以用python内置的enumerate函数，将list变成索引-元素对

    ```python
    l=[1,2,3]
    for i,j in enumerate(l):
        print(i,j)
    #0 1
    #1 2
    #2 3
    ```
    * 列表生成式
        * 用简便的方法生成复杂的list
        * 比如说生成[1*1，2*2，3*3····]的一个list

    ```python
    l=list(range(0,10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #传统方法
    t=[]
    for i in l:
        t.append(i*i)
    t
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    #用列表生成式
    [i*i for i in l]
    #输出
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
        * 还可以有更多的玩法

    ```python
    [i*i for i in l if i%2==0]
    #用if条件只输出偶数的平方
    [i+j for i in 'ABC' for j in 'DEF']
    #输出
    ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    #用两重循环来进行全排列
    d={'x': 'A', 'y': 'B', 'z': 'C' }
    [k + '=' + v for k, v in d.items()]
    #输出
    ['y=B', 'x=A', 'z=C']
    #说明了for循环可以使用两个变量生list，但是要注意格式
    ```
        * 还可以用list元素的一些方法来制出特定的list

    ```python
    l=['A','B','C']
    [s.lower() for s in l]
    ['a','b,','c']
    #如果list中的元素不是纯的str就要在列表生成式后面加if语句
    #用isinstance(s,str)==True可以判断该s是否为字符
    ```
    * 生成器（generator）
        * 通过某种算法，将list中的元素推算出来，不必创建整个完整的list，节省大量的空间
        * 创建一个generator有两种方法
            1. 直接将列表生成式的`[]`换成`()`就是一个生成器了，取值时用`next()`语句取接下去的list元素值，但是这样太傻逼了，一般不用，只用for循环取值，因为generator也是可迭代对象

    ```python
    g=(i*i for i in range(10))
    #直接输g是不能取值的，传统next(g)一个一个输出
    #for循环给g迭代即可
    for i in g:
        print(i)
    #但是如果先用了next（）取值后再用for循环会得到不一样的结果
    ```
            2. 当算法很复杂时，用上面类似列表生成式的方法无法处理，则可以使用函数实现

    ```python
    #用定义函数方法求斐波那契数列
    def fib(num):
        n,a,b=0,0,1
        while n<num:
            print(b)
            a,b=b,a+b
            n=n+1
        return 'done'
    #在python中，可以用a,b=b,a+b这样的赋值方法，更加灵活
    #可以看出，fib中的数据也是有着算法可以推算出来的
    #因此只需将fib中的print（b）变成yield（b）
    #即可将此函数变成一个generator
    ···
    yield(b)
    ···
    ```
        * 需要注意的点
            * 一旦函数中有了关键字yield，这个函数就不再是函数了，而是一个generator
            * 函数顺序运行，运行到return或最后一句返回，而generator由next（）开始运行，每次遇到yield即停止，下一次再从上次的yield开始运行，所以我们一般用for循环而不会用next（）去输出值
            * 将函数改造成generator的缺点是无法获取return语句的返回值，只能捕获错误（还没学到）来获取返回值

    * 迭代器
        * 不如先说说可迭代对象和迭代器的区别
            * 前面已经知道list、tuple、dict、set、str、generator都是可迭代对象（Iterable），但是只有generator是迭代器（Iterator）
            * 迭代器可以被next()函数调用，并且不断返回下一个值
            * 迭代器和可迭代对象都可以用for循环
        * Iterator是个惰性计算的序列，因为内部已经给定了特定的算法，只需要用next()即可知道下一个输出是什么
        * 可以通过iter()函数将Iterable变成Iterator

    ```python
    >>> from collections import Iterator
    >>> isinstance(iter('abc'),Iterator)
    True
    #但是下面这样子就不行了
    isinstance(iter(str),Iterator)
    False
    #会报错说“type”类型的数据不是iterable
    #所有的数据类型的祖先都是“type”即元类
    #也就是说，python中万物皆对象
    ```
        * 其实for循环的原理也就是用了迭代器不断next()下一个值

    ```python
    for i in [1,2,3,4,5]:
        pass
    #等价于
    it=iter([1,2,3,4,5])
    while True:
        try:
            x=next(it)
        except StopIteration
            break
    ```

***

* 函数式编程
    * 概念简单来说就是：在编程语言中，越低级的语言，抽象程度就越低，执行效率就越高，反之，高级语言的抽象程度高，执行效率低。而函数式编程就是抽象程度很高的编程范式。
    * 函数式编程一个特点就是：允许把函数本身作为参数传入另一个函数，还允许返回一个函数！python允许使用变量，所以不是纯的函数式编程语言。
    * 高阶函数
        * 所谓高阶函数（higher-order function）并不是高等数学中的高阶函数，他的意思是`函数作为参数传入，这样的函数称为高阶函数`，其特点有三个：
            1. 变量可以指向函数
                * 就是说可以把函数赋值给一个变量，如`f=abs f(-1) #输出1`

            2. 函数名也是变量
                * 也就是说函数名也是可以当作变量，给别人赋值，可可以把原来的函数名看作指向一个特定的函数
                * eg:abs函数本来是绝对值函数，若赋予`abs=10`,再次调用abs(-1)时会报错，因为此时abs不再是绝对值函数，要想变成绝对值函数就得重新启动python解释器

            3. 传入函数
                * 一个函数接受另一个函数作为参数，举个栗子

    ```python
    def add(i,j,f):
        return f(i)+f(j)
    #调用
    add(-1,2,abs)
    #输出3
    ```

    * map/reduce
        * map是python内置的一个高阶函数，接受两个参数，一个是function函数，另一个是Iterable可迭代对象，map将函数作用于Iterable的每一个元素，并将结果作为一个新的Iterator返回

    ```python
    #原本的map既不是Iterable也不是Iterator
    #但是调用map之后，返回的却是一个Iterator
    from collections import Iterator
    from collections import Iterable
    isinstance(map,Iterator)
    False
    isinstance(map,Iterable)
    False
    r=map(abs,[-1.-2])
    #由于r是一个Iterator,所以不能够直接输出，要序列化或者用fo循环迭代
    list(r)
    [1,2]
    isinstance(r,Iterator)
    True
    ```
        * map可以用少量代码完成挺复杂的事情，比如将list中的int数据转化成str数据，map的强大不止于此

    ```python
    l=map(str,[1,2,3,4])
    list(l)
    ['1', '2', '3', '4']
    ```
        * reduce也是一个很强大的函数，它也接收两个参数，一个function函数，一个序列，此函数必须接收序列中的两个元素，并且把结果再和下一个元素做累计计算，总的来说就是相当于多次调用function函数`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`
        * 可以简单用一个例子来说明reduce的用法，将序列转化成int整数。（reduce函数在functools模块里，需要先引入才能用）

    ```python
    from functools import reduce
    def add(x,y):
        return x*10+y
    l=reduce(add,[1,2,3,4,5])
    l
    12345
    ```
    * filter(筛选函数)
        * python内置的高阶函数，和map一样接收两个参数，一个function，一个序列，返回一个Iterator。不同之处在于：filter将函数作用于序列每一个元素，若function的返回值为True，则保留该元素，若为False，则舍弃该元素，达到筛选的目的

    ```python
    def f(x):
        return x%2==0
    list(filter(f,[1,2,3,4,5,6]))
    #输出
    [2,4,6]
    ```
        * 做个练习题复习一下：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数

    ```python
    def f(x):
        return str(x)[::-1]==str(x)
    #切片知识回去看一下
    res=filter(f,range(1,1000))
    list(res)
    #就可以得出答案了
    ```
    * sorted(排序函数)
        * python内置的sorted()高阶函数可以对list进行排序
        * sorted后面可以接key函数，按照自己的意愿来排序

    ```python
    sorted([-1,2,4,8,-3,7])
    #要用list，因为sorted只针对list排序
    #输出
    [-3, -1, 2, 4, 7, 8]

    sorted([-1,2,4,8,-3,7],key=abs)
    #按绝对值大小排序，此时key函数为abs
    #输出
    [-1, 2, -3, 4, 7, 8]

    sorted([-1,2,4,8,-3,7],key=abs,reverse=True)
    #reverse布尔型参数，表示排序的正反
    ```
        * 给list中的str型元素排序，由于str比较的是字母ASCII码值，则需要一些key函数辅助，否则大写字母和小写字母的混合排序会杂乱

    ```python
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
    #此时就按照了首字母小写的顺序来排序了
    #输出
    ['about', 'bob', 'Credit', 'Zoo']
    ```
    * 返回函数
        * 函数作为一个函数的返回值，就是在函数的内部再定义一个函数，调用外部函数时，得到的不是计算值，而是一个函数，再调用一次外部函数时才能得到值。这种结构称为`闭包`，十分强大，意义就在于可以不用马上得出结果。

    ```python
    #举个栗子，做一个返回自定义求和函数的function
    def lazy_sum(*arg):
    #可以看到里面定义的sum函数是没有参数的，用的是外部函数的而参数
        def sum():
            x=0
            for i in arg:
                x=x+i
            return x
        return sum
    #调用外部lazy_sum函数
    lazy_sum(1,2,3,4)
    #输出来的是一个函数
    <function __main__.lazy_sum.<locals>.sum>
    #再次调用lazy_sum函数才能得到值
     lazy_sum(1,2,3,4)()
     #输出10
    ```
        * 闭包也就是说内部函数引用了外部函数的局部变量和参数，再返回内部函数时，相关变量和参数都保存在返回的函数中，要注意一点，每次调用外部函数都会返回一个新的函数，即使传入的参数一样，得到的结果也不一样

    ```python
    #拿上一题做栗子
    f1=lazy_sum(1,2,3,4)
    f2=lazy_sum(1,2,3,4)
    f1==f2
    #输出
    False
    ```
        * ***还有一题不会，先放在这*************************

    * 匿名函数（lambda）
        * 用匿名函数是为了减少代码量，有时不用把函数的显式写出来，就写个匿名的就足够了
        * 表达式为`lambda x:y`，x表示为匿名函数的参数，y表示返回值，lambda函数只能写一个表达式，所以功能也有限，只在特定的地方用到lambda，而且lambda也可以作为返回函数被函数返回

    ```python
    def sum(x,y):
        return lambda :x+y

    ```
    * 装饰器(decorator)
        * 意义就在函数运行过程动态增加函数功能，而不改变函数的主体内容
        * 装饰器本质上就是一个`返回函数`的高阶函数，所以一般要先定义这个decorator才能把他的效果给其他的函数，使用时在函数的定义处加上`@`decorator

    ```python
    def deco(fun):
        def wrap(*args,**kw):
            print('%s' % fun.__name__)
            return fun(*args,**kw)
        return wrap
    #以上是定义了一个decorator，先打印text内容再调用fun参数
    @deco
    def demo():
        print('hello,world')
    #将@deco放在函数的定义处，相当于demo=deco(demo)
    ```
        * 但是这样子有一个很大的缺点，定义的函数的名字被改变了，这样的话一些依赖函数名的代码运行起来会出错，所以functools.wraps可以帮助我们把他的名字改过来

    ```python
    #如上一个例题的函数
    now.__name__
    wrap
    #原本应该是now的，被decorator调用后就变成了返回的wrap函数了
    #所以正确的定义decorator的方法应该是
    import functools
    def deco(fun):
        @functools.wraps(fun)
        #只需要加上这么一段就行了
        def wrap(*args,**kw):
            print('%s' % fun.__name__)
            return fun(*args,**kw)
        return wrap
    ```
        * 有时候decorator自己要传参数，所以要定义一个三层嵌套的decorator

    ```python
    #廖老师的例子
    import functools
    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    #调用时
    @log('debug')
    def now():
        print('HelloWorld')
    #相当于是now=log('debug')(now)
    #传入debug作为log的参数，返回decorator函数
    #将now作为参数继续传入，最终返回wrapper函数
    now.__name__
    now
    #这回就没有改变了
    ```
    * 偏函数
        * 有时候要改变函数的默认参数，便可用functools里的partial来实现

    ```python
    #int()函数可以将str转化为int，其实他还有个base参数可以传入为规定的进制数，默认下是10
    #下面用partial将其二进制数大量转化为十进制
    import functools
    int2=functools.partial(int,base=2)
    int2('110')
    6
    #当然，也可以在int2的参数中传入base的其他值
    int2('110',base=10)
    110
    ```

***

* 模块
    * 模块的使用方便了代码的编写，写完一个模块之后直接导入即可，减少了代码量。并且也防止了函数名及变量的冲突，相同的函数名和变量名可以存放在不同的模块中
    * 为了防止模块名冲突，python引入了包(package)的概念，package里面存放着模块，只要package不重名，模块名重复了也没事
    * 自定义一个模块
        * 以python内建的sys模块为例，编写一个hello模块，给出标准的模板

    ```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    ' a test module '
    __author__ = 'Michael Liao'
    import sys
    def test():
        args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

    if __name__=='__main__':
        test()
    #第一行的注释意思是在Linux/MacOS/Unix系统上可以直接运行该py程序
    #第二行指明了是utf-8编码
    #第三行是对模块的说明，模块的第一行字符串都视为说明部分
    #特殊变量__author__是代表开发者的名字
    #一二三四行就是标准的模板所需要的内容,不写也没事，最好写上
    #当我们在命令行运行hello模块时，解释器会把特殊变量__name__置为__main__
    #在其他环境运行if语句将判断失败，因此这种写法最常见做运行测试
    ```
    * 作用域
        * 在一个模块中，有些变量和函数我们只希望在模块内部（private）使用而不让外部（public）使用，那么可以在函数和变量前加_或者__
        * `__xx__`这种是可以直接引用的，但是是特殊变量，有特殊作用，自己定义的时候不要这样定义
        * 但是要注意，python没有方法阻止用户访问private变量和函数，一切全靠自觉
        * 用了private变量和函数后，只需在模块中公开public函数，而不需要知道内部的代码逻辑，这是一种代码封装方法

***

* 面向对象编程(object oriented programming)
    * 概念：python中，万物都是对象，与传统的面向过程编程不同，这个把所有东西都视作一个对象，python有自带的对象如str、list、tuple等，也可以自定义对象，自定义的对象叫做类(class)，面向对象编程就是将对象作为程序的基本单元，每一个对象都包含数据以及操作数据的函数。
    * 面向对象的程序设计把计算机程序视为一组对象的集合， 而每个对象都可以接收其他对象发过来的消息， 并处理这
    些消息， 计算机程序的执行就是一系列消息在各个对象之间传递。
    * 举个例子，来描述一下面向过程和面向对象的实现方法的不同
        * 题目：打印两个学生的名字和成绩
        * 面向过程：

    ```python
    std1 = { 'name': 'Michael', 'score': 98 }
    std2 = { 'name': 'Bob', 'score': 81 }
    def print_score(std):
        print('%s: %s' % (std['name'], std['score']))
    ```

        * 面向对象：

    ```python
    class Student(object):
        def __init__(self, name, score):
            self.name = name
            self.score = score
        def print_score(self):
            print('%s: %s' % (self.name, self.score))
    ```
        * 可以看出，面向对象时，首先把学生看成一个对象(类)，这个对象拥有姓名(name)和分数(score)两个属性(property)，所以应该先创建出student对应的对象，再用对象包含的函数(称之为方法Method)将自己的数据打印出来。

    ```python
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()
    ```

    * 类(class)和实例(instance)
        * 类名一般首字母要大写，然后类名紧跟着(xx),表示这个类是从xx类继承而来的，没有合适的继承则直接用`(object)`,这是所有的类都会最终继承的类
        * 如果定义的类没有绑定属性的话，则创建实例时可以给实例传入空参数，若是使用了`__init__`方法绑定了属性的话，则创建实例时不能够传入空参数，要传入相应__init__的属性。
        * 类可以认为是创建实例的模板，而每个实例又拥有不同的数据，彼此之间独立。

    ```python
    # 定义一个没有绑定属性的类
    class Student(object):
        pass
    # 创建该实例时不传入参数
    Bob = Student()
    # 定义一个绑定属性的类
    class Student(object):
        def __init__(self,name,score):
            self.name = name
            self.score = score
    # 创建实例
    Bob = Student('Bob John', '100')
    Bob.name
    'Bob John'
    ```

        * `__init__`方法的第一个参数永远是self(本身)，所以可以将类的所有的属性全都绑定到该方法中，因为这个方法就指向了实例本身。
        * 其实类的方法和普通的函数没有什么不同，一样可以传入关键字参数、默认参数、可变参数等等，只是调用时不用传入`self`参数。

    * 类的封装
        * 上述例子中，Student类


***

* 错误、调试和测试
    * 错误处理
        * python中内置一套`try...except...finally`的捕获错误的机制，当觉得某句代码会出错时，放在try后面试一下，若有错则会运行except后面的内容，finally可要可不要，具体用法如下：

    ```python
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')
    ```
        * 需要注意的是，错误有很多种，若发生了多个不同的错误，则需要用多个except语句来处理，并且如果没有错误的话可以在except后面加上else语句，没有错误时会自动执行else语句
        * python里的错误也是一个class，所以except会捕获该错误以及他的子类，导致后面的except捕获不到错误，并且所有的并且所有的错误都是由BaseException类派生的
        * try...except...finally是个十分好的错误捕获语句，还可以跨越多层使用，不用到最底层去捕获错误
        * 如果错误没有被捕获的话，最终会被python解释器捕获，并且打印一个错误信息，要看得懂哪里出了错误才能去排查
    * 抛出错误
        * 捕获错误就是捕获到一个class，所以python中有许多的函数会抛出错误，同样，我们也可以定义一个class作为错误抛出，但是一般不要用自己定义的，用自带的错误class就可以了
        * 通常有另外一种抛出错误的方法如下

    ```python
    def foo(s):
        n = int(s)
            if n==0:
        raise ValueError('invalid value: %s' % s)
        return 10 / n
    def bar():
        try:
            foo('0')
        except ValueError as e:
            print('ValueError!')
            raise
    bar()
    #这种方法是很常见的，虽然已经打印了一个valueerror
    #但是再加一个raise的话就会抛出当前错误的原样
    #并且，在except中raise一个错误，还可以把这个错误转化成另一种类型的错误（逻辑符合即可）
    ```
    * 调试
        * 当程序运行出错时，要进行调试判断问题出在哪里，有下面几个方法
        1. 简单粗暴，直接把可能出问题的变量打印出来（print）
        2. 用多了print会使得输出很混乱，所以，凡是用到print的地方都可以用assert代替，这种方法叫做`断言`

    ```python
    def foo(s):
        n = int(s)
        assert n != 0, 'n is zero!'
        return 10 / n
    def main():
        foo('0')
    main()
    #这就是断言，他认为n!=0一定是True，否则逻辑就会错误
    #若前面为False，则assert会抛出assertion error，说'n is zero'
    ```
        3. 把print替换成logging，这是比print和assert都更加有效的方法，他不会抛出错误，并且可以输出到文件

    ```python
    import logging
    logging.basicConfig(level=logging.INFO)
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)
    #loging允许你指定记录信息的级别，有debbug,warning,error,info四个级别
    #当level=INFO时，logging.debug等就不起作用了，很方便
    ```
        4. 用pdb模块
            * 导入pdb后在可能出错的地方用pdb.set_trace()就可以设置一个断点，程序运行到这里会进入pdb调试环境
            * 进入pdb环境后用p指令可以查看变量的值，用c指令可以退出pdb继续运行程序

    ```python
    import pdb
    s = '0'
    n = int(s)
    pdb.set_trace() # 运行到这里会自动暂停
    print(10 / n)
    #下面是运行结果
    (Pdb) p n
    0
    (Pdb) c
    Traceback (most recent call last):
    File "xx.py", line 7, in <module>
    print(10 / n)
    ZeroDivisionError: division by zero
    ```

        5. 想要更加方便设置断点和单步执行时，可以用pycharm这个IDE，但是廖老师说logging才是最屌的

    * 单元测试
    * 文档测试（单元测试以及文档测试应该暂时用不到，有需要再学习）

***

* IO编程
    * 读文件
        * 读取文件之前首先得把这个文件给打开。用open语句可以打开一个已有的文件，若没有的话则会报错，并且每次open完了之后还得调用close函数，不然会占用操作系统的资源

    ```python
    f = open('/Users/michael/test.txt', 'r')
    ```
        * 上述例子后面的`r`表示以什么方式打开，`r`则是只读，所以如果打开的是一个不存在的文件就会报错，如果写的是`w`，则是可写，这时候如果文件不存在的话系统就会新建一个空文件，不会报错，类似的还有很多打开方式，自己去查。
        * 前面的路径推荐写相对路径，方便在不同的设备上运行。
        * 打开了文件之后就要读取文件了，用read方法执行读取操作。

    ```python
    f.read()
    f.close() # 每次记得在最后面关闭文件！！
    ```
        * 上述方法每次都要open然后close，一旦open方法出现了IO错误，后面的close方法就不会起作用，所以可以用`try...finally`语句来执行close，但是这也太麻烦了吧，所以python还有个更为简便的方法，让我们自动的调用close()，那就是`with`语句

    ```python
    with open('/path/to/file', 'r') as f:
        print(f.read())
        # 这就话就直接包括了close()
    ```
        * 说一下读取文件内容的各种方式
            * `read`一次性读取所有的内容，对大文件最好不用，可能会使内存爆炸。
            * `read(size)`方法每次最多读取size个字节的内容，可以反复调用知道文件全部被读取完成。
            * `readline`每次读取一行内容，`readlines`一次读取所有行，返回一个list，适用于对配置文件额度读取，用readlines输出时可以使用一个for循环，然后对每一行使用`strip()`将空格和换行符去除，方便查看。
            * 但是要注意，一定要在with语句结束之前读取，否则要是在他结束后在读就会出错，因为那时文件已经被关闭了。
        * file-like Object
            * 只要能用open方法打开，并且能返回read方法的对象都叫做`file-like Object`，上面的例子都是读取用UTF-8编码的文本文件，其实除了这个还可以对其他的file-like Object执行读写操作。
            * 二进制文件读取
                * 就是将上面读写文本文件的`r`改成`rb`，`b`表示的就是`binary`

    ```python
    f = open('/Users/michael/test.jpg', 'rb')
    f.read()
    b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # # 十六进制表示的字节
    ```
            * 读取非UTF-8编码的文本文件
                * 就是在open里面给一个`encoding`参数，例如`encoing = 'gbk'`。
                * 如果文件中还夹杂了一些非法编码的字符，则可能会发生`UnicodeDecodeError`，提示解码错误，最简单的处理办法就是忽略他，在open函数中加上`error = 'ignore'`。

    * 写文件
        * 写文件的话跟上面读取文件是一样的，也要先open再close，所以还是用with语句方便。
        * 写入文件时，open的参数就要变成`w`了，但是注意，`w`会将原有的内容给覆盖掉，因此，如果要追加写入的话就得用`a`，`a`就表示追加模式。
        * 同样也可以指定写入数据的编码格式，与上文一样。

    * StringIO和BytesIO
        * 上面说的是对文件(在硬盘中)的读写，其实也可以在内存中进行读写。
        * StringIO就是在内存中进行str的读写，Bytes就是在内存中操作二进制数据。
        * 这两个了解一下就好，暂时不会涉及到。

    * 操作文件和目录
        * 这一小节讲的是python内置的os模块操作文件目录
        * `os.name()`函数查看当前系统的名称，`os.environ()`函数查看系统环境变量的值，返回一个list，想获取某个环境变量的值可以用`os.environ.get('key')`。
        * 操作目录：
            * `os.path.abspath('.')`查看当前目录的绝对路径，`.`就表示的是`当前`，也可以填别的目录，相对路径则是`os.path.relpath('dir','start dir')`，注意要填上`startdir`，不然程序不知道是相对谁的相对路径。
            * `os.mkdir('dir')`就创建了一个新目录，同样，用`os.rmdir('dir')`可以删除某个目录。
            * `os.path.split()`可以将路径拆分，返回一个tuple，`os.path.splitext()`以tuple形式返回文件的拓展名，这个有什么用呢，待会儿再讲。

    ```python
    os.path.split('/Users/michael/testdir/file.txt')
    # 下面是返回的结果
    ('/Users/michael/testdir', 'file.txt')

    os.path.splitext('/path/to/file.txt')
    # 下面是返回的结果
    ('/path/to/file', '.txt')     
    ```

        * 操作文件
            * `os.rename('former','latter')`给文件重命名。
            * `os.remove('file')`函数删除该文件,和`os.rmdir()`不同，那是删除一个目录，这是删除一个文件。
            * 下面用两个列表生成器展示一行代码过滤出当前目录下的所有目录和所有的py文件

    ```python
    [x for x in os.listdir('.') if os.path.isdir(x)]
    # ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
    [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
    # ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
    ```

        * os就先讲这么多，注意有些函数是在os里面，有些是在os.path里面，用的时候要注意，更多的内容可以去参考官方文档。

    * 序列化
        * 在程序运行时，所有变量都是在内存中而不是在硬盘里，结束后内存会被回收。所以将变量从内存中变成可传输或者可储存的过程就叫做序列化，在python中叫做picking，js中叫做serialization，都是一样的意思，目的就是让数据能够被写入文件，也有反序列化unpicking，就是将序列化后的内容重新读取到内存中。
        * python的内置`pickle`模块提供了序列化功能

    ```python
    import pickle
    d = dict(name='Bob', age=20, score=88)
    pickle.dumps(d)
    # 或者也可以这样写
    f = open('text.txt','wb')
    pickle.dump(d,f)
    f.close()
    ```

        * pickle的dumps方法直接将任意对象序列化为一个bytes，然后可以直接将其写入文件，而pickle的dump方法则是将对象序列化后写入一个`file-like Object`中。
        * 然后如果从文件中读取到内存中时，先将文件读取到一个bytes，再用pickle.load()或者pickle.loads()方法来反序列化保存的对象。

    ```python
    f= open('tet.txt','rb')
    d = pickle.load(f)
    f.close()
    # 输出结果就是刚刚的对象
    {'age': 20, 'score': 88, 'name': 'Bob'}
    ```

        * JSON
            * 上面写的pickle的兼容性很低，所以一般只用来保存一些不重要的数据，一般在不同的编程语言中传递数据的话就必须将对象序列化为标准的格式，现在普遍用的都是`JSON`，它表示出来的就是一个`字符串`，可以被所有语言读取。
            * python内置json模块可以很快速的将dict数据转化成json数据

        ```python
        import json
        d = dict(name='Bob', age=20, score=88)
        json.dumps(d)
        # 输出即是一个json类型数据，注意它是一个字符串
        '{"age": 20, "score": 88, "name": "Bob"}'
        ```

            * 和pickle一样，序列化和反序列化的方法都是dump、dumps、load、loads。

        ```python
        json_str = '{"age": 20, "score": 88, "name": "Bob"}'
        json.loads(json_str)
        # 输出结果为python的dict
        {'age': 20, 'score': 88, 'name': 'Bob'}
        ```
            * 除了dict以外，我们也经常使用class(类)来表示一个对象，这样也可以很方便的序列化，但是如果直接像前面那样写的话会出现报错，因为dumps方法不知道如何将一个类的实例转化成一个json。
            * 可以查看dumps的文档，在dumps里面加上一个参数`default=lambda obj: obj.__dict__`，这样子的话就可以把class的实例转化成一个dict数据，至于接下去该怎么做，还是依然用dump或者load方法来序列或者反序列，有需要的话可以去查json模块的文档。
