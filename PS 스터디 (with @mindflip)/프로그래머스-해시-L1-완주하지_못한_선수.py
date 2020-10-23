# def solution(participant, completion):
#     for i in range(len(participant)):
#         if participant[i] in completion:
#             completion.remove(participant[i])
#             participant[i] = ""

#     for p in participant:
#         if p != "":
#             return p
# 유효성 검사 탈락

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[i+1]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))