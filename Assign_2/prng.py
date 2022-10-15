#!/usr/bin/env python3
# coding=utf-8

import time, random

"""_summary_
"""

def main():
    while True:
        time.sleep(1)
        with open("prng-service.txt", "r") as r_prng:
            if r_prng.readline() == 'run':
                with open("prng-service.txt", "w") as w_prng:
                    w_prng.write(str(random.randint(0, 1000)))


if __name__ == "__main__":
    main()
