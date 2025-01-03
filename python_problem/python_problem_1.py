num=0

while num < 31: 
    while True:

        try:
            count = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
            
            if count in [1, 2, 3]:
                break
            else:
                print("1,2,3 중 하나만 입력하세요")
        
        except ValueError:
            print("정수를 입력하세요.")

    for i in range(count):
        num += 1
        print(f"playerA : {num}")
        if num >=31 : 
            print("게임종료 playerA win!")
            break
    if num >=31:
        break

    while True:
        try:
            countB = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
            
            if countB in [1, 2, 3]:
                break
            else:
                print("1,2,3 중 하나만 입력하세요")
        except ValueError:
            print("정수를 입력하세요")

    for i in range(countB):
        num += 1
        print(f"playerB : {num}")
        if num >=31 : 
            print("게임종료! playerB win!")
            break
    if num >=31:
        break






# #8단계 
# def brGame(player) : 
# while True : 
#     try : 
#         count = int(input(f"{player} 부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))


#         if (count in [1,2,3]):
#             break
#         else:
#             print("1,2,3 중 하나만 입력하세요")

# # sum(count) !=6 필요없는거거

#     except ValueError :
#         print("정수를 입력하세요요")

# #4단계 
# for i in range(count):
#     num += 1
#     print(f"{player} : {num}")
#     if num == 31:
#         return player

# #num 1 증가하고서 출력력
# #if num==31이면 종료 > print문이 아니라 return문으로 

# while num < 31:
#     winner = brGame("playerA")
#     if winner:
#         print(f"{winner} win!")
#         break

#     winner = brGame("playerB")
#     if winner:
#         print(f"{winner} win!")
#         break
























