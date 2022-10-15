#!\usr\bin\env python3
# coding=utf-8

import time

"""_summary_
"""

def main():
    while True:
        time.sleep(1)
        with open("image-service.txt", "r") as r_imag:
            line = r_imag.readline().strip('\n')
            if line.isnumeric():
                with open("image-service.txt", "w") as w_prng:
                    w_prng.write(f'cs361-images\{int(line) % 722}.png')


if __name__ == "__main__":
    main()
