top_heights = [6, 9, 5, 7, 4]

# [6, 9, 5, 7, 4]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 4]
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:  # O(N)
        height = heights.pop()
        # [6, 9, 5, 7]
        for idx in range(len(heights) - 1, -1, -1):  # 시작점, 끝나는점, 연산을 줄여갈 값  O(N)
            if heights[idx] > height:
                answer[len(heights)] = idx + 1  # 하나를 pop한 stack의 heights의 길이 = pop 한것 인덱스 (0부터 시작이니까)
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!