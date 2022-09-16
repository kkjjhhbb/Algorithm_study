def solution(n):
    return bin(n)[2:].count('1')
# 2의 n제곱 수인 경우에는 에너지가 필요하지 않다
# 2의 n제곱인 경우 -> 이진수로 변경 후에 1이 한 개일 경우
# 아닌 경우 -> 최대한 2의 n제곱쪽으로 편승해야함 그래서 +1 해서 맞춰줘야하는데 그 횟수 == 1의 개수