a = float(input())
b = float(input())
c = float(input())
x1 = (-b-(b**2-(4*a*c))**0.5)/(2*a)
x2 = (-b+(b**2-(4*a*c))**0.5)/(2*a)
print(round(x1,3),round(x2,3))

#โดยปกติแล้วถ้า round ได้เลขลงตัวที่เป็นจำนวนเต็ม มันจะมี .0 ให้แค่ตำแหน่งเดียว
