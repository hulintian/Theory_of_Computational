## Class NP
- 验证

- 找 HAMPATH :
  - 暴力：
  1. 枚举
  2. 验证

> 用非确定的TM，枚举出所有情况，验证器验证

证据(proof): path
证据就是NTM的一条枚举的路径，而这条证据的路径是一个确定的。

- Defn: NP
  1. DTM verify in P time
  2. NTM solve in NP time

- P:判定 NP:验证
  - 是不是真包含？不知道，未定

## NP 完全

- 在NP集合的边缘

### 1. 可满足性问题 SAT
- 存在对变量的负责，让布尔公式结果为1

> Cook-Levin

### 多项式时间规约性
