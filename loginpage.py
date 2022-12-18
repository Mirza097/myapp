from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
Window.size = (350,580)

class LoginPage(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.login, 5)
        
    def login(self, *args):
        screen_manager.current = "login"
    
    def anim(self, widget):
        anim = Animation(pos_hint={"center_y": 1.16})
        anim.start(widget)
        
    def anim1(self, widget):
        anim = Animation(pos_hint={"center_y": .85})
        anim.start(widget)
        
    def icons(self, widget):
        anim = Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"center_y": .85})
        anim.start(widget)
        
    def text(self, widget):
        anim = Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)

if __name__ == "__main__":
    LoginPage().run()