from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 2

        self.add_widget(Button(text="satu", background_color=[1,0,0,1]))
        self.add_widget(Button(text="dua", background_color=[0,1,0,1]))
        self.add_widget(Button(text="tiga", background_color=[0,0,1,1]))
        self.add_widget(Button(text="empat", background_color=[1,0,0,1]))

        self.add_widget(Button(text="satu", background_color=[0,1,0,1]))
        self.add_widget(Button(text="dua", background_color=[0,0,1,1]))
        self.add_widget(Button(text="tiga", background_color=[1,0,0,1]))

class GridLayoutDemo(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    GridLayoutDemo().run()