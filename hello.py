# แสดงข้อความ "ยินดีต้องรับสู่บทเรียน"
print('ยินดีต้อนรับสู่บทเรียน')

name = input('คุณชื่ออะไร : ')
print('คุณชื่อ : %s'%name)
print("คุณชื่อ : %s"%name)
print('คุณชื่อ : {0}'.format(name))

number = int(input('กรุณากรอกตัวเลข : '))

# โปรแกรมเกิดข้อผิดพลาด
if number > 10:
    print('ตัวเลขที่คุณกรอกมีค่ามากกว่าสิบ')
    #   print('เป็นจำนวนคู่')
else:
    print('ตัวเลขที่คุณกรอกมีค่าน้อยกว่าสิบ')
    print('เป็นจำนวนคี่')

# ประเภทตัวแปร 
a = 3
b = 0.5
c = 'สวัสดีครับ'
d = "สวัสดีครับ"
e = True

n1 = 10
n2 = 20

print(n1 == 10) # True
print(n2 == 10) # False
print(n1 == 10 and n2 == 20) # True
print(n1 == 10 or n2 == 20) # True

print(n1 + n2) # 30
print(n1 - n2) # -10
print(n1 * n2) # 200
print(n1 / n2) # 0.5
print((n1 + n1) * (n2 - n1) / 2) # 100

print('สวัสดีครับ' + 'ยินดีต้อนรับ') # สวัสดีครับยินดีต้อนรับ
print('สวัสดีครับ' + 'ยินดีต้อนรับ' + n1 + 'sdf')

