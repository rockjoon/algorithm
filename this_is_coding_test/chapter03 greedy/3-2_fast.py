# 3-2 큰 수의 법칙
# m이 10억 이상이 되더라도 시간 초과 없이 연산할 수 있는 방법

# n,m,k 입력 받기
n, m, k = map(int, input().split())
# 배열 입력 받기
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

# 가장 큰수가 k번 더해지고 두 번째로 큰 수가 한번 더해진다.
# 이러한 수열이 반복된다.
part = first * k + second
# 반복되는 수열의 길이
part_length = k+1
# 수열이 반복되는 횟수
part_count = m // part_length
# 수열이 반복되고 남은 숫자의 갯수
surplus = m % part_length

sum = part * part_count + k * surplus
print(sum)
