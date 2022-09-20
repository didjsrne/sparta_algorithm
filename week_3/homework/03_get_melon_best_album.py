genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}  # 많이 플레이 된 음악 장르(key)별 재생 수(value)
    genre_index_play_array_dict = {}  # 장르 내 정렬
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:  # 딕셔너리 안에 없다면
            genre_total_play_dict[genre] = play  # 장르(key)에 재생수 넣기
            genre_index_play_array_dict[genre] = [[i, play]]  # 장르(key)에 (인덱스, 재생수) 묶어 value에 저장
        else:  # 딕셔너리 안에 있다면
            genre_total_play_dict[genre] += play  # 재생 수 늘리기
            genre_index_play_array_dict[genre].append([i, play])

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)  # lambda item: item[1] -> 밸류값 기준 정렬 / item[0] = 키값 기준 / 내림차순
    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)  # 밸류값 기준 정렬, 내림차순
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result



print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!