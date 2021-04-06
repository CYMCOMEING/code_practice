[TOC]

# 目录
在文件开头输入下面的标记自动显示目录
```markdown
[TOC]
```

# 标题
在想要设置为标题的文字前面加#来表示，#和文字之间有一个空格，可表示1-6级标题。
```markdown
# 一级标题
## 二级标题
### 三级标题
```


# 字体

* **斜体**  
    在文字左右两侧分别用一个*号包起来
* **加粗**  
    在文字左右两侧分别用两个*号包起来
* **斜体加粗**  
    在文字左右两侧分别用三个*号包起来
* **删除线**  
    在文字左右两侧分别用两个~~号包起来
* **高亮**  
    在文字左右两侧分别用两个==号包起来

```markdown
*这是倾斜的文字*
**这是加粗的文字**
***这是斜体加粗的文字***
~~这是加删除线的文字~~
==这是高亮的文字==
```  
*这是倾斜的文字*  
**这是加粗的文字**  
***这是斜体加粗的文字***  
~~这是加删除线的文字~~  
==这是高亮的文字==  

# 引用  
在引用的文字前面加>即可。注意>和文件之间有空格。
```markdown
> 引用的内容
>> 引用的内容
>>>>> 引用的内容
```  
> 引用的内容
>> 引用的内容
>>>>> 引用的内容


# 列表  
* **无序列表**  
在文字前面加+ - *其中一种都可以  
* **有序列表**  
数字加点
* **列表嵌套**  
下一级前面加三个空格，为了工整对齐建议加4个空格
* **列表嵌套桥台**  
```markdown
* 列表内容
    1. 嵌套内容
    2. 嵌套内容
    3. 嵌套内容
* 列表内容
    * 嵌套内容
    * 嵌套内容
    * 嵌套内容
* 列表内容
```

# 任务列表
```markdown
- [ ] 任务一
- [ ] 任务二
- [x] 任务三
```

- [ ] 任务一
- [ ] 任务二
- [x] 任务三


# 表格
* 第二行分割表头和内容。  
* 文字默认居左
* 两边加：表示文字居中
* 右边加：表示文字居右
```markdown
表头|表头|表头|表头
---|:--:|:--:|---
内容|内容|内容|内容
内容|内容|内容|内容
```

# 链接  
```markdown
文字链接 [link](https://)
网址链接 <http://>
```  

