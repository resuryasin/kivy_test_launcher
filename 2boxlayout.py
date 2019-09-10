from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25

        self.box1 = BoxLayout(orientation='vertical', padding=25)
        self.box2 = BoxLayout(orientation='horizontal', padding=25)

        self.box1.add_widget(Button(text="satu", background_color=[1,0,0,1]))
        self.box1.add_widget(Button(text="dua", background_color=[0,1,0,1]))
        self.box1.add_widget(Button(text="tiga", background_color=[0,0,1,1]))

        self.box2.add_widget(Button(text="satu", background_color=[1,0,0,1]))
        self.box2.add_widget(Button(text="dua", background_color=[0,1,0,1]))
        self.box2.add_widget(Button(text="tiga", background_color=[0,0,1,1]))

        self.add_widget(self.box1)
        self.add_widget(self.box2)

class BoxLayoutDemo(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    BoxLayoutDemo().run()