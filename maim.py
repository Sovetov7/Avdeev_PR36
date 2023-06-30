from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config

Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '800')


class MyPaintWidget(Widget):
    Except_num = 0

    def on_touch_down(self, touch):

        if (self.Except_num == 0):
            self.color = (1, 1, 1, 1)
        else:
            pass

        with self.canvas:
            Color(*self.color)
            d = 20.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        with self.canvas:
            Color(*self.color)
            d = 20.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def red(self):
        self.color = (176, 0, 0)
        self.Except_num = 1

    def yellow(self):
        self.color = (255, 232, 0)
        self.Except_num = 2

    def white(self):
        self.color = (255, 255, 255)
        self.Except_num = 3


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.color = (random(), 1, 1)
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        red_color_btn = Button(text='Brush', pos=(100, 0), background_normal='', background_color=(176, 0, 0))
        red_color_btn.bind(on_release=self.red)
        yellow_color_btn = Button(text='Brush', pos=(200, 0), background_normal='', background_color=(254, 232, 0))
        yellow_color_btn.bind(on_release=self.yellow)
        white_color_btn = Button(text='Brush', pos=(300, 0), background_normal='', background_color=(255, 255, 255))
        white_color_btn.bind(on_release=self.white)

        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(red_color_btn)
        parent.add_widget(yellow_color_btn)
        parent.add_widget(white_color_btn)
        return parent

    def white(self, obj):
        self.painter.white()

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def red(self, obj):
        self.painter.red()

    def yellow(self, obj):
        self.painter.yellow()


if __name__ == '__main__':
    MyPaintApp().run()