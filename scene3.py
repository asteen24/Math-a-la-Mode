import pygame
from button import Button
import sys
import random
import time

class Scene3:
    def __init__(self, screen, scene2_instance):
        self.enough_money = False
        self.not_enough_money = False
        self.scene2_instance = scene2_instance

        self.purchased_dresses = []
        self.purchased_shirts = []
        self.purchased_bottoms= []
        self.purchased_bags = []
        self.purchased_shoes= []

        self.colordark = (230, 177, 197)
        self.gem_picture_rect = pygame.draw.rect(screen, self.colordark, pygame.Rect(24, 24, 100, -10))
        self.gem_rect = pygame.draw.rect(screen,  self.colordark, pygame.Rect(64, 24, 100, -10))
        self.show=True
        self.locked=True
        self.wardrobe = True
        self.clothing_shown=1
        self.count = 0
        self.end_loop = False
        self.max = 8
        self.category = ["Dresses", "Shirts", "Bottoms", "Bags", "Shoes"]
        self.outfit = [None, None, None, None, None]
        self.category_Dresses_price = ["0", "0", "20", "25", "30", "40", "60", "75", "100", "150"]
        self.category_Shirts_price = ["0", "0","30", "80"]
        self.category_Bottoms_price = ["0", "0","20", "40", "50", "70"]
        self.category_Bags_price = ["0", "0","50", "80", "100", "120", "160", "190"]
        self.category_Shoes_price = ["0", "0", "30", "60"]
        self.category_number = 0
        self.category_font = pygame.font.SysFont("inkfree", 20)
        self.gems_font = pygame.font.Font(None, 32)
        self.colornumber = 0
        self.backgroundnumber = 1
        self.screen = screen
        self.width, self.height = pygame.display.get_surface().get_size()
        # create button
        self.button = Button(screen, "<-", 20, 20, 50, 27.5, (101, 136, 140), (255,255,255), font_size=30, type="rectangle")
        self.hair = Button(screen, "Hair", 220, 567, 50, 27.5, (101, 136, 140), font_size=30,  type="rectangle")
        #self.category_name = Button(screen, self.category[self.category_number], 220, 567, 50, 27.5, (101, 136, 140), font_size=30,  type="rectangle")
        self.category_back = Button(screen, "<", 220, 90, 20, 15, (101, 136, 140), font_size=25,  type="rectangle")
        self.category_next = Button(screen, ">", 320, 90, 20, 15, (101, 136, 140), font_size=25,  type="rectangle")
        self.clothing_icons_back = Button(screen, "<", 220, 493, 50, 25, (39, 60, 60), (255, 255, 255), font_size=50,  type="rectangle")
        self.clothing_icons_next = Button(screen, ">", 280, 493, 50, 25, (39, 60, 60), (255, 255, 255), font_size=50,  type="rectangle")
        self.background = Button(screen, "AppDraft/Backgrounds/backgroundicon.png", 282, 566, 50, 27.5, (101, 136, 140), font_size=15, type="rectangle")
       
        self.refresh()
        
        self.dress1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
        self.dress2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

        self.shirt1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
        self.shirt2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

        self.bottom1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
        self.bottom2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

        self.bag1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
        self.bag2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

        self.shoe1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
        self.shoe2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

    def refresh(self):
        self.dress_icon_name = "AppDraft/Clothes/"+  str(self.category[self.category_number])+ "/icon" + str(self.clothing_shown) + ".png" #clothes changed when category changed
        self.dress_icon_name2 = "AppDraft/Clothes/"+  str(self.category[self.category_number])+ "/icon" + str(self.clothing_shown+1) + ".png" #clothes changed when category changed
        
        self.dress_name1 = "AppDraft/Clothes/"+  str(self.category[self.category_number])  +"/" +str(self.clothing_shown) + ".png" #clothes changed when category changed
        self.dress_name2 = "AppDraft/Clothes/"+  str(self.category[self.category_number])  +"/" +str(self.clothing_shown+1) + ".png" #clothes changed when category changed
        
        self.dress_display1 = pygame.image.load(self.dress_name1)
        self.dress_display2 = pygame.image.load(self.dress_name2)
        
    def draw_scene(self):
        background_color = (255, 255, 255)  # White in RGB

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60))
        
        number_of_gems = self.scene2_instance.get_gems()
        
        gems_surface = self.gems_font.render(number_of_gems, True, (230, 177, 197))  # Update text color here
        
        # Clear the screen with the background color
        self.screen.fill(background_color)
        xb=0
        yb=0
        xm=-5 #70
        ym=75 #50
        xw=189 #70
        yw=66.5 #50
        xh=-35
        yh=64

        
        color = ["red", "blonde", "brown", "black"]
        hair_color = "AppDraft/Models + Hair/hair " + color[self.colornumber] + ".png"
        background_image = "AppDraft/Backgrounds/b"+ str(self.backgroundnumber) +".jpg"
        open_wardrobe = "AppDraft/wardrobe.png"
        

        try:
            model = pygame.image.load("AppDraft/Models + Hair/real new full body.png")
            hair = pygame.image.load(hair_color)
            closet=pygame.image.load(open_wardrobe)
            background = pygame.image.load(background_image)

            self.screen.blit(background, (xb,yb))
            self.screen.blit(model, (xm,ym))

            self.screen.blit(gems_surface, (self.gem_rect.x + 68, self.gem_rect.y + 16))
            self.screen.blit(pygame.image.load('Icons/gem.png'), (self.gem_picture_rect.x + 70, self.gem_picture_rect.y + 12))
        

            self.screen.blit(closet, (xw, yw))

            self.hair.draw()
            self.background.draw()
            self.button.draw()
            #self.category.draw()
            self.category_back.draw()
            self.category_next.draw()
            self.clothing_icons_back.draw()
            self.clothing_icons_next.draw()
            category_surface = self.category_font.render((self.category[self.category_number]), True, (255, 255, 255))
            self.screen.blit(category_surface, (260, 90))

            if ((self.not_enough_money == False) and (self.enough_money == True)):
                enough_money = self.gems_font.render("purchased :)", True, (230,177,197))
                self.screen.blit(enough_money, (220,33))  
            elif ((self.not_enough_money == True) and (self.enough_money == False)):
                not_enough_money = self.gems_font.render("insufficient funds :(", True, (230,177,197))
                self.screen.blit(not_enough_money, (180,15))

            if all(x is None for x in self.outfit) == False:
                for i in range (0,5):#Max number of items on the model at a time (length of outfit list)

                    if self.outfit[i] == None:
                        #prevents the code from breaking if an item in the outfits list is set to none (i.e has not been pressed or set to none intentionaly)
                        continue
                    else:
                        #Displays the top buttons clothes on the model
                        if ((self.show == True) and (self.outfit[0] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (26,162))
                        elif ((self.show == True) and (self.outfit[1] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (55,168))
                        elif ((self.show == True) and (self.outfit[2] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (34, 277))
                        elif ((self.show == True) and (self.outfit[3] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (-30,330))
                        elif ((self.show == True) and (self.outfit[4] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (60,573))
                        #Displays the bottom buttons clothes on the model
                        if ((self.show == False) and (self.outfit[0] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (26,162))
                        elif ((self.show == False) and (self.outfit[1] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (55,168))
                        elif ((self.show == False) and (self.outfit[2] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (34, 277))
                        elif ((self.show == False) and (self.outfit[3] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (-30,330))
                        elif ((self.show == False) and (self.outfit[4] == self.outfit[i])):
                            self.screen.blit(self.outfit[i], (60,573))
                    

            if ((str(self.category[self.category_number])) == "Dresses"):
                self.dress1.draw()
                self.dress2.draw()
                self.add_lock(self.purchased_dresses,self.category_Dresses_price)
            
            elif ((str(self.category[self.category_number])) == "Shirts"):
                self.shirt1.draw()
                self.shirt2.draw()
                self.add_lock(self.purchased_shirts, self.category_Shirts_price)
            
            elif ((str(self.category[self.category_number])) == "Bottoms"):
                self.bottom1.draw()
                self.bottom2.draw()            
                self.add_lock(self.purchased_bottoms, self.category_Bottoms_price)
            
            elif ((str(self.category[self.category_number])) == "Bags"):
                self.bag1.draw()
                self.bag2.draw()            
                self.add_lock(self.purchased_bags, self.category_Bags_price)
            
            elif ((str(self.category[self.category_number])) == "Shoes"):
                self.shoe1.draw()
                self.shoe2.draw()
                self.add_lock(self.purchased_shoes, self.category_Shoes_price)

       
            if ((self.clothing_shown <=10) and (self.wardrobe == True)):
                
                self.refresh()

                self.dress1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle")
                self.dress2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 
                
                self.shirt1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
                self.shirt2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

                self.bottom1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
                self.bottom2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

                self.bag1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
                self.bag2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

                self.shoe1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
                self.shoe2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 

                self.jewelry1 = Button(self.screen, self.dress_icon_name, 213, 118, 130, 180, (101, 136, 140), type="rectangle") 
                self.jewelry2 = Button(self.screen, self.dress_icon_name2, 213, 295, 130, 192, (105, 136, 140), type="rectangle") 
            
            
            self.screen.blit(hair, (xh,yh))

            self.wardrobe = False

        except:
            self.clothing_shown=1

    def add_lock(self,purchased,price):

        self.screen.blit(pygame.image.load('Icons/gem_small.png'), (320, 118))
        self.screen.blit(pygame.image.load('Icons/gem_small.png'), (320, 295))

        if (self.category_number) == 0:
            category_Dresses_price_surface = self.category_font.render((self.category_Dresses_price[self.clothing_shown-1]), True, (255, 255, 255))
            self.screen.blit(category_Dresses_price_surface, (325, 118))
            category_Dresses_price_surface = self.category_font.render((self.category_Dresses_price[self.clothing_shown]), True, (255, 255, 255))
            self.screen.blit(category_Dresses_price_surface, (325, 295))
        elif (self.category_number) == 1:
            category_Shirts_price_surface = self.category_font.render((self.category_Shirts_price[self.clothing_shown-1]), True, (255, 255, 255))
            self.screen.blit(category_Shirts_price_surface, (325, 118))
            category_Shirts_price_surface = self.category_font.render((self.category_Shirts_price[self.clothing_shown]), True, (255, 255, 255))
            self.screen.blit(category_Shirts_price_surface, (325, 295))
        elif (self.category_number) == 2:
            category_Bottoms_price_surface = self.category_font.render((self.category_Bottoms_price[self.clothing_shown-1]), True, (255, 255, 255))
            self.screen.blit(category_Bottoms_price_surface, (325, 118))
            category_Bottoms_price_surface = self.category_font.render((self.category_Bottoms_price[self.clothing_shown]), True, (255, 255, 255))
            self.screen.blit(category_Bottoms_price_surface, (325, 295))
        elif (self.category_number) == 3:
            category_Bags_price_surface = self.category_font.render((self.category_Bags_price[self.clothing_shown-1]), True, (255, 255, 255))
            self.screen.blit(category_Bags_price_surface, (325, 118))
            category_Bags_price_surface = self.category_font.render((self.category_Bags_price[self.clothing_shown]), True, (255, 255, 255))
            self.screen.blit(category_Bags_price_surface, (325, 295))
        elif (self.category_number) == 4:
            category_Shoes_price_surface = self.category_font.render((self.category_Shoes_price[self.clothing_shown-1]), True, (255, 255, 255))
            self.screen.blit(category_Shoes_price_surface, (325, 118))
            category_Shoes_price_surface = self.category_font.render((self.category_Shoes_price[self.clothing_shown]), True, (255, 255, 255))
            self.screen.blit(category_Shoes_price_surface, (325, 295))

    def display_outfit(self,dress_display):
        if ((str(self.category[self.category_number])) == "Dresses"):
            self.outfit[0] = dress_display
            if self.outfit[0] != None:
                if ((self.outfit[1] or self.outfit[2]) != None):
                    self.outfit[1] = None
                    self.outfit[2] = None
        elif ((str(self.category[self.category_number])) == "Shirts"):
            self.outfit[1] = dress_display
            if self.outfit[1] != None:
                self.outfit[0] = None
        elif ((str(self.category[self.category_number])) == "Bottoms"):
            self.outfit[2] = dress_display
            if self.outfit[2] != None:
                self.outfit[0] = None
        elif ((str(self.category[self.category_number])) == "Bags"):
            self.outfit[3] = dress_display

        elif ((str(self.category[self.category_number])) == "Shoes"):
            self.outfit[4] = dress_display
            
        
    
    def buy_clothing(self, show, category_price, dress_display):
        
        if float(self.scene2_instance.get_gems()) >= float(category_price[self.clothing_shown - 1]):
            try:
                # Deduct gems and update scene 2's total
                if show:
                    self.scene2_instance.set_gems(float(category_price[self.clothing_shown - 1]), 0)
                else:
                    self.scene2_instance.set_gems(float(category_price[self.clothing_shown]), 0)
                self.show = show
                self.display_outfit(dress_display)
                self.enough_money = True
                self.not_enough_money = False
            except Exception as e:
                print("Exception in Scene3:", e)
        else:
            # Handle not enough gems
            self.not_enough_money = True
            self.enough_money = False


    def check_button_pressed(self, point):
        e = None
        try:
            
            if self.button.check_collision(point):
                return "Scene1"
            elif self.hair.check_collision(point):
                if self.colornumber > 2:
                    self.colornumber=0
                else:
                    self.colornumber+=1
            elif self.background.check_collision(point):
                if self.backgroundnumber > 4:
                    self.backgroundnumber=1
                else:
                    self.backgroundnumber+=1
            elif self.category_next.check_collision(point):
                self.clothing_shown = 1
                self.category_number += 1
                if self.category_number >= len(self.category):
                    self.category_number = 0
                self.refresh()
                self.wardrobe = True  # Set wardrobe to True to refresh clothing icons
            
            elif self.category_back.check_collision(point):
                self.category_number -= 1
                if self.category_number < 0:
                    self.category_number = len(self.category) - 1
                self.refresh()
                self.wardrobe = True  # Set wardrobe to True to refresh clothing icons
            
            elif self.clothing_icons_next.check_collision(point):
                if ((self.clothing_shown <=9) and (self.category_number == 0)):
                    self.clothing_shown+=2
                elif ((self.clothing_shown <=3) and (self.category_number == 1)):
                    self.clothing_shown+=2
                elif ((self.clothing_shown <=5) and (self.category_number == 2)):
                    self.clothing_shown+=2
                elif ((self.clothing_shown <=7) and (self.category_number == 3)):
                    self.clothing_shown+=2
                elif ((self.clothing_shown <=3) and (self.category_number == 4)):
                    self.clothing_shown+=2

                if ((self.clothing_shown>=9) and (self.category_number == 0)):
                    self.clothing_shown=9
                    self.clothing_icons_next = Button(self.screen, ">", 280, 493, 50, 25, (39, 60, 60), (180, 180, 180), font_size=50,  type="rectangle")
                elif ((self.clothing_shown>=3) and (self.category_number == 1)):
                    self.clothing_shown=3
                    self.clothing_icons_next = Button(self.screen, ">", 280, 493, 50, 25, (39, 60, 60), (180, 180, 180), font_size=50,  type="rectangle")
                elif ((self.clothing_shown>=5) and (self.category_number == 2)):
                    self.clothing_shown=5
                    self.clothing_icons_next = Button(self.screen, ">", 280, 493, 50, 25, (39, 60, 60), (180, 180, 180), font_size=50,  type="rectangle")
                elif ((self.clothing_shown>=7) and (self.category_number == 3)):
                    self.clothing_shown=7
                    self.clothing_icons_next = Button(self.screen, ">", 280, 493, 50, 25, (39, 60, 60), (180, 180, 180), font_size=50,  type="rectangle")
                elif ((self.clothing_shown>=3) and (self.category_number ==4)):
                    self.clothing_shown=3
                    self.clothing_icons_next = Button(self.screen, ">", 280, 493, 50, 25, (39, 60, 60), (180, 180, 180), font_size=50,  type="rectangle")
                self.wardrobe = True
            elif self.clothing_icons_back.check_collision(point):
                if self.clothing_shown >=2:
                    self.clothing_shown-=2
                    self.clothing_icons_next = Button(self.screen, ">", 280, 493, 50, 25, (39, 60, 60), (255, 255, 255), font_size=50,  type="rectangle")
                    self.clothing_icons_back = Button(self.screen, "<", 220, 493, 50, 25, (39, 60, 60), (255, 255, 255), font_size=50,  type="rectangle")
                else:
                    self.clothing_shown+=0
                    self.clothing_icons_back = Button(self.screen, "<", 220, 493, 50, 25, (39, 60, 60), (180, 180, 180), font_size=50,  type="rectangle")

                self.wardrobe = True

            elif self.dress1.check_collision(point):
                if ((str(self.category[self.category_number])) == "Dresses"):
                    if ((self.clothing_shown-1) not in self.purchased_dresses):
                        self.buy_clothing(True, self.category_Dresses_price, self.dress_display1)
                        if self.enough_money == True:
                            self.purchased_dresses.append(self.clothing_shown-1)
                    else:
                        self.show = True        
                        self.display_outfit(self.dress_display1)
                elif ((str(self.category[self.category_number])) == "Shirts"):
                    if ((self.clothing_shown-1)not in self.purchased_shirts):
                        self.buy_clothing(True, self.category_Shirts_price, self.dress_display1)
                        if self.enough_money == True:
                            self.purchased_shirts.append(self.clothing_shown-1)
                    else:
                        self.show = True        
                        self.display_outfit(self.dress_display1)
                elif ((str(self.category[self.category_number])) == "Bottoms"):
                    if ((self.clothing_shown-1)not in self.purchased_bottoms):
                        self.buy_clothing(True, self.category_Bottoms_price, self.dress_display1)
                        if self.enough_money == True:
                            self.purchased_bottoms.append(self.clothing_shown-1)
                    else:
                        self.show = True        
                        self.display_outfit(self.dress_display1)
                elif ((str(self.category[self.category_number])) == "Bags"):
                    if ((self.clothing_shown-1)not in self.purchased_bags):
                        self.buy_clothing(True, self.category_Bags_price, self.dress_display1)
                        if self.enough_money == True:
                            self.purchased_bags.append(self.clothing_shown - 1)
                    else:
                        self.show = True        
                        self.display_outfit(self.dress_display1)
                elif ((str(self.category[self.category_number])) == "Shoes"):
                    if ((self.clothing_shown-1) not in self.purchased_shoes):
                        self.buy_clothing(True, self.category_Shoes_price, self.dress_display1)
                        if self.enough_money == True:
                            self.purchased_shoes.append(self.clothing_shown - 1)
                    else:
                        self.show = True        
                        self.display_outfit(self.dress_display1)

                        
                
            elif self.dress2.check_collision(point):
                if ((str(self.category[self.category_number])) == "Dresses"):
                    if (self.clothing_shown not in self.purchased_dresses):
                        self.buy_clothing(False, self.category_Dresses_price, self.dress_display2)
                        if self.enough_money == True:
                            self.purchased_dresses.append(self.clothing_shown)
                    else:
                        self.show = False        
                        self.display_outfit(self.dress_display2)

                elif ((str(self.category[self.category_number])) == "Shirts"):
                    if (self.clothing_shown not in self.purchased_shirts):
                        self.buy_clothing(False, self.category_Shirts_price, self.dress_display2)
                        if self.enough_money == True:
                            self.purchased_shirts.append(self.clothing_shown)
                    else:
                        self.show = False        
                        self.display_outfit(self.dress_display2)

                elif ((str(self.category[self.category_number])) == "Bottoms"):
                    if (self.clothing_shown not in self.purchased_bottoms):
                        self.buy_clothing(False, self.category_Bottoms_price, self.dress_display2)
                        if self.enough_money == True:
                            self.purchased_bottoms.append(self.clothing_shown)
                    else:
                        self.show = False        
                        self.display_outfit(self.dress_display2)

                elif ((str(self.category[self.category_number])) == "Bags"):
                    if (self.clothing_shown not in self.purchased_bags):
                        self.buy_clothing(False, self.category_Bags_price, self.dress_display2)
                        if self.enough_money == True:
                            self.purchased_bags.append(self.clothing_shown)
                    else:
                        self.show = True        
                        self.display_outfit(self.dress_display2)

                elif ((str(self.category[self.category_number])) == "Shoes"):
                    if (self.clothing_shown not in self.purchased_shoes):
                        self.buy_clothing(False, self.category_Shoes_price, self.dress_display2)
                        if self.enough_money == True:
                            self.purchased_shoes.append(self.clothing_shown)
                    else:
                        self.show = True        
                        self.display_outfit(self.dress_display2)

        
                        
        except Exception as ex:
            e = ex
            print(f"Exception in Scene3: {type(e).__name__}: {e}")
        return None
