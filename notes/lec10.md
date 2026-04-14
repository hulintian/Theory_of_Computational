# 高级定理

## 递归定理

> 在任何图灵机中得到自己的编码

- TM to write TM

1. 存在可计算函数，q(w)，q(w)打印w，然后停机

> 不能循环定义：

- 程序打印自己的代码
- 程序打印自己的代码，然后显示在屏幕上

- defn: $MIN_{TM}$
- $MIN_{TM}$是不可识别的

## Turing规约

$$A \le B$$
- exists a solution for B can use to solve A

- oracle，喻示，一个装置判定字符串是否属于语言
> 不是魔法

- A图灵可规约，有个装置能够喻示B（$M^{B}$），然后来构造A的判定器。
$$A \le_{T} B$$
