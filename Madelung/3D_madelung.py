m: list[float] = []     #1原子ごとのマーデリング定数
outermost: int = int(input())   #最外殻　
x: int = 0      #x座標
y: int = 0      #y座標
z: int = 0      #z座標
r: float = 0    #中心原子との距離

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

# for x in range(-outermost, outermost + 1):
#     for y in range(-outermost, outermost + 1):
#         for z in range(-outermost, outermost + 1):
#             if x == y == z == 0: 
#                 #中心は計算しない
#                 continue
#             r = (x**2 + y**2 + z**2) ** 0.5
#             # breakpoint()
#             if (x + y + z) % 2 == 0:
#                 r *= -1
#             if is_face:
#                 #立方体の面
#                 contribution = 0.5
#             if is_edge:
#                 #立方体の辺
#                 contribution = 0.25
#             if is_vertex:
#                 #立方体の頂点
#                 contribution: float = 0.125
#             if is_inside:
#                 #内殻
#                 contribution = 1.0
#             print(f"{contribution}, {x},{y},{z}" )
#             m.append(contribution / r)

# print(sum(m))
# print(m)
# # print(len(m))

x,y,z = 2,2,1
if (abs(x) == outermost) or (abs(y) == outermost) or (abs(z) == outermost):
    #立方体の面
    contribution = 0.5
if is_edge:
    #立方体の辺
    contribution = 0.25
if is_vertex:
    #立方体の頂点
    contribution: float = 0.125

print(contribution)