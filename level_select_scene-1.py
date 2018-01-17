# Created by: Gavin Zhou
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from main_menu_scene import *

import ui

from main_game_scene_one import *
from main_game_scene_two import *
from main_game_scene_three import *
from main_game_scene_four import *
from main_game_scene_five import *

class level_select_Scene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background 
        self.level_select_background = SpriteNode('./assets/sprites/level_select_background.jpg',
                                                  parent = self, 
                                                  position = self.size / 2, 
                                                  size = self.size)
        # add level select button 1-5
        level_select_button1 = self.size/2
        level_select_button1.x = level_select_button1.x - 400
        self.level_select_button1 = SpriteNode('./assets/sprites/level_select_button_1.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 2)



        level_select_button2 = self.size/2
        level_select_button2.x = level_select_button2.x - 200
        self.level_select_button2 = SpriteNode('./assets/sprites/level_select_button_2.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 2)



        level_select_button3 = self.size/2
        level_select_button3.x = level_select_button3.x + 0
        self.level_select_button3 = SpriteNode('./assets/sprites/level_select_button_3.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 2)



        level_select_button4 = self.size/2
        level_select_button4.x = level_select_button4.x + 200
        self.level_select_button4 = SpriteNode('./assets/sprites/level_select_button_4.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 2)



        level_select_button5 = self.size/2
        level_select_button5.x = level_select_button5.x + 400
        self.level_select_button5 = SpriteNode('./assets/sprites/level_select_button_5.PNG',
                                              parent = self,
                                              position = self.size/2,
                                              scale = 2)



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
        # if level button1 is pressed, goto main game scene1
        if self.level_select_button1.frame.contains_point(touch.location):
            self.main_game_scene_one(GameScene())

        # if start button2 is pressed, goto main game scene2
        if self.level_select_button2.frame.contains_point(touch.location):
            self.main_game_scene_two(GameScene())

        # if start button3 is pressed, goto main game scene3
        if self.level_select_button3.frame.contains_point(touch.location):
            self.main_game_scene_three(GameScene())

        # if start button4 is pressed, goto main game scene4
        if self.level_select_button4.frame.contains_point(touch.location):
            self.main_game_scene_four(GameScene())

        # if start button5 is pressed, goto main game scene5
        if self.level_select_button5.frame.contains_point(touch.location):
            self.main_game_scene_five(GameScene())
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
    
