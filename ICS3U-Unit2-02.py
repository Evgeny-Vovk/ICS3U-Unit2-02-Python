# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: September 2022
# ICS3U-Unit2-02.py File, learning input process and output in python.

import math
from turtle import width


def main():

    # input
    length_of_rectangle = int(input("Type in the length of your rectangle(mm): "))
    width_of_rectangle = int(input("Type in the width of your rectangle(mm): "))

    # process
    area_of_rectangle = length_of_rectangle * width_of_rectangle
    perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)

    # output
    print("\nThe area of the rectangle is {} mm².".format(area_of_rectangle))
    print("The perimeter of the rectangle is {} mm.".format(perimeter_of_rectangle))

    print("\nDone.")


if __name__ == "__main__":
    main()
