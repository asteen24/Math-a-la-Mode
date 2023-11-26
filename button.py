import pygame

class Button:

    def __init__(self, screen, text, x, y, width, height, color=(227, 200, 208), font_color=(255,235,245), font_size=35, type='rectangle'):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font_color = font_color
        self.type = type

        if type == 'rectangle':
            self.rect = pygame.Rect(x, y, width, height)
        elif type == 'circle':
            self.rect = pygame.Rect(x-width//2, y-width//2, width, width)

        self.font = pygame.font.SysFont('Roboto',font_size)

    def draw(self):
        if self.type == 'rectangle':
            pygame.draw.rect(self.screen, self.color, self.rect)
        elif self.type == 'circle':
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.width//2)

        if ".png" in self.text: 
            text = pygame.image.load(self.text).convert_alpha()
        else: 
            text=self.font.render(self.text, True, self.font_color)
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)
        

    def check_collision(self, point):
        # check if the point collides with the button
        
        if self.type == 'rectangle':
            pygame.draw.rect(self.screen, (211,186,196), self.rect)
        elif self.type == 'circle':
            pygame.draw.circle(self.screen, (211,186,196), (self.x, self.y), self.width//2)

        return self.rect.collidepoint(point)