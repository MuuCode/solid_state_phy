m: list[float] = []
outermost: int = int(input())
i: int = 0
x: int = 0
r: float = 0

for x in range(-outermost, outermost + 1):
   if x == 0:
      continue
   r = abs(x)
   if x % 2 == 0:
      r *= -1
   m.append(1 / r)


print(sum(m))

# import math

# print(2 * math.log(2))