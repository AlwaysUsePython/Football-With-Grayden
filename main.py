import pygame
import math
import random
import time

pygame.init()
screen = pygame.display.set_mode((1000, 650))

font = pygame.font.Font('freesansbold.ttf', 60)

def copyList(arr):
    newArr = []
    for item in arr:
        newArr.append(item)
    return newArr

def drawYardMarks(position):
    startYard = float(format(position - 10, ".4f"))

    if startYard >= 60:
        startYard = 60

    elif startYard <= -10:
        startYard = -10

    for i in range(2000):
        yardLine = float(format(startYard + float(format(i / 40, ".4f")), ".4f"))
        #print(yardLine)
        #ready = input()
        if yardLine // 1 == yardLine:
            if yardLine == 100:
                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect(i/2, 25, 200, 600))
                return
            elif yardLine == 0:
                pygame.draw.rect(screen, (100, 0, 0), pygame.Rect(i / 2 - 200, 25, 200, 600))
            elif yardLine > 0:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i/2, 25, 2, 20))
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i/2, 605, 2, 20))
                if yardLine % 5 == 0:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i/2, 45, 2, 20))
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i/2, 625-40, 2, 20))
                if yardLine % 10 == 0:
                    if yardLine > 0 and yardLine < 100:
                        text1 = "0"
                        text1 = font.render(text1, True, (255, 255, 255))
                        text1Rect = text1.get_rect()
                        text1Rect.center = (i/2 + 30, 85)
                        screen.blit(text1, text1Rect)

                        text2Rect = text1.get_rect()
                        text2Rect.center = (i / 2 + 30, 650 - 85)
                        screen.blit(text1, text2Rect)
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i/2, 25, 2, 600))

                        text2 = str(int(5-abs(5 - (yardLine // 10))))
                        text2 = font.render(text2, True, (255, 255, 255))
                        text3Rect = text1.get_rect()
                        text3Rect.center = (i / 2 - 30, 85)
                        screen.blit(text2, text3Rect)

                        text4Rect = text2.get_rect()
                        text4Rect.center = (i / 2 - 30, 650 - 85)
                        screen.blit(text2, text4Rect)

                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i / 2, 25, 2, 600))
                if yardLine == 30:
                    pygame.draw.rect(screen, (70, 30, 175), pygame.Rect(i/2-1, 25, 4, 600))
                if yardLine == 40:
                    pygame.draw.rect(screen, (200, 200, 50), pygame.Rect(i/2-1, 25, 4, 600))



def drawBall(position, y):
    if position < 70 and position > 0:
        pygame.draw.rect(screen, (100, 50, 20), pygame.Rect(200-7, y+5, 14, 10))

    else:
        if position > 70:
            pygame.draw.rect(screen, (100, 50, 20), pygame.Rect(200 - 7 + 20*(position - 70), y +5, 14, 10))
        if position < 0:
            pygame.draw.rect(screen, (100, 50, 20), pygame.Rect(200 - 7 + 20*(position), y +5, 14, 10))


def drawPlayerWithBall(position, y):
    if position < 70 and position > 0:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200-10, y-10, 20, 20))
        pygame.draw.rect(screen, (255, 120, 0), pygame.Rect(200 - 9, y - 9, 18, 18))
    else:
        if position > 70:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200 - 10 + 20*(position - 70), y - 10, 20, 20))
            pygame.draw.rect(screen, (255, 120, 0), pygame.Rect(200 - 9 + 20*(position - 70), y - 9, 18, 18))
        if position < 0:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200 - 10 + 20*(position), y - 10, 20, 20))
            pygame.draw.rect(screen, (255, 120, 0), pygame.Rect(200 - 9 + 20*(position), y - 9, 18, 18))

def drawPlayerWithoutBall(ballSpot, yardLine, y, color):
    if ballSpot < 70 and ballSpot > 0:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200 - 10 + 20 * (yardLine - ballSpot), y - 10, 20, 20))
        pygame.draw.rect(screen, color, pygame.Rect(200 - 9 + 20*(yardLine - ballSpot), y - 9, 18, 18))

    elif ballSpot <= 0:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200 - 10 + 20 * (yardLine), y - 10, 20, 20))
        pygame.draw.rect(screen, color, pygame.Rect(200 - 9 + 20 * (yardLine), y - 9, 18, 18))

    elif ballSpot >= 70:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200 - 10 + 20 * (yardLine - 70), y - 10, 20, 20))
        pygame.draw.rect(screen, color, pygame.Rect(200 - 9 + 20 * (yardLine-70), y - 9, 18, 18))

def detectCollision(playerYardline, playerY, opponentYardline, opponentY):
    if abs(playerYardline - opponentYardline) <= 1:
        if abs(playerY - opponentY) <= 20:
            return True
    return False
def drawBackground(position):
    #print(position)
    screen.fill((20, 180, 0))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 1000, 25))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 625, 1000, 25))
    drawYardMarks(position)

