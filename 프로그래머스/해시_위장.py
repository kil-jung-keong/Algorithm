from collections import defaultdict
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
def solution(clothes):
    for i in range(len(clothes)):
        clothes[i].reverse()
    cloth_list = defaultdict(list)
    for k,v in clothes:
        cloth_list[k].append(v)
    count = 1
    for k in cloth_list.keys():
        count *= (len(cloth_list[k]) + 1)
    count -= 1
    return count
print(solution(clothes))
