# 1. 가상환경 생성
# python -m venv myenv (가상환경 이름)

# 2. 가상환경 활성화
#source myenv/bin/activate  # macOS/Linux
#myenv\Scripts\activate     # Windows

#.\activate (tap키)

# 3. 가상환경 내에서 필요한 패키지 설치
# pip install <패키지이름>

# 4. 작업 완료 후 가상환경 비활성화
# deactivate

import pygame

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame 종료
pygame.quit()
