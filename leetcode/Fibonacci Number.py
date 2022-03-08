#하향식 (메모이제이션)
class Solution:
    d = [0] * 31

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.d[n]:
            return self.d[n]

        self.d[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.d[n]

#타뷸레이션 (상향식)
class Solution:
    d = [0] * 31

    def fib(self, n: int) -> int:
        self.d[1]=1
        for i in range(2,n+1):
            self.d[n] = self.d[n - 1] + self.d[n - 2]
        return self.d[n]
#재귀를 사용하지 않고 반복으로 풀이하며 작은 값부터 계산하면서 타뷸레이션한다.

#두 변수만 이용해 공간 정략
    def fib(self, n: int) -> int:
        x,y=0,1
        for i in range(0,n):
            x,y=y,x+y
        return x
