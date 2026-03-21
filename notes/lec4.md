# Chapter2 上下文无关文法

> CFG & PDA

### 歧义性

- 一句话能给出两种解释

- example
$$
S \rightarrow S + S | S * S | a
$$
> $a + a * a$ 能通过两种方式生成，歧义
>> 如何形式化的描述歧义？如何说生成的两个语法树是不同的？\
>> 简单的看：两个不同的推导过程？不同推导过程，语法树有可能是一颗。提出**最左派生**

- 最左派生：每次替换最左边剩下的变元
- 歧义：CFG G 有两个以不同的最左派生
- 固有歧义：CFG language 只能有

### Chomsky normal form

- 规范（标准的）：
  1. 一个变元产生两个变元
  2. 一个变元产生一个终结符
  - 允许 $S \rightarrow \epsilon$ 起始变元产生空串
  - S 不能在右边

- 程序化的转换（6步）
  1. step1: 增加新的起始变元 $S_{0}$ 和 规则 $S_{0} \rightarrow S$ 
  > 避免S出现在推导右边的情况
  2. step2: 删除 所有 $A\rightarrow \epsilon$ 规则
  3. step3: 考虑单元产生式 $A \rightarrow B$
  4. step4: 考虑 $A \rightarrow u_{1}u_{2}\dots u_{k}$，其中 $k \gt 2$ 且 $u_{i}$ 是变量或终结符，替换 
  $$
  A \rightarrow u_{1}A_{1} , A_1 \rightarrow u_2A_2 , \dots 
  $$

> n叉树 -> 2叉树 ？

## 下推自动机

> PDA Pushdown automata 能力与CFG等价，CFG的机器模型
>
> PDA = NFA + Stack (inf storage) \
> 输入带：只读 \
> 有限控制器 \
> 下推栈：保存无限信息 \
> 只读头、可读可写头 \
> 说明：
> 1. 只有非确定PDA才与CFG等价
> 2. 只能从前到后读一遍输入带
> 3. 可以在栈里写输入字符以外的辅助字符
> 4. 只能在栈顶读写
> 5. 读一个栈顶字符意味着将其从栈顶弹出

- PDA Def: 6-tuple 
$$
M = (Q, \Sigma, \Gamma, \delta, q_{0}, F)
$$

- 其中 $\Gamma$ 是栈字母表
- $\delta: Q\times \Sigma_{\epsilon} \times \Gamma_{\epsilon} \rightarrow P(Q \times \Gamma_{\epsilon})$

> 从栈里读，栈顶符号写在最右边

- 通常约定：
    1. 头几个小写字母


- 下推自动机停留在接受状态，就接受

- 不确定性：magic guess
