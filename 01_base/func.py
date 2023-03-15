# def menu():
#     print("오늘의 메뉴")
#     print("오늘 점심메뉴는 제육볶음입니다.")
#     print("내일의 메뉴")
#     print("냉리의 점심메뉴는 돈까스 입니다.")

# menu()

# print("사용할 데이터")
# input("데이터")

# def add(num1, num2, num3): #param 파람, parameter 파라미터
#     print(num1 + num2 + num3)

# add(1, 2, 3) # 인자 argument 알규먼츠
# # 인자의 개수 메개변수 개수 똑같이 맞춰주기

def add(text1, text2):  #독스트린 함수 설명 간단하게 써놓기
    ''' 문자열 두개(성, 이름)을 입력받아서 합쳐서 출력 
    args
        text1 : 성을 받는 문자열
        text2 : 이름을 받는 문자열    
    '''
    # print(text1 + text2)
    text = text1 + text2
    return text

print(add("홍", "길동")) # None 반환형이 없는 함수다


