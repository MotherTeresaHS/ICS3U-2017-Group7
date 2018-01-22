# Created by: Gavin Zhou
# Created on: Jan 2016
# Created for: ICS3U

#This scene used when player lose

from scene import *
import ui

from main_menu_scene import *

# when user lose, turn to this scene
class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background 
        self.game_over_scene_background = SpriteNode('./assets/sprites/game_over_background.jpg',
                                                  parent = self, 
                                                  position = self.size / 2, 
                                                  size = self.size)
        home_button_position = self.size/2
        home_button_position.x = home_button_position.x - 200
        home_button_position.y = home_button_position.y - 280
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                              parent = self,
                                              position = home_button_position,
                                              scale = 0.3)

        play_button_position = self.size/2
        play_button_position.x = play_button_position.x + 200
        play_button_position.y = play_button_position.y - 280
        self.back_button = SpriteNode('./assets/sprites/play_button.PNG',
                                              parent = self,
                                              position = play_button_position,
                                              scale = 0.252)






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
        if self.home_button.frame.contains_point(touch.location):
            self.present_modal_scene(MainMenuScene())
        if self.play_button.frame.contains_point(touch.location):
            self.present_modal_scene(MainGameScene())
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
    
