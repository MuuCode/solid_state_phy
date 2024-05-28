m: list[float] = []     #1原子ごとのマーデリング定数
outermost: int = int(input())   #最外殻　
x: int = 0      #x座標
y: int = 0      #y座標
z: int = 0      #z座標
r: float = 0    #中心原子との距離
x, y, z = -1, 1, 0
#頂点の条件
is_vertex = (
    abs(x) == outermost and
    abs(y) == outermost and
    abs(z) == outermost
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
    abs(x) < outermost and
    abs(y) < outermost and
    abs(z) < outermost
)


if is_vertex :
    #立方体の頂点 (is_edge と is_faceに含まれるのでこの順番にする)
    contribution = 0.125
elif is_edge:
    #立方体の辺
    contribution: float = 0.25
elif is_face:
    #立方体の面
    contribution = 0.5
elif is_inside:
    #内殻
    contribution = 1.0

print(contribution)