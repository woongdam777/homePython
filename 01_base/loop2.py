# for i in range(1, 10+1):
#     print(i)

# for i in "일이삼사오" :
#     print(i)

# fruits = ["사과", "딸기", "바나나"]    
# for i in fruits:
#     print("과일 바구나에 {}가 들어있습니다.".format(i))

# 1부터 30까지의 수 중에서 3의 배수들의 합을 구하시오.

# sum = 0

# for i in range(1, 30+1):
#     if i % 3 == 0:
#         print("{} + {} = ".format(sum,i), end = "")
#         sum+=i
# print(sum)

# sum = 0

# for i in range(3, 30+1,3):
#         if i % 3 == 0:
#            print("{} + {} = ".format(sum,i), end = "")
#         sum+=i
# print(sum)

# coffee = {"아메리카노" : 2500, "라떼" : 3000, "자바" : 2500}

# for i in coffee.items(): # 전부
#     print(i)

# for i in coffee.values(): # 값
#     print(i)
    
# for i in coffee.keys(): # 키값
#     print(i)

# for i in enumerate(coffee): #인덱스와 함꼐
#     print(i)

# list_2nd = [[1,2,3],["a","b","c"]]

# for i in list_2nd:
#     for j in i:
#         print(j)

# for i  in range(1,3):
#     for j in range(1,3):
#         print("첫 번째 for문의 반복 {}번, 두번째 for 문의 반복{}번".format(i,j))


# print("2단부터 9단까지 구구단 출력")
# for i in range(2, 9+1):
#     for j in range(1,9+1):
#         # print("{} x {} = {}".format(i,j,i*j), end = "\t")
#         print(f"{i} x {j} = {i*j}", end = "\t")
#     print()


# 3중 for문
list_3rd = [[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]]

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in list_3rd:
    cnt1 += 1
    print("i의 {}번째 반복입니다.".format(cnt1))
    print(i)
    for j in i:
      cnt2 += 1
      print("j의 {}번째 반복입니다.".format(cnt2))
      print(j)
      for k in j:
          cnt3 += 1
          print("k의 {}번째 반복입니다.".format(cnt3))
          print(k)
print("i는 {}번 반복, j는 {}번 반복, k는{}번 반복".format(cnt1,cnt2,cnt3))