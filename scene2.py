import os
import pygame
from button import Button
import sys
import random
import time
from statistics_page import StatisticsPage
from datetime import datetime





class Scene2:
    def __init__(self, screen):
        self.statistics_page = StatisticsPage(screen)
        self.screen = screen
        self.width, self.height = pygame.display.get_surface().get_size()

        self.questions_answered = 0
        self.questions_answered_correctly = 0

        if self.questions_answered > 0:
            self.accuracy = (self.questions_answered_correctly / self.questions_answered) * 100
        else:
            self.accuracy = 100
        
         
        


        # Load gems from the text file
        self.load_gems(self.accuracy)


        self.wrong = 0
        self.colordark = (230, 177, 197)
        self.firstQ = True
        self.var = ""
        self.gemsstring = str(self.gems)

        self.base_font = pygame.font.Font(None, 32)
        self.gems_text_surface = self.base_font.render(self.gemsstring, True, (255, 255, 255))
        self.text_surface = self.base_font.render(self.var, True, (255, 255, 255))

        self.input_rect = pygame.draw.rect(self.screen, self.colordark, pygame.Rect(50, 180, 275, 33))
        self.gem_picture_rect = pygame.draw.rect(self.screen, self.colordark, pygame.Rect(24, 24, 100, -10))
        self.gem_rect = pygame.draw.rect(self.screen, self.colordark, pygame.Rect(64, 24, 100, -10))

        # create button
        self.button = Button(screen, "<--", 50, 50, 50, 50, font_size=35, type="circle")

        # create the calculator
        button_size = 70
        ws = 30 #word size
        ns = 45 #number size

        self.delete = Button(screen, "delete", 90 , 580, button_size, button_size,  self.colordark, font_size=ws-3, type="circle")
        self.zero = Button(screen, "0", 190 , 580, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.enter = Button(screen, "enter", 290 , 580, button_size, button_size,  self.colordark, font_size=ws, type="circle")
        self.one = Button(screen, "1", 90 , 480, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.two = Button(screen, "2", 190 , 480, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.three = Button(screen, "3", 290 , 480, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.four = Button(screen, "4", 90 , 380, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.five = Button(screen, "5", 190 , 380, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.six = Button(screen, "6", 290 , 380, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.seven = Button(screen, "7", 90 , 280, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.eight = Button(screen, "8", 190 , 280, button_size, button_size,  self.colordark, font_size=ns, type="circle")
        self.nine = Button(screen, "9", 290 , 280, button_size, button_size, self.colordark, font_size=ns, type="circle")

    def getquestion(self):
        question_font = pygame.font.SysFont("Consolas", 50)
        number1 = random.randrange(0, 13)
        number2 = random.randrange(0, 13)
        self.answer = number1 * number2
        question = str(number1) + " x " + str(number2)
        self.question_text_surface = question_font.render(question, True, (230, 177, 197))
        
    def draw_scene(self):
        mathimg = pygame.image.load('math.jpg')
        self.screen.blit(mathimg, (0,0))

        self.button.draw()
        self.delete.draw()
        self.zero.draw()
        self.enter.draw()
        self.one.draw()
        self.two.draw()
        self.three.draw()
        self.four.draw()
        self.five.draw()
        self.six.draw()
        self.seven.draw()
        self.eight.draw()
        self.nine.draw()
        if self.wrong > 0:
            wrong_input = self.base_font.render("Try again!", True, (230,177,197))
            self.screen.blit(wrong_input, (255,33))
        
        # Render the user input (self.var)
        input_font = pygame.font.Font(None, 35)
        input_surface = input_font.render(self.var, True, (230, 177, 197))  # Update text color here
        self.screen.blit(input_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

        # Update the gemstr (self.gemsstring) with the correct value of self.gems
        self.gemsstring = "{:.2f}".format(self.gems)
        # Render the gemstr (self.gemsstring)
        gems_font = pygame.font.Font(None, 32)
        gems_surface = gems_font.render(self.gemsstring, True, (230, 177, 197))  # Update text color here
        self.screen.blit(gems_surface, (self.gem_rect.x + 68, self.gem_rect.y + 16))

        pygame.draw.rect(self.screen, (240, 200, 220), self.input_rect, 2)  # Update rect color here
        pygame.draw.rect(self.screen, (255,255,255), self.gem_picture_rect, 2)  # Update rect color here
        pygame.draw.rect(self.screen, (255,255,255), self.gem_rect, 2)  # Update rect color here

        self.screen.blit(pygame.image.load('Icons/gem.png'), (self.gem_picture_rect.x + 70, self.gem_picture_rect.y + 12))

        # Display the question
        if self.firstQ:
            self.getquestion()
            self.firstQ = False
        self.screen.blit(self.question_text_surface, (108, 100))

        pygame.display.update()
    
    def get_gems(self):
        return self.gemsstring
    
    def load_gems(self, accuracy):
    # Load gems from the text file if it exists, otherwise set it to 0
        if os.path.exists("gems.txt"):
            with open("gems.txt", "r") as file:
                content = file.read().strip()
                if content:
                    gems = float(content)
                    self.gems = gems
                   # x = datetime.datetime.now(datetime)
                    if self.questions_answered > 0:
                        self.accuracy = (self.questions_answered_correctly / self.questions_answered) * 100
                        self.statistics_page.save_data(datetime.today().strftime("%m-%Y"), int(accuracy))
                    else:
                        self.accuracy = 100
                        self.statistics_page.save_data(datetime.today().strftime("%m-%Y"), int(accuracy))
                else:
                    self.gems = 0.00
        else:
            self.gems = 0.00

    def set_gems(self, decrease, increase):
        if decrease > 0:
            self.gems -= decrease
        if increase > 0:
            self.gems += increase

        self.gemsstring = "{:.2f}".format(self.gems)  # Update self.gemsstring
        # Save the score (gems) to the text file
        with open("gems.txt", "w") as file:
            file.write(str(self.gems))
        self.load_gems(self.accuracy)


    def check_button_pressed(self, point):

        if self.button.check_collision(point):
            return "Scene1"
        if self.zero.check_collision(point):
            self.var += "0"
        if self.one.check_collision(point):
            self.var += "1"
        if self.two.check_collision(point):
            self.var += "2"
        if self.three.check_collision(point):
            self.var += "3"
        if self.four.check_collision(point):
            self.var += "4"
        if self.five.check_collision(point):
            self.var += "5"
        if self.six.check_collision(point):
            self.var += "6"
        if self.seven.check_collision(point):
            self.var += "7"
        if self.eight.check_collision(point):
            self.var += "8"
        if self.nine.check_collision(point):
            self.var += "9"

        if self.delete.check_collision(point):
            # get text input from 0 to -1 i.e. end.
            self.var = self.var[:-1]
            self.text_surface = self.base_font.render(self.var, True, (255, 255, 255))

        if self.enter.check_collision(point):        
            if (str(self.answer) == str(self.var)):
                self.questions_answered +=1
                self.var = ""  # Reset self.var to an empty string
                self.getquestion()
                #pygame.display.flip()

                if self.wrong == 0:
                    self.set_gems(0,1)
                    self.questions_answered_correctly +=1
                elif self.wrong == 1:
                    self.set_gems(0,0.5)
                    self.questions_answered_correctly -=0.25
                elif self.wrong == 2:
                    self.set_gems(0,0.25)
                    self.questions_answered_correctly -=0.25
                elif self.wrong >= 3:
                    self.gems += 0
                    self.questions_answered_correctly -=0.5
                self.wrong = 0
            else:
                self.wrong+=1
                self.var=""
                
            x = self.gemsstring.split(".")
            if len (x[1])<2:
                self.gemsstring+="0"
            self.gems_text_surface = self.base_font.render(self.gemsstring, True, (255, 255, 255))

        return None
