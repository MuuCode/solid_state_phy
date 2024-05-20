import math
import numpy as np

m = []
outermost = int(input())
# outermost = 2
i = 0
x = 0
y = 0
z = 0

#頂点の条件
is_vertex = (
    abs(x) == outermost and
    abs(y) == outermost and
    abs(z) == outermost
)
#辺の条件
is_edge = (
    (abs(x) == outermost and abs(y) == outermost and z == 0) or
    (abs(x) == outermost and abs(z) == outermost and y == 0) or
    (abs(y) == outermost and abs(z) == outermost and x == 0)
)
#面の条件
is_face = (
    (abs(x) == outermost and y == 0 and z == 0) or
    (abs(y) == outermost and x == 0 and z == 0) or
    (abs(z) == outermost and x == 0 and y == 0)
)
#内部の条件
is_inside = (
    abs(x) != outermost and
    abs(y) != outermost and
    abs(z) != outermost
)

r = []
for x in range(-outermost, outermost + 1):
    for y in range(-outermost, outermost + 1):
        for z in range(-outermost, outermost + 1):
            if x == y == z == 0: 
                #中心は計算しない
                continue
            r = (x**2 + y**2 + z**2) ** 0.5
            r.append((x**2 + y**2 + z**2) ** 0.5)
            if (x + y + z) % 2 == 0:
                r *= -1
            if is_vertex:
                #立方体の頂点
                contribution = 0.125
            if is_edge:
                #立方体の辺
                contribution = 0.25
            if is_edge:
                #立方体の面
                contribution = 0.5
            if is_inside:
                #内殻
                contribution = 1.0
            
            m.append(contribution / r)


# print(sum(m))
print(r)