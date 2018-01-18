# Created by: Gavin Zhou
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from main_menu_scene import *

import ui

class level_select_Scene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.level_select_background = SpriteNode('./assets/sprites/level_select_background.jpg',
                                                  parent = self, 
                                                  position = self.size / 2, 
                                                  size = self.size)
                                                  
        level_select_button1 = self.size/2
        level_select_button1.x = level_select_background1.x - 400
        self.level_select_button1 = SpriteNode('./assets/sprites/level_button_1.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 0.75)
        level_select_button2 = self.size/2
        level_select_button2.x = level_select_background2.x - 200
        self.level_select_button2 = SpriteNode('./assets/sprites/level_button_1.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 0.75)
        level_select_button3 = self.size/2
        level_select_button3.x = level_select_background3.x + 0
        self.level_select_button3 = SpriteNode('./assets/sprites/level_button_1.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 0.75)
        level_select_button4 = self.size/2
        level_select_button4.x = level_select_background4.x + 200
        self.level_select_button4 = SpriteNode('./assets/sprites/level_button_1.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 0.75)
        level_select_button5 = self.size/2
        level_select_button5.x = level_select_background5.x + 400
        self.level_select_button5 = SpriteNode('./assets/sprites/level_button_1.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 0.75)
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
    
