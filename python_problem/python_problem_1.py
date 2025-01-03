num=0

def brGame(player, num):
    while True:

        try:
            count = int(input(f" {player}부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
            
            if count in [1, 2, 3]:
                break
            else:
                print("1,2,3 중 하나만 입력하세요")
        
        except ValueError:
            print("정수를 입력하세요.")

    for i in range(count):
        num += 1
        print(f"{player} : {num}")
        if num >=31 : 
            print(f"게임종료 {player} win!")
            break
    return num 

while num < 31:
    num = brGame("playerA", num)
    if num >= 31:
        break
    num = brGame("playerB", num)

    # while True:
    #     try:
    #         countB = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
            
    #         if countB in [1, 2, 3]:
    #             break
    #         else:
    #             print("1,2,3 중 하나만 입력하세요")
    #     except ValueError:
    #         print("정수를 입력하세요")

    # for i in range(countB):
    #     num += 1
    #     print(f"playerB : {num}")
    #     if num >=31 : 
    #         print("게임종료! playerB win!")
    #         break
    # if num >=31:
    #     break


























