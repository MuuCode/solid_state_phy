import numpy as np
import time

outermost = int(input())  # 最外殻
start_time = time.time()  # 計測開始

# 座標を作成
x, y, z = np.meshgrid(
    np.arange(-outermost, outermost + 1),
    np.arange(-outermost, outermost + 1),
    np.arange(-outermost, outermost + 1),
    indexing='ij'
)

# 中心(0, 0, 0)を除外
mask_center = (x == 0) & (y == 0) & (z == 0)

# 距離の計算
r = np.sqrt(x**2 + y**2 + z**2)
r[mask_center] = np.inf  # 中心は計算しない

# 偶奇による符号反転
sign = np.where((x + y + z) % 2 == 0, -1, 1)

# 頂点の条件
is_vertex = (np.abs(x) == outermost) & (np.abs(y) == outermost) & (np.abs(z) == outermost)

# 辺の条件
is_edge = ((np.abs(x) == outermost) & (np.abs(y) == outermost)) | \
          ((np.abs(x) == outermost) & (np.abs(z) == outermost)) | \
          ((np.abs(y) == outermost) & (np.abs(z) == outermost))

# 面の条件
is_face = (np.abs(x) == outermost) | (np.abs(y) == outermost) | (np.abs(z) == outermost)

# 内部の条件
is_inside = (np.abs(x) < outermost) & (np.abs(y) < outermost) & (np.abs(z) < outermost)

# 貢献度の設定
contribution = np.ones_like(r)
contribution[is_face] = 0.5
contribution[is_edge] = 0.25
contribution[is_vertex] = 0.125

# 中心を除外した計算
m = sign * contribution / r
m[mask_center] = 0

# 結果を出力
print(np.sum(m))

end_time = time.time()  # 計測終了

# 実行時間を表示
print(f"実行時間: {end_time - start_time:.6f} 秒")
