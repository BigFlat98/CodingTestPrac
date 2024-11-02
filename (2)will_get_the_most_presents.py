
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
friends = ["muzi", "ryan", "frodo", "neo"]


# #선물 전달 도식화
# def split_gift(gifts_list,friends_list):
#     or_list = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
#     for g in gifts_list:
#         gift_data = g.split(" ")
#         for l in range(len(friends)):
#             if gift_data[0] == friends_list[l]:
#                 give_index = l
#             if gift_data[1] == friends_list[l]:
#                 take_index = l
#         or_list[give_index][take_index]+=1
#     return or_list

# def take_list(org,friends_list):
#     take_sum_list = []
#     for i in range(len(friends_list)):
#         s=0
#         for j in range(len(friends_list)):
#             s+=org[j][i]
#         take_sum_list.append(s)  
#     return take_sum_list

# def who_is_the_winner(org,friends_list):
#     can_take_list = [0 for _ in range(len(friends_list))]
#     for i in range(len(friends_list)):
#         for j in range(len(friends_list)):
#             if i == j :
#                 continue
#             elif org[i][j] > org[j][i]:
#                 can_take_list[i] +=1
#             elif gift_index_list[i] > gift_index_list[j]:
#                 can_take_list[i] +=1
#     return max(can_take_list)

# or_list = split_gift(gifts,friends)
# give_sum_list= list(map(sum,or_list))
# take_sum_list = take_list(or_list,friends)
# #선물 지수 리스트
# gift_index_list = [(give_sum_list[i] - take_sum_list[i]) for i in range(len(give_sum_list))]
# winner = who_is_the_winner(or_list,friends)

# print(winner)

def split_gift(gifts_list,friends_list):
    or_list = [[0 for _ in range(len(friends_list))] for _ in range(len(friends_list))]
    for g in gifts_list:
        gift_data = g.split(" ")
        for l in range(len(friends_list)):
            if gift_data[0] == friends_list[l]:
                give_index = l
            if gift_data[1] == friends_list[l]:
                take_index = l
        or_list[give_index][take_index]+=1
    return or_list
#스플릿을 사용해서 직접 나누는 방법도 있지만 enumelate 함수를 사용해서 인덱스와 값을 각 변수에 넣고 값을 비교하는 방법도 있을 듯

def take_list(org,friends_list):
    take_sum_list = []
    for i in range(len(friends_list)):
        s=0
        for j in range(len(friends_list)):
            s+=org[j][i]
        take_sum_list.append(s)  
    return take_sum_list

def who_is_the_winner(org,friends_list,gil):
    can_take_list = [0 for _ in range(len(friends_list))]
    for i in range(len(friends_list)):
        for j in range(len(friends_list)):
            if i == j :
                continue
            elif org[i][j] > org[j][i]:
                can_take_list[i] +=1
            elif org[i][j] == org[j][i]:
                if gil[i] > gil[j]:
                    can_take_list[i] +=1
    return max(can_take_list)
        

def solution(friends, gifts):
    or_list = split_gift(gifts,friends)
    give_sum_list= list(map(sum,or_list))
    take_sum_list = take_list(or_list,friends)
    gift_index_list = [(give_sum_list[i] - take_sum_list[i]) for i in range(len(give_sum_list))]
    answer = who_is_the_winner(or_list,friends,gift_index_list)
    return answer

print(solution(friends,gifts))
#중요한 풀이
#여기서 
# def solution(friends, gifts):
#     f = {v: i for i, v in enumerate(friends)} -> 친구 리스트의 각 친구명을 인덱스 번호로 사용하기 위해 딕셔너리로 만들고
#     l = len(friends)
#     p = [0] * l
#     answer = [0] * l
#     gr = [[0] * l for i in range(l)]
#     for i in gifts:
#         a, b = i.split()
#         gr[f[a]][f[b]] += 1 -> 만든 딕셔너리로 친구 명을 인덱스로 사용하면 코드를 많이 줄일 수 있음.

#     for i in range(l):->이게 선물 지수 계산한 결과 넣는 리스트 만드는 코드인 것 같음
#         p[i] = sum(gr[i]) - sum([k[i] for k in gr])->진짜 잘 짰다

#     for i in range(l): ->여기는 뭐.. 똑같고
#         for j in range(l):
#             if gr[i][j] > gr[j][i]:
#                 answer[i] += 1
#             elif gr[i][j] == gr[j][i]:
#                 if p[i] > p[j]:
#                     answer[i] += 1 

#     return max(answer)
