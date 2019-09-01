from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MyLayout(GridLayout):
    pass


class WeatherApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    WeatherApp().run()