#!/usr/bin/env python3
# coding=utf-8

"""_summary_
"""

import time
from PIL import Image as img


class RangeError(Exception):
    def __init__(self, input):
        self.input = input


def main():
    clean_up = False

    while True:
        try:
            user_input = int(input(
'-----------------------MENU-----------------------\n\
Enter 1: Generate Random Pokémon Image\n\
Enter 2: Exit Program\n\n'))
            if user_input < 1 or user_input > 2:
                raise RangeError('\nInvalid Integer Entered\n\n')

        except ValueError:
            print('\nInvalid entry, please enter integer.\n\n')
            continue

        except RangeError as range_msg:
            print(range_msg)
            continue

        # Erase all data in prng-service.txt & image-service.txt
        if clean_up == True:
            with open("prng-service.txt", "w") as prngsrv:
                prngsrv.truncate(0)
                
            with open('image-service.txt', 'w') as imagsrv:
                imagsrv.truncate(0)

        match user_input:
            case 1:
                msg = ''
                pic = ''

                with open("prng-service.txt", "w") as prngsrv:
                    prngsrv.write('run')

                time.sleep(2)
                with open("prng-service.txt", "r") as prngsrv:
                    msg = prngsrv.readline().strip('\n')

                print(f'Random number: {msg}')

                with open('image-service.txt', 'w') as imagsrv:
                    imagsrv.write(msg)

                time.sleep(2)
                with open('image-service.txt', 'r') as imagsrv:
                    pic = imagsrv.readline().strip('\n')

                print(f'Picture location: {pic}')

                pokemon = img.open(r''f'{pic}''')
                pokemon.show()


            case 2:
                print('GoodBye')
                # os.system("taskkill /f /im  Microsoft.Photos.exe")
                exit()


if __name__ == "__main__":
    main()
