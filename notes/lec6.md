## TM 变型

### 多带TM

- 读写头在最左端，输入放在第一条纸带上

- $\delta: Q \times Gamma^{k} \rightarrow Q \times \Gamma^{k} \times \{L, R, S\}^{k}$

> 和 单带的能力一样，等价

### 非确定TM（NTM）

> TM的下一个动作有多个

- $\delta: Q\times \Gamma \rightarrow P(Q\times\Gamma\times\{L,R\})$

- 接受：存在一条路径接受

> NTM 等价于一个 TM

### 枚举器

- 用来打印

- 一个语言是图灵可识别的，当前仅当有枚举器能打印它

### 与其他模型的等价性

- 其他计算模型
- 无边界？读写头不动？与单带图灵机等价

## 算法的定义

- 算法：作为判定器的TM，input,output,finite,确定

> 转折点：聚焦于算法，更简单的描述算法

- 算法的描述：
  - 形式化
  - 实现
  - 高水平：伪代码

- TM的输入是串、对象转成串

- 语言--问题的转换

### Hilbert Problem?
