def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)

    return participant[-1]