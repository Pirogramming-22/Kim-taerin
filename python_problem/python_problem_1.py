import random
num=0

def brGame(player, num):
    if player == "computer":
        count = random.randint(1, 3)
        print(f"{player}가 {count}개의 숫자를 부릅니다.")
    
    else:
        while True:

            try:
                count = int(input(f"부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
                
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
        num = brGame("computer", num)
        if num >= 31:
            break

        num = brGame("player", num)

