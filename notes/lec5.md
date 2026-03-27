### PDA 与 CFG 之间的等价性

> need to read book.

CGL : 被 CFG 生成；用 PDA 能生成

## 非上下文无关的

> 超出 PDA 识别能力范围的

### Pumping Lemma

- if A is CFL, exist $P \gt 0$ for any $s \in A, |s|\ge P, s=uvxyz$ 满足
  1. for each $i \ge 0, uv^{i}xy^{i}z \in A$
  2. $|vy| > 0$
  3. $|vxy| \le p$

> 当 $|s|$ 足够长，生产s的解析树的高度比 CFG的 variable还多，最长的那个路径上必定出现两个同一个variable，假设重复的是 $R$ 有 $R \Rightarrow x; R\Rightarrow vRy; then: R\Rightarrow v^{i}Ry^{i}$

> read example 2.21, use pumping lemma to proof

> 栈的哲学意义：只能记住一条路径的历史
