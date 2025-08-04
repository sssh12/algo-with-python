# +와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

# range() 함수가 for 문을 순환하며 반환하는 인덱스 값이 필요 없는 경우 _를 사용
for _ in range(n // 2):
  print('+-', end='') # +-를 n // 2개의 출력

if n % 2:
  print('+', end='')  # n이 홀수일 때만 +를 출력

print()