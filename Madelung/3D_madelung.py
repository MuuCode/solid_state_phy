import time

outermost: int = int(input())   #最外殻　
start_time = time.time()  # 計測開始

m: list[float] = []     #1原子ごとのマーデリング定数
x: int = 0      #x座標S
y: int = 0      #y座標
z: int = 0      #z座標
r: float = 0    #中心原子との距離
test = outermost ** 2

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

for x in range(-outermost, outermost + 1):
    for y in range(-outermost, outermost + 1):
        for z in range(-outermost, outermost + 1):
            if x == y == z == 0: 
                #中心は計算しない
                continue
            r = (x**2 + y**2 + z**2) ** 0.5
            # breakpoint()
            if (x + y + z) % 2 == 0:
                r *= -1
            if is_face:
                #立方体の面
                contribution = 0.5
            elif is_edge:
                #立方体の辺
                contribution = 0.25
            elif is_vertex:
                #立方体の頂点
                contribution: float = 0.125
            elif is_inside:
                #内殻
                contribution = 1.0
            # print(f"{contribution}, {x},{y},{z}" )
            m.append(contribution / r)


print(sum(m))

end_time = time.time()  # 計測終了

# 実行時間を表示
print(f"実行時間: {end_time - start_time:.6f} 秒")
# print(m)
# # print(len(m))

# x,y,z = 1,1,1
# test: str = 'default'
# contribution: float = 0
# # breakpoint()
# # if is_vertex_abs:
# #     #立方体の頂点
# #     contribution = 0.125
# #     print(f"contribution: {contribution}")
# # if is_vertex:
# #     test = 'vertex'
# #     print(f"test: {test}")
# # if x == outermost:
# #     test = 'only_x'
# #     print(f"test: {test}")
# # if x == y == z == outermost:
# #     test = 'x == y == z == outermost'
# #     print(f"test: {test}")
# print(str(is_vertex_abs))
# # if x == outermost and y == outermost:
# #     test == 'x_y'


# elif is_edge:
#     #立方体の辺
#     contribution = 0.25
# elif (abs(x) == outermost) or (abs(y) == outermost) or (abs(z) == outermost):
#     #立方体の面
#     contribution = 0.5
# print(f"contribution: {contribution}")
# print(f"test: {test}")



# outermost: int = int(input()) 
# x,y,z = 1,-1,1
# test: str = 'default'
# contribution: float = 0
# is_vertex = (
#     abs(x) == outermost and abs(y) == outermost and abs(z) == outermost
# )
# is_edge = {
#     (abs(x) == abs(y) == outermost and abs(z) != outermost) or 
#     (abs(y) == abs(z) == outermost and abs(x) != outermost) and 
#     (abs(x) == abs(z) == outermost and abs(y) != outermost)
# }


# if abs(x) == outermost and abs(y) == outermost and abs(z) == outermost:
#     #立方体の頂点
#     contribution = 0.125
#     print(f"contribution: {contribution}")
# if is_vertex:
#     test = 'vertex'
#     print(f"test: {test}")
# if is_edge:
#     print("edge")