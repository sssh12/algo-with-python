# 1부터 n까지 정수의 합 구하기 2(for 문)
# 변수가 하나만 있을 때는 while 문보다 for 문을 사용하는 것이 좋음

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
for i in range(1, n + 1):
  """
  range() 함수는 이터러블 객체를 생성
  이터러블 객체는 '반복할 수 있는 객체'를 의미
  파이썬에서 사용하는 대표적인 이터러블 자료형은 list, str, tuple
  """
  sum += i  # sum에 i를 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')