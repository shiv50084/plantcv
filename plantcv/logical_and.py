# Join images (AND)

import cv2
from . import print_image
from . import plot_image


def logical_and(img1, img2, device, debug=None):
    """Join two images using the bitwise AND operator.

    Inputs:
    img1   = image object1, grayscale
    img2   = image object2, grayscale
    device = device number. Used to count steps in the pipeline
    debug  = None, print, or plot. Print = save to file, Plot = print to screen.

    Returns:
    device = device number
    merged = joined image

    :param img1: numpy array
    :param img2: numpy array
    :param device: int
    :param debug: str
    :return device: int
    :return merged: numpy array
    """

    device += 1
    merged = cv2.bitwise_and(img1, img2)
    if debug == 'print':
        print_image(merged, (str(device) + '_and_joined.png'))
    elif debug == 'plot':
        plot_image(merged, cmap='gray')
    return device, merged
