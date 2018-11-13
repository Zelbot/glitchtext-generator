import random
import pyperclip
import tkinter as tk


class Application:

    LIGHT_GREY = "#e1e1ff"  # (225, 225, 255)
    ALT_GREY = '#dcdcdc'  # (220, 220, 220)
    MID_GREY = "#afafaf"  # (175, 175, 175)

    def __init__(self, master, generator):
        self.master = master
        self.gen = generator
        self.current_glitched = ''
        self.all_glitched = []
        self.index = 0

        # Row 1
        self.input_label = tk.Label(text='Text input:', bg=self.MID_GREY)
        self.input_label.grid(row=0, column=0, sticky=tk.NSEW)

        self.input_entry = tk.Entry(bg=self.ALT_GREY)
        self.input_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # Row 2
        self.strength_label = tk.Label(text='Strength:', bg=self.MID_GREY)
        self.strength_label.grid(row=1, column=0, sticky=tk.NSEW)

        self.strength_entry = tk.Entry(bg=self.ALT_GREY)
        self.strength_entry.grid(row=1, column=1, sticky=tk.NSEW)

        self.generate_button = tk.Button(text='Generate', bg=self.LIGHT_GREY, cursor='hand2',)
        self.generate_button.bind('<ButtonRelease-1>', self.generate_glitched_text)
        self.generate_button.grid(row=0, column=2, rowspan=2, sticky=tk.NSEW)

        # Row 3
        self.glitch_text_label = tk.Label(text='', bg=self.MID_GREY, font=('Arial', 15))
        self.glitch_text_label.grid(row=2, column=1, sticky=tk.NSEW)
        self.master.rowconfigure(2, minsize=150)  # Increase row size to get a better text preview

        # Row 4
        self.back_button = tk.Button(text='Back', bg=self.LIGHT_GREY, cursor='hand2',
                                     command=self.previous_glitched_text)
        self.back_button.grid(row=3, column=0, sticky=tk.NSEW)

        self.copy_button = tk.Button(text='Copy', bg=self.LIGHT_GREY, cursor='hand2',
                                     command=self.copy_glitched_text)
        self.copy_button.grid(row=3, column=1, sticky=tk.NSEW)

        self.next_button = tk.Button(text='Next', bg=self.LIGHT_GREY, cursor='hand2',
                                     command=self.next_glitched_text)
        self.next_button.grid(row=3, column=2, sticky=tk.NSEW)

    def update_texts(self, textboxes):
        """
        Get the text from a list of entry boxes and update the corresponding attribute
        """
        for textbox in textboxes:
            text = textbox.get()

            if textbox == self.input_entry and self.gen.string != text:
                self.gen.string = text

            if textbox == self.strength_entry and self.gen.strength != int(text):
                self.gen.strength = int(text)

    def generate_glitched_text(self, _):  # Second param is passed when the self.generate_button is pressed
        """
        Generates and previews the glitched text
        """
        self.update_texts([self.input_entry, self.strength_entry])

        if self.gen.string == '':
            return

        glitched_text = self.gen.generate_text()
        self.current_glitched = glitched_text
        self.all_glitched.append(glitched_text)
        self.glitch_text_label.configure(text=glitched_text)

        self.warn_text_length()

        self.index = len(self.all_glitched) - 1
        print('New text generated.')

    def previous_glitched_text(self):
        """
        Displays the previous glitched text
        """
        if not self.all_glitched:  # List is empty
            return

        if self.index > 0:
            self.index -= 1

            self.current_glitched = self.all_glitched[self.index]
            self.glitch_text_label.configure(text=self.current_glitched)

            self.warn_text_length()
            print(f'Displaying generated text #{self.index + 1} / {len(self.all_glitched)}')

    def copy_glitched_text(self):
        """
        Copies the currently displayed glitched text to the clipboard
        """
        if self.gen.string == '':
            return

        pyperclip.copy(self.current_glitched)
        print('Copied the displayed text to the clipboard.')

    def next_glitched_text(self):
        """
        Displays the next glitched text
        """
        if self.index < len(self.all_glitched) - 1:
            self.index += 1

            self.current_glitched = self.all_glitched[self.index]
            self.glitch_text_label.configure(text=self.current_glitched)

            self.warn_text_length()
            print(f'Displaying generated text #{self.index + 1} / {len(self.all_glitched)}')

    def warn_text_length(self):
        """
        Changes the copy button's color to inform the user whether the text can be used as a Discord nickname
        """
        if len(self.current_glitched) > 32:
            self.copy_button.configure(bg=self.MID_GREY)
        else:
            self.copy_button.configure(bg=self.LIGHT_GREY)


