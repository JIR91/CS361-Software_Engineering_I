#!/usr/bin/env python3
# coding=utf-8

import view as gui

class NOT_A_WORD(Exception):
    pass


class CONTROL:
    def __init__(self):
        self.win = gui.Tk()
        self.view = gui.WINDOW_FRAME(self, self.win)
        self.on_search_frame = False
        self.input = []

    def user_input(self, event: gui.Event):
        try:
            self.input.append(self.view.user_input.get())
            self.input_check(self.input[-1])
            if self.on_search_frame == False:
                self.on_search_frame = True
                self.view.display_search_results()
            self.view.display_links(self.input)
            self.file_out()
            self.display_inputs()
            self.view.user_input.set('')
        except NOT_A_WORD:
            print('Error')
            self.view.user_input.set('')

    def display_inputs(self):
        for request in self.input:
            print(request)
        print('\n')

    def file_out(self):
        with open('user_request.txt', 'w+') as f:
            for request in self.input:
                f.write(request+'\n')

    def input_check(self, input):
        if input.isnumeric():
            self.input.pop()
            raise NOT_A_WORD

    def run(self):
            self.win.mainloop()


def main():
    ui = CONTROL()
    ui.run()

if __name__ == "__main__":
    main()
