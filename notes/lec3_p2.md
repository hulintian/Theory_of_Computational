# Chapter2 上下文无关文法

## CFG

> 上下文无关文法（CFG）
>
> CFG的语言：G1 ：文法生成的所有字符串的集合
> CFG的语言：通过派生得到仅有总结的集合

- 替换规则

- example:

$$
\begin{align*}
A & \rightarrow 0A1 \\
A & \rightarrow B \\
B & \rightarrow \# \\
\end{align*}
$$

- 上面的CFG
  - 变量: AB
  - 终结符: 0,1,#
  - 起始变元: A
  - 箭头左侧只有一个变量

- why context free?
  - 每个替换规则左边只有一个变元，替换只跟左边的有关

- 数学上的定义
  - 4-tuple

  $$
    \begin{align*}
    (V, \Sigma, R, S) \\
    V &: variable\\
    \Sigma &: terminals\\
    R &: repalce rule \\
    S &: start\\
    \end{align*}
  $$

- 派生（双横线的箭头$\Rightarrow$）

### 设计CFG

- example:
$$
B = \{0^{n}1^{n}| n \ge 0\} \\ solution:
\begin{align*}
S \rightarrow 0S1 | \epsilon
\end{align*}
$$

- 如何表示两个CFG的并？
  - example:

$$
B = \{0^{n}1^{n}| n \ge 0\} \cup \{1^{n}0^{n}| n \ge 0\} \\
\begin{align*}
solution: S & \rightarrow S_{1} | S_{2} \\
S_{1} & \rightarrow 0S_{1}1 | \epsilon \\
S_{2} & \rightarrow 0S_{2}1 | \epsilon
\end{align*}
$$

- 任何正则语言可以由CFG描述
  - 如果  $\delta(q_i,a) = q_j$，add rule: $V_i \rightarrow aV_j$
  - ...

### 歧义性
