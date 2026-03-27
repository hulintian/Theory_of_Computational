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
