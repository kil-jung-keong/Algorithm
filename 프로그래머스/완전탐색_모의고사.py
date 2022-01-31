def make_answer(answers,data):
    num_answer = []
    for _ in range(len(answers)//len(data)):
        num_answer.extend(data)
    num_answer.extend(data[:len(answers)%len(data)])
    return num_answer

def solution(answers):
    answer = []
    one_data = [1,2,3,4,5]
    two_data = [2,1,2,3,2,4,2,5]
    three_data = [3,3,1,1,2,2,4,4,5,5]
    one_answer = make_answer(answers,one_data)
    two_answer = make_answer(answers,two_data)
    three_answer = make_answer(answers,three_data)
    return answer