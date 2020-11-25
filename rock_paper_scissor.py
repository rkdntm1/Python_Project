#가위 바위 보 만들어보기 
#랜덤
import random

print("------가위바위보 시작!------- ")
#가위 바위 보 를 리스트로 지정해 놓기
A = ['가위', '바위', '보'] 
#횟수 카운터 추가
win = 0
cnt = 0
draw = 0

while True:
    #컴퓨터 가위바위보 값 랜덤 지정 해주기
    computer = random.choice(A)
    #나의 가위바위보값 입력
    answer = input('무엇을 내실껀가요? ')
    if computer == '가위':
        if answer == '가위':
            print('비겼다!')
            draw += 1
        elif answer == '바위' :
            print('이겼다!')
            win += 1
        elif answer == '보' :
            print('졌다!')            
    elif computer == '바위' :
        if answer == '가위' :
            print('졌다!')
        elif answer == '바위' :
            print('비겼다!')
            draw += 1
        elif answer == '보' :
            print('이겼다!')
            win += 1
    elif computer == '보' :
        if answer == '가위' :
            print('이겼다!')
            win += 1
        elif answer == '바위' :
            print('졌다!')
        elif answer == '보' :
            print('비겼다!')
            draw += 1
    if answer == '그만':
        break
    cnt += 1 
print("======게임종료/게임결과 ======")
print("총 횟수 : {0} , 승리 : {1} 패배 : {2} 무승부 {3}".format(cnt,win, cnt-win-draw, draw ))