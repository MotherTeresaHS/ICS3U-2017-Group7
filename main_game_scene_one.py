# peter
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from numpy import random


class main_game_scene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.fishes = []
        self.fishes_move_speed = 10.0
        self.scale_size = 0.75
        self.fish_rate = 1
        
        # add background color
        background_position = Vector2(self.screen_center_x,
                                      self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/main_game_scene_one.jpg',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
                                     
        player_position = Vector2()
        player_position.x = self.screen_center_x
        player_position.y = 100
        self.player = SpriteNode('./assets/sprites/player_fish.PNG',
                                 parent = self,
                                 position = player_position,
                                 scale = 0.1)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        fish_create_chance = random.randint(1,25)
        if fish_create_chance <= self.fish_rate:
            self.add_fish_three()
        fish_create_chance = random.randint(1,25)
        if fish_create_chance <= self.fish_rate:
            self.add_fish_two()
        fish_create_chance = random.randint(1,25)
        if fish_create_chance <= self.fish_rate:
            self.add_fish()
        
        if len(self.fishes) > 0:
           for fish_hit in self.fishes:
               if fish_hit.frame.intersects(self.player.frame):
                  self.player.remove
                  fish_hit.remove
                  self.fishes.remove(fish_hit)
        else:
         pass
         
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        player = self.size/2
        player.x = player.x+0
        self.player = SpriteNode('./assets/sprites/player_fish.png')
        
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        if self.player.frame.contains_point(touch.location):
            self.player.position = touch.location
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
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
        fish_start_position = Vector2()
        fish_start_position.x = self.size_of_screen_x - 100
        fish_start_position.y = random.randint(10, 
                                         self.size_of_screen_y - 100)
        
        fish_end_position = Vector2()  
        fish_end_position.x = - 100
        fish_end_position.y = random.randint(100,
                                       self.screen_center_y - 100)
        
        self.fishes.append(SpriteNode('./assets/sprites/small_fish.PNG',
                                      position = fish_start_position,
                                      parent = self,
                                      scale = 0.12)) 
                             
        fishMoveAction = Action.move_to(fish_end_position.x,
                                        fish_end_position.y,
                                        self.fishes_move_speed,
                                        TIMING_SINODIAL)
                                        
        self.fishes[len(self.fishes)-1].run_action(fishMoveAction)      
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    def add_fish_two(self):
        fish_start_position = Vector2()
        fish_start_position.x = self.size_of_screen_x - 100
        fish_start_position.y = random.randint(100, 
                                         self.size_of_screen_y - 100)
        
        fish_end_position = Vector2()  
        fish_end_position.x = - 100
        fish_end_position.y = random.randint(100,
                                       self.screen_center_y - 100)
        
        self.fishes.append(SpriteNode('./assets/sprites/medium_fish.PNG',
                                      position = fish_start_position,
                                      parent = self,
                                      scale = 0.12)) 
                             
        fishMoveAction = Action.move_to(fish_end_position.x,
                                        fish_end_position.y,
                                        self.fishes_move_speed,
                                        TIMING_SINODIAL)
                                        
        self.fishes[len(self.fishes)-1].run_action(fishMoveAction)     
        
    def add_fish_three(self):
        fish_start_position = Vector2()
        fish_start_position.x = self.size_of_screen_x - 100
        fish_start_position.y = random.randint(100, 
                                         self.size_of_screen_y - 100)
        
        fish_end_position = Vector2()  
        fish_end_position.x = - 150
        fish_end_position.y = random.randint(10,
                                       self.screen_center_y - 100)
        
        self.fishes.append(SpriteNode('./assets/sprites/large_fish.PNG',
                                      position = fish_start_position,
                                      parent = self,
                                      scale = 0.18)) 
                             
        fishMoveAction = Action.move_to(fish_end_position.x,
                                        fish_end_position.y,
                                        self.fishes_move_speed,
                                        TIMING_SINODIAL)
                                        
        self.fishes[len(self.fishes)-1].run_action(fishMoveAction)
