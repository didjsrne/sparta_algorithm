import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0  # 카운트
    last_added_date_index = 0
    max_heap = []

    while stock <= k:  # 공장이 멈추지 않게
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:  # 마지막 공급이 공장이 멈추기 전에 들어와야하니까
            heapq.heappush(max_heap, -supplies[last_added_date_index])  # 최솟값 heap으로 최댓값 구하기(음수 활용)
            last_added_date_index += 1

        answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))