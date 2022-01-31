def left_days(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]
        if progresses[i] % speeds[i] == 0:
            day = progresses[i] // speeds[i]
            days.append(day)
        else:
            day = progresses[i] // speeds[i]
            day += 1
            days.append(day)
    return days
        
def solution(progresses, speeds):
    answer = []
    days = left_days(progresses, speeds)
    max_day = max(days)
    function = [0] * (max_day+1)
    function[days[0]] += 1
    for i in range(1,len(days)):
        # if days[i-1] > days[i]:
        #     function[days[i-1]] += 1
        # elif days[i-1] <= days[i]:
        max_day = max(days[:i+1])
        function[max_day] += 1
    for func in function:
        if func != 0:
            answer.append(func)
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))