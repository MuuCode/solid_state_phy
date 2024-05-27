m: list[float] = []
outermost: int = int(input())
i: int = 0
x: float = 0
y: float = 0


for x in range(-outermost, outermost + 1):
   for y in range(-outermost, outermost + 1):
      if x == y == 0:
         continue
      r: float = (x**2 + y**2) ** 0.5
      if (x + y ) % 2 == 0:
         r *= -1
      if abs(x) == abs(y) == outermost:
         #最外殻の四隅
         contribution: float = 0.25
      if abs(x) != abs(y) and (abs(x) == outermost or abs(y) == outermost):
         #最外殻の辺
         contribution = 0.5
      if abs(x) != outermost and abs(y) != outermost:
         #内殻
         contribution = 1.0
      
      m.append(contribution / r)


print(sum(m))