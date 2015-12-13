# StudyMakeDown

标签（空格分隔）： 未分类

---

在此输入正文123
$x^{y^z}=(1+{\rm e}^x)^{-2xy^w}$

【标题】
类Atx形式：
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
# 注：#和「一级标题」之间建议保留一个字符的空格（其他类似），这是最标准的 Markdown 写法。

类Setext形式：
利用 =（最高阶标题）和 -（第二阶标题）
This is an H1
==
This is an H2
---------

【列表】
- 文本1
- 文本2
- 文本3
1. 文本1
2. 文本2
3. 文本3
4. 文本4

【插入链接】
语法： [显示文本](链接地址)
[简书](http://jianshu.io)
[你好sdfds](http://www.baidu.com)
你好sdfds(http://www.baidu.com)

This is [an example](http://example.com/   "Titleabc")
inline link.[This link](http://example.net/) has no title attribute.

This is [an example] [id] reference-style link.
[id]: http://www.baidu.com/ "Optional Title Here1"
[id]: <http://www.baidu.com/> "Optional Title Here2"

[Google][]
[Google]: http://google.com/

Visit [Daring Fireball][] for more information.
[Daring Fireball]: http://daringfireball.net/

I get 10 times more traffic from [Google] [1] than from[Yahoo] [2] or [MSN] [3].
[1]: http://google.com/ "Google"
[2]: http://search.yahoo.com/ "Yahoo Search"
[3]: http://search.msn.com/ "MSN Search"

I get 10 times more traffic from [Google][] than from[Yahoo][] or [MSN][].
[google]: http://google.com/ "Google"
[yahoo]: http://search.yahoo.com/ "Yahoo Search"
[msn]: http://search.msn.com/ "MSN Search"

自动链接
<http://www.163.com/>
<address@example.com>

【插入图片】
语法：! [显示文本](图片链接地址)
![你好打算发sdfdssdfdsf](http://upload-images.jianshu.io/upload_images/1331049-dda207980f6f49f2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 注：插入图片的语法和链接的语法很像，只是前面多了一个！

![Alt text](http://upload-images.jianshu.io/upload_images/1331049-3dfb46edc0b1021c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Alt text123456](http://ww2.sinaimg.cn/bmiddle/615fb632jw1eyy3r1qo2oj20m80veac2.jpg   "Optional titledfd")

![Alt text阿斯顿][id]
sdfdsgsdgsdgdsgsdgdsd
大范甘迪发郭德纲都发生过

[id]: http://ww4.sinaimg.cn/bmiddle/aa397b7fjw1dzplsgpdw5j.jpg "Optional title attribute"



【引用】
你只需要在你希望引用的文字前面加上 >就好了
> 一盏灯， 一片昏黄； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。

【斜体与粗体】
*一盏灯*， **一片昏黄**； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。

*single asterisks*
_single underscores_
**double asterisks**
__double underscores__

【反斜杠】
\*this text is surrounded by literal asterisks\*
\_this text is surrounded by literal asterisks\_
Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：
\\   反斜线
\`   反引号
\*   星号
\_   底线
\{\}  花括号
\[\]  方括号
\(\)  括弧
\#   井字号
\+   加号
\-   减号
\.   英文句点
\!   惊叹号

【代码】
如果要标记一小段行内代码，你可以用反引号把它包起来
Use the `printf()` function.
``There is a literal backtick (`) here.``

A single backtick in a code span: `` ` ``
A backtick-delimited string in a code span: `` `foo` ``

插入HTML原始码：
Please don't use any `<blink>` tags.
`&#8212;` is the decimal-encoded equivalent of `&mdash;`.

【分割线】

--------
***
**********


【表格】【原生markdown不支持这样的表格，扩展的markdown才可能支持】
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | 1600 |
| col 2 is      | centered      | 12   |
| zebra stripes | are neat      | 1    |


