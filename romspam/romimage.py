import os
import random
import shutil

"""
    getimage
    Get a random image from a directory.
"""
def getimage(directory):
    if not os.path.isdir(directory):
        raise Exception("romimage.getimage was supplied an invalid directory.")

    choices = [f for f in os.listdir(directory) if f.endswith(".png") or f.endswith(".jpg") or f.endswith(".gif") or f.endswith(".jpeg")]
    if len(choices) == 0:
        return None
    else:
        return os.path.join(directory, random.choice(choices))

"""
    moveimagesent
    Move an image from a directory into the directory's "sent" directory. Image
    should be an absolute path.
"""
def moveimagesent(image):
    # Image must not be None
    if image is None:
        raise Exception("Image specified cannot be None.")

    # Image path must be absolute
    if not os.path.isabs(image):
        raise Exception("Path specified is not an absolute path.")

    # Get directory of image
    directory = os.path.dirname(os.path.realpath(image))

    # Check if sent directory exists
    sentDirectory = os.path.join(directory, "sent")
    if not os.path.isdir(sentDirectory):
        os.makedirs(sentDirectory)

    # Move file
    filename = os.path.basename(image)
    shutil.move(image, os.path.join(sentDirectory, filename))

"""
    resetsent
    Reset sent images by moving them back out of the sent folder.
"""
def resetsent(directory):
    # Check directory supplied exists
    if not os.path.isdir(directory):
        raise Exception("romimage.getimage was supplied an invalid directory.")

    # Check if sent directory exists
    sentDirectory = os.path.join(directory, "sent")
    if not os.path.isdir(sentDirectory):
        return False

    # Move each file back
    for image in os.listdir(sentDirectory):
        filename = os.path.basename(image)
        shutil.move(os.path.join(sentDirectory, filename), os.path.join(directory, filename))

    # Remove sent folder
    shutil.rmtree(sentDirectory)

    return True
