import pkg.modu as p

print("請輸入三角形的 3 個頂點坐標")
print("-" * 30)
a = tuple(map(int, input("請輸入頂點 a 的坐標：").split(',')))
b = tuple(map(int, input("請輸入頂點 b 的坐標：").split(',')))
c = tuple(map(int, input("請輸入頂點 c 的坐標：").split(',')))
print("-" * 30)
result = p.modu.triangle_zhonxin(a, b, c)
print(f"此三角形的重心為：{result}")
