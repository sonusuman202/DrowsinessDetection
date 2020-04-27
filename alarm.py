import pygame
import time
def playNotificationSound():
    pygame.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()
    time.sleep(10)
playNotificationSound()
