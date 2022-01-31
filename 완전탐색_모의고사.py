def make_answer(answers,data):
    num_answer = []
    for _ in range(len(answers)//len(data)):
        num_answer.extend(data)
    num_answer.extend(data[:len(answers)%len(data)])
    return num_answer

def score(answers, num_answer):
    score = 0
    for i in range(len(answers)):
        if answers[i] == num_answer[i]:
            score += 1
    return score 
    
def solution(answers):
    answer = []
    one_data = [1,2,3,4,5]
    two_data = [2,1,2,3,2,4,2,5]
    three_data = [3,3,1,1,2,2,4,4,5,5]
    one_answer = make_answer(answers,one_data)
    two_answer = make_answer(answers,two_data)
    three_answer = make_answer(answers,three_data)
    one_score = score(answers, one_answer)
    two_score = score(answers, two_answer)
    three_score = score(answers, three_answer)   
    max_score = max(one_score,two_score,three_score)
    if one_score == max_score:
        answer.append(1)
    if two_score == max_score:
        answer.append(2)    
    if three_score == max_score:
        answer.append(3)  
    answer.sort()
    return answer

print(solution([1,3,2,4,2]))
