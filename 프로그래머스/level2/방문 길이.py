def solution(dirs):
    answer = 0
    visited = []
    # LRUD
    move = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x = y = 0
    for dir in dirs:
        for i, m in enumerate(move):
            if dir == m:
                nx = x + dx[i]
                ny = y + dy[i]

                if -5 <= nx <= 5 and -5 <= ny <= 5:
                    if ((x, y), (nx, ny)) not in visited:
                        visited.append(((x, y), (nx, ny)))
                        visited.append(((nx, ny), (x, y)))
                        answer += 1
                    x, y = nx, ny
    return answer