# 图片  
链接前面加 ! 即可显示图片
```markdown
![image](https://)
![image](https:// "提示文字"){height=30%}
```  
有道云还没有办法指定图片的宽高，但是可以用html的<img>标签
```html
<img src="https://" width = "100" height = "100" alt="图片" />
```
![image](https://www.baidu.com/img/flexible/logo/pc/result.png "百度")

# 单行代码
用一个反引号把代码包起来
```markdown
`code`
```  

# 代码块
用三个反引号把代码包起来，反引号要独占一行  
或者也可以使用4空格缩进
```markdown
    ```
    代码
    ```
```  
显示某个语言的代码高亮
```markdown
    ```java
    代码
    ```
```
如果不需要代码高亮,可以使用
```markdown
    ```nohighlight
    代码
    ```
```
显示数学公式
```markdown
    ```math
    E = mc^2
    
    x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
    ```
```
```math
E = mc^2

x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
```
森么[sdsdf](ddddd)

# 注释
**语法：**  
待解释文字[^脚注 id]  
[^脚注 id]:注释内容  

**注意事项:**  
脚注 id 必须唯一  
无论脚注 id 如何起名，显示时一律标为数字，并且按出现顺序排列  
```markdown
Markdown[^mark]
[^mark]: 《Markdown让文字更加精致》
```

# 空格
```xml
&ensp;或&#8194; //半角
&emsp;或&#8195; //全角
&nbsp;或&#160;
```

# 换行符  
```
<br>
<br/>
<br />
```
也可以后面加两个空格实现换行

# 两端文字之间增加空行
输入两个换行。

# 分割线  
输入三个或以上的-或者*都可以

# 符号转义
如果需要用到markdown的符号，可以在符号前面加\，是符号不被转义

# 支持html
```markdown
<html>
<!--在这里插入内容-->
</html>
```

# 强制分页
```
<div STYLE="page-break-after:always;"></div>
```
在预览不能看到效果，但是输出pdf时会实现分页（待验证）

# 流程图

## 方向的值  
* TB 从上到下  
* BT 从下到上  
* RL 从右到左  
* LR 从左到右  
* TD同TB  

## 基本图形
* id + [文字描述]矩形
* id + (文字描述)圆角矩形
* id + [文字描述]不对称的矩形
* id + {文字描述}菱形
* id + ((文字描述))圆形

## 节点之间的连接
* A --> B  A带箭头指向B
* A --- B  A不带箭头指向B
* A -.- B  A用虚线指向B
* A -.-> B  A用带箭头的虚线指向B
* A ==> B  A用加粗的箭头指向B
* A -- 描述 --- B  A不带箭头指向B并在中间加上文字描述
* A -- 描述 --> B  A带箭头指向B并在中间加上文字描述
* A -. 描述 .-> B  A用带箭头的虚线指向B并在中间加上文字描述
* A == 描述 ==> B  A用加粗的箭头指向B并在中间加上文字描述

## 子流程图
格式，在graph下添加
```
subgraph 标题
    a --> b
end
```
```
graph LR
    start[开始] --> stop[结束]
    
    subgraph 子流程
        a --> b
    end
```

## 自定义样式
```

graph LR
    id1(Start)-->id2(Stop)
    style id1 fill:#f9f,stroke:#333,stroke-width:4px,fill-opacity:0.5
    style id2 fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 10,5
```
```
graph LR
    id1(Start)-->id2(Stop)
    style id1 fill:#f9f,stroke:#333,stroke-width:4px,fill-opacity:0.5
    style id2 fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 10,5
```

## demo
绘制一个流程图,找出 A、 B、 C 三个数中最大的一个数。
```

graph LR
    start[开始] --> input[输入A,B,C]
    input --> conditionA{A是否大于B}
    conditionA -- YES --> conditionC{A是否大于C}
    conditionA -- NO --> conditionB{B是否大于C}
    conditionC -- YES --> printA[输出A]
    conditionC -- NO --> printC[输出C]
    conditionB -- YES --> printB[输出B]
    conditionB -- NO --> printC[输出C]
    printA --> stop[结束]
    printC --> stop
    printB --> stop
```

```
graph LR
    start[开始] --> input[输入A,B,C]
    input --> conditionA{A是否大于B}
    conditionA -- YES --> conditionC{A是否大于C}
    conditionA -- NO --> conditionB{B是否大于C}
    conditionC -- YES --> printA[输出A]
    conditionC -- NO --> printC[输出C]
    conditionB -- YES --> printB[输出B]
    conditionB -- NO --> printC[输出C]
    printA --> stop[结束]
    printC --> stop
    printB --> stop
```

# 甘特图工具
需要在\`\`\`里面写，以gantt开头。  
ateFormat YYYY-MM-DD  规定了时间轴  
title （标题文本）表示甘特图标题。  
[点击查看更详细甘特图语法](http://knsv.github.io/mermaid/#styling39)
```markdown

gantt
dateFormat YYYY-MM-DD
title 产品开发计划表
section 初期阶段  
明确需求:2017-04-11,10d
section 中期阶段  
跟进开发:2017-04-22,10d
section 后期阶段  
走查测试:2017-05-03,20d
```
```
gantt
dateFormat YYYY-MM-DD
title 产品开发计划表
section 初期阶段
明确需求: 2017-04-11,10d
section 中期阶段
跟进开发: 2017-04-22,10d
section 后期阶段
走查测试: 2017-05-03,20d
```

