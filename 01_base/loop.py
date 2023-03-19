# # 최소값 최대값 입력
# min_num = int(input("최소값 입력 > "))
# max_num = int(input("최대값 입력 > "))
# # 홀수, 짞수 리스트 생성
# odd_list = []
# even_list = []
# # 제어변수에 최소값 할당
# num = min_num

# # 최소값이 최대값 보다 작을 경우 실행

# if min_num < max_num:
#     while num <= max_num: # 제어변수가 최댓값이 될 때까지 반복 실행
#         if num %2 ==0: # 짝수 판별
#             even_list.append(num)
#         else:
#             odd_list.append(num)
#         num += 1
#     print("{}부터 {}까지의 짝수는 {}입니다.".format(min_num, max_num, even_list)) # 최소, 최대, 짝수출력
#     print("{}부터 {}까지의 홀수는 {}입니다.".format(min_num, max_num, odd_list)) # 최소, 최대, 홀수출력
# else: # 최소값이 최대값보다 크거나 같은 경우
#     print("최댓값 {}이 최소값 {}보다 크지 않습니다.".format(max_num, min_num))        
    

# 탈출문
# numbers=[[1,2,3],[10,20,30]]

# for i in numbers:
#     print(i)
#     for j in i:
#         print(j)
#         break

# key = 제품이름, value = 가격
menu = {"아이스 아메리카노" : 3000, "아메리카노" : 2500, "아이스 라떼" : 4000,
        "라떼" : 3500, "아이스크림" : 8000}
        
ice_menu = {}
hot_menu = {}

for i, j in menu.items():
    if i[0:3] =="아이스":
        ice_menu[i] = j
    else:
        hot_menu[i] = j

print("차가운 메뉴")
for i, j in ice_menu.items():
    print("제품명 : {}, 가격 : {}".format(i,j))
print("따뜻한 메뉴")
for i, j in hot_menu.items():
    print("제품명 : {}, 가격 : {}".format(i,j))
