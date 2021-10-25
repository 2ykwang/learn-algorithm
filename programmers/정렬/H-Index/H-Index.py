def solution(citations):
    citations.sort(reverse=True)

    answer = 0

    for c in citations:
        if answer >= c:
            break
        answer += 1
    return answer
