### 线性界限自动机 LBA

> 给有限的纸带

- $A_{LBA}$是可判定的

- LEMMA5.8 设M是有q个状态和g个带符号的LBA。对于长度为n的带子，M有 $qng^{n}$ 个格局

> LBA 陷入循环能用 TM判定出来

- $E_{LBA}$是不可判定的，规约到 $A_{TM}$
  - assume TM R decides $E_{LBA}$, construct $A_{TM}$ TM S

- $ALL_{CFG}$是不可判定的
- $EQ_{CFG}$是不可判定问题

> read5.2 PCP

## 映射可规约性

$A \le B$：假设B有解，则A有解
> 在这节前面的规约称为图灵规约，映射规约更严格

- 问题A映射规约为B,记为$A \le_{m} B$ 如果：

$\exists f: \Sigma^{*} \rightarrow \Sigma^{*} $

> 存在一个可计算函数，把A中的字符串，转换成一个在B中的字符串

- 可计算函数

- 推理：$A\le_{m}B \Rightarrow \bar{A} \le_{m} \bar{B}$