class Generator:

    diactrical_marks = [
        u'\u0300', u'\u0301', u'\u0302', u'\u0303', u'\u0304',
        u'\u0305', u'\u0306', u'\u0307', u'\u0308', u'\u0309',
        u'\u030A', u'\u030B', u'\u030C', u'\u030D', u'\u030E', u'\u030F',

        u'\u0310', u'\u0311', u'\u0312', u'\u0313', u'\u0314',
        u'\u0315', u'\u0316', u'\u0317', u'\u0318', u'\u0319',
        u'\u031A', u'\u031B', u'\u031C', u'\u031D', u'\u031E', u'\u031F',

        u'\u0320', u'\u0321', u'\u0322', u'\u0323', u'\u0324',
        u'\u0325', u'\u0326', u'\u0327', u'\u0328', u'\u0329',
        u'\u032A', u'\u032B', u'\u032C', u'\u032D', u'\u032E', u'\u032F',

        u'\u0330', u'\u0331', u'\u0332', u'\u0333', u'\u0334',
        u'\u0335', u'\u0336', u'\u0337', u'\u0338', u'\u0339',
        u'\u033A', u'\u033B', u'\u033C', u'\u033D', u'\u033E', u'\u033F',

        u'\u0340', u'\u0341', u'\u0342', u'\u0343', u'\u0344',
        u'\u0345', u'\u0346', u'\u0347', u'\u0348', u'\u0349',
        u'\u034A', u'\u034B', u'\u034C', u'\u034D', u'\u034E', u'\u034F',

        u'\u0350', u'\u0351', u'\u0352', u'\u0353', u'\u0354',
        u'\u0355', u'\u0356', u'\u0357', u'\u0358', u'\u0359',
        u'\u035A', u'\u035B', u'\u035C', u'\u035D', u'\u035E', u'\u035F'

        u'\u0360', u'\u0361', u'\u0362', u'\u0363', u'\u0364',
        u'\u0365', u'\u0366', u'\u0367', u'\u0368', u'\u0369',
        u'\u036A', u'\u036B', u'\u036C', u'\u036D', u'\u036E', u'\u036F',

        u'\u1DC0', u'\u1DC1', u'\u1DC2', u'\u1DC3', u'\u1DC4',
        u'\u1DC5', u'\u1DC6', u'\u1DC7', u'\u1DC8', u'\u1DC9'
        ]

    def __init__(self):
        self.string = ''
        self.last_mark = ''
        self.strength = 1

    def get_new_mark(self, avoid_duplicates=True):
        """
        Chooses a random mark from the diactrical_marks list
        Comes with the option to avoid duplicates
        """
        new_mark = random.choice(self.diactrical_marks)

        if avoid_duplicates is True:
            while new_mark == self.last_mark:
                new_mark = random.choice(self.diactrical_marks)

        self.last_mark = new_mark
        return new_mark

    def generate_text(self):
        """
        Converts the given string by adding strength - 1 and strength + 1 amount of marks to each character
        The result is then printed and copied to the user's clipboard
        """
        glitched_text = ''

        for char in self.string:
            current_char = char

            amount_of_marks = random.randint(self.strength - 1, self.strength + 1)
            if amount_of_marks < 1:
                amount_of_marks = 1

            for i in range(amount_of_marks):
                current_char += self.get_new_mark()

            glitched_text += current_char

        return glitched_text


def main():
    generator = Generator()
    root = tk.Tk()
    root.configure(bg=Application.MID_GREY)
    root.title('Glitchtext Generator - Github/Zelbot')
    _ = Application(root, generator)  # Instance needed so the widgets show up

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = root.winfo_reqwidth() + 50
    window_height = root.winfo_reqheight() + 50
    window_x = int(screen_width/2 - window_width*1.5)
    window_y = int(screen_height/2 - window_height)
    root.geometry(f'+{window_x}+{window_y}')

    root.mainloop()


if __name__ == '__main__':
    main()
