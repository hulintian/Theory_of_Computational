# Chapter 3 丘奇-图灵论题

## Turning Machine

> read-head + infinite tape
> - 反复读写
> - 由状态决定是否停止，TM之有一个接受和一个拒绝状态，进入接受/输入马上停机，除此为循环状态

- TM formal define

TM is a 7-tuple $(Q, \Sigma, \Gamma, \delta, q_{0}, q_{acc}, a_{rej})$

- 说清楚图灵机当前的状态（图灵机的格局）
  1. 状态控制器当前的状态
  2. 当前带子上的内容
  3. 读写头的位置

- Configuration of TM (图灵机的格局)，example：
  - `aqb`：状态`q`，读写头在`b`上
  - init: $q_{0}w$
  - accept: $uq_{accept}v$
  - reject: $uq_{reject}v$

- TM 接受：
  - 存在格局序列$C_{1}C_{2}\cdots C_{k}$,

> let A is a language

- Turning 可识别 （Turning-recognizable）
  - $a \in A$ accept
  - $a \notin A$ reject or loop

- 图灵可判断(Turning Decidable)：接受、拒绝，
> 不管怎么样都停机 -- **判定**，完备 $\sqcup$
