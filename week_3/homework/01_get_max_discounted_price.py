shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    coupons.sort(reverse=True)  # 내림차순 정렬 [40, 20]
    prices.sort(reverse=True)  # 내림차순 정렬 [1500000, 30000, 2000]
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100  # 가격이 젤 높은순으로 젤 쏀 할인받기
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):  # 쿠폰보다 물품이 많을때, 물품보다 쿠폰이 많을땐 의미가 없음
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000