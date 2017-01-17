# Created by: Anna Devlin
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game

from scene import *
import ui
from numpy import random
import sound

class GameScene(Scene):
    def setup(self):
        # this is called when user moves to the scene
        
        # size of screen variables are updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        #self.score = 0
        self.game_over = False
        self.score = 0
        self.stroke_began = False
        self.fish = []

        self.new_fish_rate = 3
        self.fishhook_enter_rate = 1
        self.game_over = False
        #self.score = 0
        
        # still not sure if these should be constants, so the variables which have not yet been changed in the body of the program are listed here:
        self.scale_size = 0.75
        self.fish_swim_speed = 20
        self.character_swim_speed = 0.8
        
        # constants, used to regulate game play
        self.SCALE_SIZE = 0.75
        self.FISH_SWIM_SPEED = 20
        self.CHARACTER_SWIM_SPEED = 0.8
        
        
        # add background image
        background_position = Vector2(self.screen_center_x, 
                              self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/ocean_background.jpg',
                                     position = background_position, 
                                     parent = self,
                                     size = self.size + (100,100))
                                     
        #add the main character to the screen
        self.character_position = Vector2(self.screen_center_x, 75)
        self.character = SpriteNode('./assets/sprites/character_facing_right.png',
                                     parent = self,
                                     position = self.size/2,
                                     size = self.size/6)
                                     
    def update(self):
        # this method is called 60 times a second to update the game
            
        # every update, randomly check if new fish should be added
        eatable_fish_create_chance = random.randint(1,120)
        if eatable_fish_create_chance <= self.new_fish_rate:
            self.add_fish()
            # call the eatable fish class
        
        # check every update if a fish is off screen
        for fish in self.fish:
            if fish.position.x > self.size_of_screen_x + 25:
                fish.remove_from_parent()
                self.fish.remove(fish)
                print("fish removed")
                print(len(self.fish))
                
        #check every update to see if the character has eaten a fish
        #if len(self.fish) > 0:
        for fish_eaten in self.fish:
            if self.fish.frame.intersects(self.character.frame):
                print("Fish was EATEN!")
                self.score += 100
                fish.remove_from_parent()
                self.fish.remove(fish_eaten)
        
        #check every update if a fish is off screen
        if len(self.fish) > 0:
                    for fish_off_screen in self.fish:
#            # THE FOLLOWING LINE OF CODE IS GETTING SYNTAX ERRORS
#                if fish_off_screen.position.x > int(self.size_of_screen_x + 10)
#                    fish_off_screen.remove_from_parent()
#                    self.fish.remove(fish_off_screen)

#for alien in self.aliens:
#            if alien.position.y < + 10:
#                alien.remove_from_parent()
#                self.aliens.remove(alien)
#                if self.game_over is False:
#                    self.score += -10
        
        #when the game ends, show a back to main menu button
        #if self.game_over is True:
        #    menu_button_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        #    self.menu_button = SpriteNode('./assets/sprites/menu_button.png',
        #                               parent = self,
        #                               position = right_button_position,
        #                               alpha = 0.5,
        #                               scale = self.scale_size)
        
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        if self.character.frame.contains_point(touch.location):
            self.stroke_began = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        # moves the character following user's finger
        
        character_aiming_point = Vector2(0,0)
        character_aiming_point.x = touch.location.x
        character_aiming_point.y = touch.location.y
        
        character_move_action = Action.move_to(character_aiming_point.x, 
                                 character_aiming_point.y, 
                                 self.character_swim_speed)
                                 
        if self.stroke_began == True:
            if touch.location.x < self.size_of_screen_x - 25 and touch.location.x > 25:
                if touch.location.y < self.size_of_screen_y - 25 and touch.location.y > 25:
                    self.character.run_action(character_move_action)
                    #if self.character.location.x > touch.location.x:
                    #    self.character.image = './assets/sprites/character_facing_right.png'
                    #if self.character.location.y < touch.location.y:
                    #    self.character.image = './assets/sprites/character_facing_right.png'
            #self.character.position = touch.location
                                         
        #print(len(self.fish))
        #self.fish[int(len(self.fish)-1)].run_action(fish_move_action)
            # add restrictions for sides of screen
                    
        #self.character_position = touch.location
        #self.character_position.y = touch.location.y
         #-1 * (self.character_position.x - touch.location.x)/3
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        self.stroke_began = False
            
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        
        # FIND A WAY TO KEEP IT LANDSCAPE
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
        
    def add_fish(self):
        #add new fish to enter into screen
        #based on alien scripting by Mr Coxall
        
        print("fish added")
        
        fish_start_position = Vector2(-200, 0)
        fish_start_position_y = random.randint(100, int(self.size_of_screen_y - 100))
        fish_start_position.y = fish_start_position_y
        
        fish_end_position = Vector2(0, 0)
        fish_end_position_x = int(self.size_of_screen_x + 100)
        fish_end_position_y = random.randint(100, int(self.size_of_screen_y - 100))
        fish_end_position.x = fish_end_position_x
        fish_end_position.y = fish_end_position_y
       
        # add a fish, just 
        self.fish.append(SpriteNode('./assets/sprites/fish.png',
                             position = fish_start_position,
                             scale = self.scale_size,
                             parent = self))

                                      
        # make fish move across the screen
        fish_move_action = Action.move_to(fish_end_position.x, 
                                         fish_end_position.y, 
                                         self.fish_swim_speed,
                                         TIMING_SINODIAL)
                                        
                                         
        print(len(self.fish))
        self.fish[int(len(self.fish)-1)].run_action(fish_move_action)
