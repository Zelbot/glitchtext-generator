import random
import pyperclip


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
        self.string = None
        self.last_mark = None
        self.strength = None

    def main(self):
        """
        Executes the defined functions one after another in order to generate glitched text
        """
        self.get_string()
        self.get_strength()
        self.generate_text()

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

    def get_string(self):
        """
        Lets the user enter the string which they want to convert
        """
        print('Please enter the string you want to convert.')
        self.string = input()

    def get_strength(self):
        """
        Lets the user choose the strength of the glitch conversion
        """
        while True:
            print('What strength do you want the generator to operate at? (1-10)')
            strength_input = input()
            if strength_input.isnumeric():
                self.strength = int(strength_input)
                break

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

        print(glitched_text)
        pyperclip.copy(glitched_text)
        print('\n\nCopied the glitched text to the clipboard!')

        print(f'Added {len(glitched_text) - len(self.string)} characters - now {len(glitched_text)} in total.')
        if len(glitched_text) <= 32:
            print('OK: The glitched string is a valid Discord nickname.')
        else:
            print('WARN: The glitched string is not a valid Discord nickname.')


if __name__ == '__main__':
    print('Glitchtext generator made by Github/Zelbot')
    Generator().main()
