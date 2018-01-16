# Created by: Peter Zhu
# Created on: Dec 2018
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
from numpy import random

class main_game_scene_one(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background 
        self.main_game_background_one = SpriteNode('./assets/sprites/main_game_background_one.jpg', 
                                     parent = self,
                                     position = self.size / 2, 
                                     size = self.size)
                                     
        pause_button = self.size/2
        pause_button.x = pause_button.x + 0
        self.pause_button = SpriteNode('./assets/sprites/back_button.png',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 0.5)
                                              
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        fish_form_one = self.size/2
        fish_form_one.x = fish_form_one.x+0
        #self.fish_form_one = SpriteNode('./assets/sprites/fish_form_one.PNG')
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        #self.     .position = touch.location
        pass
    
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
    
