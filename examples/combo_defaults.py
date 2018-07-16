from guizero import App, Combo, PushButton


class ComboBug:
    def __init__(self):
        app = App(title="Hello world")
        self.items1 = ['1', '2', '3']
        self.items2 = ['4', '5', '6']

        self.the_combo = Combo(app, options=self.items1)
        self.the_button = PushButton(app, text='Push Me', command=self.switch_items)

        app.display()

    def switch_items(self):
        self.the_combo.clear()
        count = 0
        for item in self.items2:
            self.the_combo.insert(count, item)
            count += 1
        self.the_combo.select_default()


ComboBug()