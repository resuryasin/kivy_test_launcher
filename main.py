from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.config import Config

Config.set('graphics','resizable',0)
Config.set('graphics','width','400')

class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.cols = 1
        self.stash = ''
        self.topGrid = GridLayout()
        self.topGrid = TextInput(multiline=False, readonly=True)          
        self.topGrid.size_hint=(None,None)
        self.topGrid.height=100
        self.topGrid.width=400
        self.topGrid.font_size=20

        self.innerGrid = GridLayout()
        self.innerGrid.cols=4
        self.bottomGrid = GridLayout()
        self.bottomGrid.cols=4
        self.bottomGrid.size_hint=(.5,None)
        self.bottomGrid.height=100

        btnList = ['AC','+/-','del','/','1','2','3','*','4','5','6','+','7','8','9','-','0','.','=']

        for i in range(len(btnList)-3):
            self.innerGrid.add_widget(self.btnCreate(btnList[i]))
        for i in range(len(btnList)-3,len(btnList)):
            self.bottomGrid.add_widget(self.btnCreate(btnList[i]))

        self.add_widget(self.topGrid)  
        self.add_widget(self.innerGrid)
        self.add_widget(self.bottomGrid)

    def btnCreate(self, text):
        btn = Button()
        btn.text = text
        btn.font_size = 20
        btn.size_hint_x=None
        if text == '0':
            btn.width=200
        else:
            # pass
            btn.width=100
        if text in ('AC','+/-','del'):
            btn.background_color = [0,0,1,1]
        else:
            btn.background_color = [0.5,0.5,0.5,1]
        btn.bind(on_press = lambda a:self.pressed(btn.text))
        return btn

    def pressed(self, *args):
        operator = ['/','-','+','*']
        if args[0] in operator and self.stash[-1:] in operator and args[0] != self.stash[-1:]:
            self.stash = self.stash[:-1]
            self.stash+=args[0]
        elif args[0] == 'del':
            self.stash = self.stash[:-1]
        elif args[0] == self.stash[-1:] and args[0] in operator or args[0] == '=' and self.stash == '':
            pass
        elif args[0] == 'AC':
            self.stash = ''
        elif args[0] == '+/-':
            import re
            x = re.split('\*|-|/|\+',self.stash)
            lastNum = x[len(x)-1]
            lastOperator = self.stash[-(len(lastNum))-1:-(len(lastNum))]
            if lastOperator == '-':
                self.stash = self.stash[:-(len(lastNum)+1)]+'+'+lastNum
            elif lastOperator == '+':
                self.stash = self.stash[:-(len(lastNum)+1)]+'-'+lastNum
            elif lastOperator == '*':
                self.stash = self.stash[:-(len(lastNum))]+'-'+lastNum
            elif lastOperator == '/':
                self.stash = self.stash[:-(len(lastNum))]+'-'+lastNum
            elif len(x) == 1:
                if lastNum == '':
                    lastNum = '0'
                self.stash = '-'+lastNum
        elif args[0] == '=' and self.stash != '':
            try:
                self.stash = str(eval(self.stash))
            except Exception as e:
                self.error_info(str(e))
        else:
            self.stash+=args[0]
        self.topGrid.text = self.stash

    def error_info(self, text):
        content = BoxLayout(orientation='vertical')
        error_message = Label(text="Terjadi kesalahan karena: \n"+text+"\nTolong periksa kembali")
        error_message.halign="center"
        error_message.font_size = 15
        close_popup = Button(text='Tutup')
        content.add_widget(error_message)
        content.add_widget(close_popup)
        popup = Popup(title='Peringatan',content=content, size_hint=(.8,.8))
        close_popup.bind(on_release=popup.dismiss)
        popup.open()

class Calculator(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    Calculator().run()