# 3-2 큰 수의 법칙
# p 92

# n,m,k 입력 받기
n, m, k = map(int, input().split())
# 배열 입력 받기
data = list(map(int, input().split()))


sum = 0     # 최종 합계
data = sorted(data)     # 배열 정렬
first = data[-1]        # 배열에서 가장 큰 수
second = data[-2]       # 배열에서 두번째로 큰 수
originalK = k           # k를 임시로 저장

while m > 0:
    k = originalK       # k가 0이 되면 다시 채움
    while k > 0:
        sum += first    # 가장 큰 수를 k번 더함
        k -= 1          # k 마이너스
        m -= 1          # m 마이너스
    sum += second       # 가장 큰수를 k번 더하고 나면 두번째로 큰 수를 한 번 더함
    m -= 1              # m 마이너스
print(sum)