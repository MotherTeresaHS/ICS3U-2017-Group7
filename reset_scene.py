# Created by: peter zhu
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows reset scene

from scene import *
import ui

from main_game_scene_one import *


class reset_scene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.reset_background = SpriteNode('./assets/sprites/reset_background.jpg',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
                                     
        yes_button = self.size/2
        yes_button.y = yes_button.y - 20
        yes_button.x = yes_button.x - 220
        self.yes_button = SpriteNode('./assets/sprites/yes_button.png',
                                              parent = self,
                                              position = yes_button,
                                              scale = 0.5)
                                              
        no_button = self.size/2
        no_button.y = yes_button.y - 5
        no_button.x = yes_button.x + 500
        self.no_button = SpriteNode('./assets/sprites/no_button.png',
                                              parent = self,
                                              position = no_button,
                                              scale = 0.5)
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
        
        if self.yes_button.frame.contains_point(touch.location):
            self.present_modal_scene(main_game_scene_one())
            
         #if self.no_button.frame.contains_point(touch.location):
            #self.main_menu_scene(GameScene())
         
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
    
