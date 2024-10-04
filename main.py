from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        self.icon="app1.png"
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.text_input = TextInput(
            font_size=50,
            size_hint_y=None,
            height=250
        )
        self.add_widget(self.text_input)

        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        # Number buttons...
        buttons = [
            ['7', '8', '9','*'],
            ['4', '5', '6','/'],
            ['1', '2', '3','-'],
            ['0', '.', '=','+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            layout.add_widget(h_layout)
            for label in row:
                button = Button(text=label)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)     
        # Backspace button...
        backspace_button = Button(text='ESC')
        backspace_button.bind(on_press=self.on_backspace_press)
        layout.add_widget(backspace_button)

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                result = str(eval(self.text_input.text))
                self.text_input.text = result
            except Exception as e:
                self.text_input.text = 'Error'
        else:
            self.text_input.text += instance.text

    def on_backspace_press(self, instance):
        text = self.text_input.text
        self.text_input.text = text[:-1]

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
