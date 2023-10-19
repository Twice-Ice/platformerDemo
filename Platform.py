import pygame;

class Platform:
    def __init__(self, topLeft, bottomRight, color):
        self.minX, self.minY = topLeft
        self.maxX, self.maxY = bottomRight
        self.sizeX = bottomRight[0] - topLeft[0]
        self.sizeY = bottomRight[1] - topLeft[1]
        self.color = color
        print("AHH OH GOD WHY DO I EXIS?!?!?!?! PLEASE HELP ME OH FOR THE LOVE OF GOD, LIFE IS MISERABLE! AHHHHAHAHHAHAH AHHHHHH  HELP MEEEEEEEEEEEEEEEEEEEEEEEEE NOOOOOOOOOOOOOOOOOOO also ur mom.")


    def collide(self, playerX, playerY, playerSizeX, playerSizeY):

        if playerX+playerSizeX > self.minX and playerX< self.maxX and playerY + playerSizeY > self.minY and playerY < self.maxY:
            return True
        else:
            return False
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.minX, self.minY, self.sizeX, self.sizeY))

class BouncePad(Platform):
    def __init__(self, topLeft, bottomRight, color, bounciness):
        self.originalBounciness = bounciness
        self.bounciness = self.originalBounciness
        super().__init__(topLeft, bottomRight, color)

    def bounce(self, jom):
        if self.bounciness > 0:
            self.bounciness -= 0.025
        pygame.mixer.Sound.play(jom)
        return self.bounciness 

    def reset(self):
        self.bounciness = self.originalBounciness 
