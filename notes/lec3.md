## 非正则语言

- 不能用RE表示的？
  - example: $B = {0^{n}1^{n} | n \ge 0}$
  - 为什么？需要记住**n**，而 **n** 无穷
  - proof?

### pumping lemma

- if A is RL , exists P $\gt$ 0, for any w $\in$ A and |w| $\ge$ P, w = xyz
  1. $xy^{i}z \in A$
  2. |y| $\gt$ 0
  3. |xy| $\le$ P

  > `y` is the loop part

- proof of pumping lemma
  - 设识别RE A的DFA有n个状态
  - 对于长度为n的字符串
  - 至少有一对重复状态

  ```mermaid
  stateDiagram-v2
    direction LR
      [*] --> x
      x --> y
      y --> y
      y --> z
      z --> [*]
  ```
- 证明不是正则的-----假设是正则的，用pumping lemma，不符合，不是正则的！
