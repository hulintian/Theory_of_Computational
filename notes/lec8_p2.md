# 可规约性

> $A_{TM}$ is not decidable. 用规约来找到更多 not decidable

- 可规约性：problem A 可规约到 problem B，用B的解来解A

## HALT
> TM 会不会停止
$$
HALT = \{ <M,w> | M 是 TM,且对输入w停机 \}
$$

- proof $A_{TM} \lt HALT_{TM}$
