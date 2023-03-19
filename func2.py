#지역변수(Local Variable), 전역변수(Globla Varialbe)

#지역변수 - 선언안 함수 내에서만 사용가능
# def jeju_potato():
#     potato = "고구마"
#     print(potato)

# jeju_potato()

# print(potato)
#NameError: name 'potato' is not defined 정의되지않음

#전역변수 - 어디에서든 사용가능

# potato = "감자"

# def jeju_potato():
#     global potato
#     print(potato)
#     potato = "고구마"
#     print(potato)
#     # UnboundLocalError: local variable 'potato' referenced before assignment
#     # 참조 : 데이터에 접근하려고 했어
#     # local symbol table 우선 여기서 변수 찾고 없으면 global symbol table에서 찾는다.
#     # 만약 활용하고 싶다면 global 활용
# jeju_potato()
# print(potato)

potato = "감자"

def jeju_potato():
    potato = "고구마"
    print(potato)

print(potato)
jeju_potato()