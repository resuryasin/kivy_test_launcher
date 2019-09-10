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
        self.cols = 1
        self.InnerGrid = GridLayout()
        self.InnerGrid.cols = 2

        self.InnerGrid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.InnerGrid.add_widget(self.name)

        self.InnerGrid.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.InnerGrid.add_widget(self.lastName)

        self.InnerGrid.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.InnerGrid.add_widget(self.email)

        self.add_widget(self.InnerGrid)
        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.displayText = TextInput(multiline=True, readonly=True, hint_text="Hasil akan tampil disini")
        self.add_widget(self.displayText)  
    def pressed(self, *args):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text
        self.displayText.text = "Name: "+name+"\nLast Name: "+last+"\nEmail: "+email


class GridLayoutDemo(App):
    def build(self):
        return MyBox()

if __name__ == '__main__':
    GridLayoutDemo().run()