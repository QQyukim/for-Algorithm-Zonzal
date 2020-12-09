def solution(genres, plays):
    play_per_genre = {}
    total_play_per_genre = {}
    answer = []

    for i in range(len(genres)):
        if genres[i] not in play_per_genre:
            play_per_genre[genres[i]] = [(plays[i], i)]
            total_play_per_genre[genres[i]] = plays[i]
        else:
            play_per_genre[genres[i]].append((plays[i], i))
            total_play_per_genre[genres[i]] += plays[i]
    
    # total 딕셔너리에서 value 값이 큰 순서대로 정렬 (내림차순)
    # play 딕셔너리의 total_play_per_genre[i] 장르에서 재생 많은 순으로 정렬 (내림차순)
    # play 딕셔너리 내에서 재생 횟수가 같은 게 있으면 고유 번호 작은 순으로 정렬 (오름차순)
    
    total_play_per_genre = sorted(total_play_per_genre.items(), key = lambda x : -x[1])

    for g in total_play_per_genre:
        album_list = play_per_genre[g[0]]
        # x[0]: 재생 횟수, x[1]: 고유 번호
        album_list = sorted(album_list, key = lambda x : (-x[0], x[1]))

        for i in range(len(album_list)):
            if i == 2:
                break
            else:
                answer.append(album_list[i][1])
    
    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
# ans = [4, 1, 3, 0]

# https://somjang.tistory.com/entry/Programmers-%ED%95%B4%EC%8B%9C-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-Python
# https://dailyheumsi.tistory.com/67