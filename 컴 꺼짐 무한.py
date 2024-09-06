import os
import time
import msvcrt  # Windows에서만 사용 가능

def should_shutdown():
    print("10초 후 시스템이 종료됩니다. 'w' 키를 누르면 종료를 취소합니다.")
    
    # 10초 동안 키 입력 대기
    for _ in range(10):
        time.sleep(1)
        if msvcrt.kbhit():  # 키 입력이 감지되면
            key = msvcrt.getch()  # 입력된 키를 가져옴
            if key == b'w':  # 'w' 키가 입력되었는지 확인
                print("'w' 키가 입력되어 종료가 취소되었습니다.")
                return False
    
    return True

while True:
    if should_shutdown():
        # 컴퓨터 종료 (운영체제에 맞는 명령 사용)
        if os.name == 'nt':  # Windows
            os.system("shutdown /s /t 1")
        else:  # Mac 또는 Linux
            os.system("shutdown -h now")
    else:
        break  # 'w' 키가 입력되면 루프 종료
