import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong by ChewKaiQuan')

light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
text_font = pygame.font.Font('freesansbold.ttf', 16)

ball = pygame.Rect(screen_width/2 - 7.5, screen_height/2 - 7.5, 15,15)
player = pygame.Rect(screen_width - 10, screen_height/2 - 35, 5, 70)
opponent = pygame.Rect(1, screen_height/2 -35, 5,70)

ball_x_speed = 7
ball_y_speed = 7
player_speed = 0
opponent_speed = 8
player_score = 0
opponent_score = 0
score_time = None

def main():
    global player_speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_speed += 7
                if event.key == pygame.K_DOWN:
                    player_speed -= 7

        game_setup()
        ball_animation()
        player_animation()
        opponent_animation()

def game_setup():
    screen.fill(bg_color)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)

    player_text = text_font.render(str(player_score), True, light_grey)
    opponent_text = text_font.render(str(opponent_score), True, light_grey)
    screen.blit(player_text, (330, 235))
    screen.blit(opponent_text, (300, 235))

    pygame.display.flip()
    clock.tick(30)

def ball_animation():
    global ball_x_speed, ball_y_speed, opponent_score, player_score
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    if ball.left <= 0:
        player_score += 1
        ball_start()
    if ball.right >= screen_width:
        opponent_score += 1
        ball_start()
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_y_speed *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_x_speed *= -1

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_x_speed, ball_y_speed
    ball.center = (screen_width/2 ,screen_height/2)
    ball_x_speed *= random.choice((1,-1))
    ball_y_speed *= random.choice((1,-1))


main()


