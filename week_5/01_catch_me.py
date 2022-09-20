from collections import deque

c = 11
b = 2

# 코니의 위치 변화
# 코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1 만큼 이동
# 즉 증가하는 속도가 1초마다 1초씩 증가
# 속도 1 2 3 4 5 6 7 8 9 ...
# 위치 3 5 8 13 18  ... f(n) = f(n-1)+t

# 브라운의 위치 변화
# B - 1, B + 1, 2 * B
# 모든 경우의 수를 나열 - BFS
# 규칙적 -> 배열, 자유자재 -> 딕셔너리
# 각 시간마다 브라운의 위치를 저장 [{ }]

# 잡았다 = 동일한 시간에 동일한 위치

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 브라운의 위치와 시간 동시에 담기
    visited = [{} for _ in range(200001)]
    # visited[위치][시간]
    # visited[3]에 5라는 키가 있냐? -> 3 위치에 5초에 간 적이 있냐?
    # visited[cony_loc] time

    while cony_loc < 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):  # Q. Queue 인데 while 을 안 쓰는 이유를 고민해보세요!
            current_position, current_time = queue.popleft()

            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1




print(catch_me(c, b))