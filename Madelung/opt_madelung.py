m: list[float] = []     #1原子ごとのマーデリング定数
outermost: int = int(input())   #最外殻　
x: int = 0      #x座標
y: int = 0      #y座標
z: int = 0      #z座標
r: float = 0    #中心原子との距離

#頂点の条件 (1,1,1)
is_vertex = (
    x == outermost and
    y == outermost and
    z == outermost
)
#本来の立方体における辺の中心 (1,1,0), (0,1,1), (1,0,1)
is_vertex_on_edge = (
    (x == outermost and y == outermost and z == 0) or
    (x == outermost and z == outermost and y == 0) or
    (y == outermost and z == outermost and x == 0)
)
#軸上の頂点　（本来の立方体における面の中心) (1,0,0), (0,1,0), (0,0,1)
is_vertex_on_axis = (
    (x == outermost and y == 0 and z == 0) or
    (y == outermost and x == 0 and z == 0) or
    (z == outermost and x == 0 and y == 0)
)
#辺の条件
is_edge = (
    (abs(x) == outermost and abs(y) == outermost) or
    (abs(x) == outermost and abs(z) == outermost) or
    (abs(y) == outermost and abs(z) == outermost)
)
#面の条件
is_face = (
    (abs(x) == outermost) or
    (abs(y) == outermost) or
    (abs(z) == outermost)
)
#内部の条件
is_inside = (
    x != outermost and
    y != outermost and
    z != outermost
)

for x in range(0, outermost + 1):
    for y in range(0, outermost + 1):
        for z in range(0, outermost + 1):
            if x == y == z == 0: 
                #中心は計算しない
                continue
            r = (x**2 + y**2 + z**2) ** 0.5
            if (x + y + z) % 2 == 0:
                r *= -1
            if is_vertex or is_vertex_on_edge or is_vertex_on_axis:
                #立方体の頂点
                contribution: float = 0.125
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

M = map(lambda x: x*4, m)
rest = sum(M)
print(rest)
