import time

memo = {
    0: 0,
    1: 1,
    2: 1
}

star_time = time.time()

# 기존 재귀함수는 계속 n-1 n-2를 같은 연산을 해가면서 풀었음
# 만약 메모에 있으면 그 값을 반환하고
# 없다면 수식대로 구한다
# = 딕셔너리에 f(1) f(2) f(3) .... 값을 저장해서 연산 없애기

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo
result = fibo_dynamic_programming(int(input()), memo)
end_time = time.time()

print(f"{result}, {(end_time - star_time):.3f}초")