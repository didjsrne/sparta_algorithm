input = "abcabcabcabcdededededede"

# 모든 경우의 수 나열해서 미니멈 찾기 -> BFS
# 반절을 넘어서는 당연하게도 압축이 안된다 -> n // 2 까지 비교
def string_compression(string):
    n = len(string)
    compression_length_array = []
    for split_size in range(1, n // 2 + 1):
        splited = [string[i:i + split_size] for i in range(0, n, split_size)]
        compressed = ""
        count = 1

        for j in range(1, len(splited)):

            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]
        compression_length_array.append(len(compressed))

    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!