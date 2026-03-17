> 形式化的解答计算机科学的基本问题。
>
> Turn Machine

## symbols

- Alphabet
- String
- String over alphabet S
- Length of string w : |w|
- Empty string
  - string of length 0 $\epsilon$

- substring, reverse (origin: $w$, reverse $w^{R}$), language (set of string)

## Homework of Chapter 0

0.1\0.2\0.5\0.6\0.9\0.10\0.11

# Chapter 1 正则语言

> regular language

## 有穷自动机 Finite Automaton (FA)

- DFA、NFA
  - 用于控制
  - 用于识别
  - 不同的视角

``` dot
digraph G {
    state

    init [shape=point]

    accept [shape=doublecircle]
}
```

- define:
$$
(Q, \Sigma, \delta, q_{0}, F) \\
Q: 状态的集合(有穷) \\
\Sigma: 字母表 \\
\delta :  Q \times \Sigma \rightarrow  Q  状态转移函数 \\ 
q_{0} 初始状态\\
F \subseteq Q 接受状态
$$

- 接受的定义：机器M接受的全部字符串A， L(M) = A

- 计算的形式化定义：
$$
set M = (Q, \Sigma, \delta, q_{0}, F), let string w = w_{1}w_{2}\dots w_{n}, and w_{i} \in \Sigma  
\\
\begin{align}
1. r_{0} = q_{0}
2. \delta (r_{i}, r_{i+1} = r_{i+1}) , i=0,1,2\dots 3\\
3. r_{n} \in F
\end{align}
$$

### regular

> 状态是用于记住事的

### 正则运算

> 从另一个角度看正则语言

let A, B are two language

1. 并
2. 连接
3. 星号

- 定理：正则语言类在 **三种运算** 下封闭

> proof: find a FA can recognize the language  or $ A \o B$ or $ A* $
>
> 证明 $A \cup B$ 是 RE： 定义一个 FA, 同时记录 $M_{A}$ $M_{B}$ 的状态

> lec2 
