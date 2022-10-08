def solution(n):
    answer = 0
    arr = [[0 for _ in range(n)] for _ in range(n)]
    check_col = [False] * n
    check_dig1 = [False] * (2 * n - 1)
    check_dig2 = [False] * (2 * n - 1)

    def possible(r, c):
        if check_col[c]:
            return False
        if check_dig1[r + c]:
            return False
        if check_dig2[r - c + n - 1]:
            return False
        return True

    def nqueen(r, cnt):
        nonlocal answer
        if r == n or cnt == n:
            answer += 1
            return

        for c in range(n):
            if arr[r][c] != 'Q' and possible(r, c):
                check_col[c] = True
                check_dig1[r + c] = True
                check_dig2[r - c + n - 1] = True
                arr[r][c] = 'Q'
                cnt += 1
                nqueen(r + 1, cnt)
                check_col[c] = False
                check_dig1[r + c] = False
                check_dig2[r - c + n - 1] = False
                arr[r][c] = ''
                cnt -= 1

    nqueen(0, 0)
    return answer