def detectCatch(ballX, ballY, receiverX, receiverY):
    if abs(ballX - receiverX) <= 1:
        if abs(receiverY - ballY) <= 10:
            return True
    return False

def playGame():
    player = [25, 325, 0, 0]
    ball = [25, 325, 0, 0, 0, 0]
    opponent = [40, 325, 0, 0]
    opponent2 = [37, 100, 0, 0]
    opponent3 = [37, 550, 0, 0]
    receiver = [29, 100, 0, 0]
    receiver2 = [29, 550, 0, 0]
    ol = [30, 325, 10]
    formerOpponentDeltaX = -1/30

    route2 = [[35, 550, 6, 0], [60, 50, 25, -500]]

    ballTarget = [-1, -1]
    holdingBall = True
    catchable = False
    speed = 30
    thrown = False
    scrimage = False
    start = time.time()
    stage = 0
    picked = False
    while True:

        if picked:
            return "INTERCEPTION"
        current = time.time()
        gap = current - start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if stage == 0:
                    if event.key == pygame.K_SPACE:
                        stage += 1

                if stage > 0:
                    if event.key == pygame.K_d:
                        player[2] = 1
                    if event.key == pygame.K_a:
                        player[2] = -1

                    if event.key == pygame.K_w:
                        player[3] = -5
                    if event.key == pygame.K_s:
                        player[3] = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player[3] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player[2] = 0

            if stage > 0 and not scrimage:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    thrown = True
                    pos = pygame.mouse.get_pos()
                    ballTarget = [pos[0], pos[1]]
                    yardTarget = yardline + (ballTarget[0]-200)/20
                    if ballTarget[0] > ball[0]:
                        ball[2] = 1/5
                    else:
                        ball[2] = -1/5
                    xDist = ballTarget[0] - 200

                    #print(xDist)
                    #ready = input()
                    yDist = ballTarget[1] - ball[1]
                    thrownX = yardline
                    #print(yDist)
                    ball[3] = ball[2] * 20 * yDist / xDist
                    holdingBall = False
                    ball[5] = 5

        player[0] += player[2] / 20

        if not holdingBall and catchable:
            if detectCatch(receiver[0], receiver[1], ball[0], ball[1]):
                storage = copyList(player)
                player = copyList(receiver)
                receiver = copyList(storage)
                holdingBall = True

            if detectCatch(receiver2[0], receiver2[1], ball[0], ball[1]):


                storage = copyList(player)
                player = copyList(receiver2)
                receiver2 = copyList(storage)
                holdingBall = True

            if detectCatch(opponent2[0], opponent2[1], ball[0], ball[1]):
                picked = True

            if detectCatch(opponent3[0], opponent3[1], ball[0], ball[1]):
                picked = True

        if stage > 0 and not thrown:
            receiver[0] += 1/20
            if receiver2[0] < route2[0][0]:
                receiver2[0] += 1/20
                receiver2[1] += (1 / (route2[0][2]*20))*route2[0][3]
            elif receiver2[0] < route2[1][0]:
                receiver2[0] += 1 / 20
                receiver2[1] += (1 / (route2[1][2]*20))*route2[1][3]
        elif stage > 0 and thrown:
            if receiver[0] < yardTarget-0.2:
                receiver[0] += 1/20
            if receiver[0] > yardTarget-0.2:
                receiver[0] -= 1/20
            if receiver[1] < ballTarget[1]:
                receiver[1] += 0.75
            elif receiver[1] > ballTarget[1]:
                receiver[1] += -0.75

            if receiver2[0] < yardTarget-0.2:
                receiver2[0] += 1/20
            if receiver2[0] > yardTarget-0.2:
                receiver2[0] -= 1/20
            if receiver2[1] < ballTarget[1]:
                receiver2[1] += 0.75
            elif receiver2[1] > ballTarget[1]:
                receiver2[1] += -0.75



        player[0] = float(format(player[0], ".4f"))
        if player[0] < -10:
            player[0] = -10
        elif player[0] > 110:
            player[0] = 110
        yardline = ball[0]
        player[1] += player[3]*gap*speed
        if player[1] < 0:
            player[1] = 0
        elif player[1] > 650:
            player[1] = 650
        if holdingBall:
            ball = [player[0], player[1], player[2], player[3], 0, 0]
        else:
            if ball[1] < 25 or ball[1] > 625:
                return "INCOMPLETE PASS"
            elif abs(ball[1] - ballTarget[1]) >= 2 or abs(20* (ball[0] - thrownX) - (ballTarget[0]-200)) >= ball[2]*20:
                """print("Y")
                print(ball[1])
                print(ballTarget[1])
                print("X")
                print(20*(ball[0] - thrownX))
                print(ballTarget[0] - 200)
                print()"""
                #ready = input()
                ball[0] += ball[2]
                ball[1] += ball[3]

                if abs(ball[1] - ballTarget[1]) <= 80 and abs(20 * (ball[0] - thrownX) - (ballTarget[0]-200)) <= ball[2]*600:
                    catchable = True
            else:
                return "INCOMPLETE PASS"
            #print(ball[1])

        drawBackground(yardline)
        #print(player[0], player[1])
        if holdingBall:
            drawPlayerWithBall(player[0], player[1])
        else:
            drawPlayerWithoutBall(yardline, player[0], player[1], (255, 120, 0))
        if stage > 0:
            drawBall(ball[0], ball[1])
        drawPlayerWithoutBall(yardline, ol[0], ol[1], (255,120,0))
        drawPlayerWithoutBall(yardline, opponent[0], opponent[1], (0, 0, 0))
        drawPlayerWithoutBall(yardline, opponent2[0], opponent2[1], (0, 0, 0))
        drawPlayerWithoutBall(yardline, opponent3[0], opponent3[1], (0, 0, 0))
        drawPlayerWithoutBall(yardline, receiver[0], receiver[1], (255, 120, 0))
        drawPlayerWithoutBall(yardline, receiver2[0], receiver2[1], (255, 120, 0))
        pygame.display.update()
        if holdingBall and player[1] > 615:
            return yardline - 30
        elif holdingBall and player[1] < 35:
            return yardline - 30
        if holdingBall and player[0] > 100:
            return "TOUCHDOWN!!"
        elif holdingBall and player[0] <= -10:
            return "SAFETY :("
        if holdingBall and detectCollision(player[0], player[1], opponent[0], opponent[1]):
            if yardline < 0:
                return "SAFETY :("
            else:
                return yardline - 30

        if player[0] > opponent[0]:
            opponent[2] = 1/25
        elif player[0] == opponent[0]:
            opponent[2] = 0
        else:
            opponent[2] = -1/25

        isCollidingWithOL = detectCollision(ol[0], ol[1], opponent[0], opponent[1])
        if isCollidingWithOL:
            formerOpponentDeltaX = opponent[2]
            opponent[2] = opponent[2] / ol[2]

        if player[1] > opponent[1]:
            opponent[3] = 5
        elif player[1] == opponent[1]:
            opponent[3] = 0
        else:
            opponent[3] = -5
        if stage > 0:
            opponent[0] += opponent[2]
            opponent[1] += opponent[3]*gap*25

        if thrown and holdingBall or (not thrown and scrimage):
            if player[0] > opponent2[0]:
                opponent2[2] = 1 / 19
            elif player[0] == opponent2[0]:
                opponent2[2] = 0
            else:
                opponent2[2] = -1 / 19
            if player[1] > opponent2[1]:
                opponent2[3] = 5
            elif player[1] == opponent2[1]:
                opponent2[3] = 0
            else:
                opponent2[3] = -5
            if stage > 0:
                opponent2[0] += opponent2[2]
                opponent2[1] += opponent2[3] * gap * 25

            if detectCollision(yardline, player[1], opponent2[0], opponent2[1]):
                return yardline - 30

            if player[0] > opponent3[0]:
                opponent3[2] = 1 / 19
            else:
                opponent3[2] = -1 / 19
            if player[1] > opponent3[1]:
                opponent3[3] = 5
            else:
                opponent3[3] = -5
            if stage > 0:
                opponent3[0] += opponent3[2]
                opponent3[1] += opponent3[3] * gap * 25

            if detectCollision(yardline, player[1], opponent3[0], opponent3[1]):
                return yardline - 30

        else:
            if receiver[0] > opponent2[0]:
                opponent2[2] = 1 / 30
            else:
                opponent2[2] = -1 / 30
            if receiver[1] > opponent2[1]:
                opponent2[3] = 5
            else:
                opponent2[3] = -5
            if stage > 0:
                opponent2[0] += opponent2[2]
                opponent2[1] += opponent2[3] * gap * 25

            if receiver2[0] > opponent3[0]:
                opponent3[2] = 1 / 30
            else:
                opponent3[2] = -1 / 30
            if receiver2[1] > opponent3[1]:
                opponent3[3] = 5
            else:
                opponent3[3] = -5
            if stage > 0:
                opponent3[0] += opponent3[2]
                opponent3[1] += opponent3[3] * gap * 25

        #print(gap)
        #print(speed)
        #print(opponent)
        if yardline > 30:
            scrimage = True
        start = current
        #ready = input()


def displayYards(yards):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    return

        screen.fill((100, 200, 150))
        if yards == "TOUCHDOWN!!":
            text = yards
        elif yards == "SAFETY :(":
            text = yards
        elif yards == "INCOMPLETE PASS":
            text = yards
        elif yards == "INTERCEPTION":
            text = yards
        else:
            text = "You gained " + format(yards, ".2f")+ " yards."
            if yards >= 10:
                text2 = "FIRST DOWN!!"
                text2 = font.render(text2, True, (255, 255, 255))
                textRect = text2.get_rect()
                textRect.center = (500, 400)
                screen.blit(text2, textRect)

        text = font.render(text, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (500, 325)
        screen.blit(text, textRect)



        pygame.display.update()

while True:
    yards = playGame()
    time.sleep(1)
    displayYards(yards)
