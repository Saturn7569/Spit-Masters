import pygame, sys

pygame.init()

class GameWindow:
    def __init__(self):
        RES = self.WIDTH, self.HEIGHT = 320, 240

        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface(RES)

        self.clock = pygame.time.Clock()
        self.FPS = 60
    
    def end_tick(self):
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        pygame.display.update()
        self.clock.tick(self.FPS)

    def clear(self):
        self.screen.fill((255, 255, 255))
        self.display.fill((0, 0, 0))

    def run(self):
        while True:
            pygame.display.set_caption(str(int(self.clock.get_fps())))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                self.check_event(event)
            
            self.update()

            self.clear()

            self.draw()
            self.draw_UI()

            self.end_tick()

    def check_event(self, e:pygame.Event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def draw_UI(self):
        pass

if __name__ == "__main__":
    game = GameWindow()
    game.run()