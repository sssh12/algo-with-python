# 2자리 양수(10 ~ 99) 입력받기(드모르간의 법칙을 사용한 방법)

print('2자리 양수를 입력하세요.')

while True:
  no = int(input('값을 입력하세요.: '))
  if not(no < 10 or no > 99):  # no >= 10 and no <= 99와 같음
    break

print(f'입력받은 양수는 {no}입니다.')