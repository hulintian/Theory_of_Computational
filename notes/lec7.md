# Tuning Recognizable

- The TM $M$  recognize language $L$:
$$
M(w) =
\left\{
\begin{array}{ll}
  accept  & w \in L \\
  reject   & w \notin L
\end{array}
\right.

$$

> algorithm is Decidable TM

# Decidable

## 可判定语言

> 判定语言 等于 解决问题，不同的视角

> 对应的机器模型是判定器

- 成员测试
- 空性质测试
- 等价性测试

> 算法的局限性

### problem1:

> 如何用TM做判定 DFA? TM 能干 DFA

$$
A_{DFA} = \{ <B, w> | B 是 DFA, w是串，B接受w \}
$$

> solve: TM M模拟DFA,模拟出来accept,accept,reject,reject

- for NFA? construct a TM N

$$
A_{NFA} = \{ <B, w> | B 是 NFA, w是串，B接受w \}
$$

> solve:
> 1. NFA B转 DFA C
> 2. call M decide <C, w>

$$
A_{REX} = \{ <R, w> | R 是正则表达式, w是串，R接受w \}
$$

> solve: RE to NFA, call N $A_{NFA}$

### problem2 空测试

- DFA是否为空？
- 空: 1. 没有接受状态；2. 起始状态到接受状态没有路径。
- 扩散，没有接受状态被标记
- 考虑：是否一定可以结束？

- 然后NFA,REX

### EQ

$$
EQ_{DFA} = \{ <A,B> | A and B are DFA, and L(A) = L(B) \}
$$

- 语言:字符串的集合。
- 集合相等？对等差 $A \cap \bar{B} = \Phi and \bar{A} \cap B =\Phi$

### 上下文无关语言可判定

1. CFG to Chromsky Normal Formal


#### 判断CFG是$\Phi$

> 反向扩散,从终结符开始标记，规则右侧所有的度被标记后，标记左侧的

### 所以的 CFG 可判定

- $A_{CFG}$

- 模拟TM ？ 存在左递归？

### EQ CFG  不可判定

- CFG在补和交下不封闭

## 停机问题

> 不可判定的

$$
A_{TM} = \{ <M,w> | M 是 TM, 且接受w \}
$$

- 用 TM 模拟 TM？ vm 陷入循环，host也陷入了循环，只能做到识别。

### how to proof?

> 语言比图灵机多--有些语言没有对应的TM。TM的集合是无限的，语言的集合是无限的？如何比较

- 比较无限的方法：
  - 对角化方法：映射，能不能对应上,例如自然数集合与偶自然数集合是一样大的
  - 可数：有限或与自然数集合有相同规模

- 需要证明：
  1. the set of all TMs 是可数的
    - TM 最终可以由{0，1}表示，对于任意的字母表$\Sigma$
  2. 语言的集合是不可数的
