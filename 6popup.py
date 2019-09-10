from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class MyBox(GridLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
        self.cols = 2

        self.Submit = Button()
        self.Submit.text = 'Submit'
        self.Submit.font_size = 20
        self.Submit.bind(on_press = lambda a:self.pressed(self.Submit.text))
        self.add_widget(self.Submit)  

        self.Cancel = Button()
        self.Cancel.text = 'Cancel'
        self.Cancel.font_size = 20
        self.Cancel.bind(on_press = lambda a:self.pressed(self.Cancel.text))
        self.add_widget(self.Cancel)  
    def pressed(self, *args):
        self.call_info(args[0])
    def call_info(self, text):
        content = BoxLayout(orientation='vertical')
        close_popup = Button(text='Close')
        error_message = Label(text="Click dari tombol "+text)
        content.add_widget(close_popup)
        content.add_widget(error_message)
        popup = Popup(title='Informasi',content=content, size_hint=(-4,-4))
        close_popup.bind(on_release=popup.dismiss)
        popup.open()



class GridLayoutDemo(App):
    def build(self):
        return MyBox()

if __name__ == '__main__':
    GridLayoutDemo().run()