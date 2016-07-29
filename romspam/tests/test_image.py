import os
import mock
from unittest import TestCase
from romspam import romimage
from romspam import romspam

class TestImage(TestCase):
    # Test to see if we can get an image
    def test_getimage(self):
        # Check if directory exists
        directory = os.path.join(romspam.rootLoc, "images")
        self.assertTrue(os.path.isdir(directory))

        # List to store retrieved images
        images = []

        # Get images
        with mock.patch('os.listdir', return_value=['test.jpg']):
            images.append(romimage.getimage(directory))
        with mock.patch('os.listdir', return_value=['test.png']):
            images.append(romimage.getimage(directory))
        with mock.patch('os.listdir', return_value=['test.gif']):
            images.append(romimage.getimage(directory))
        with mock.patch('os.listdir', return_value=['test.jpeg']):
            images.append(romimage.getimage(directory))

        # Check each image passes
        self.assertTrue(len(images) == 4)
        for image in images:
            self.assertTrue(image != None)
            self.assertTrue(image.endswith(".png") or image.endswith(".jpg") or image.endswith(".gif") or image.endswith(".jpeg"))

    # Test that getimage fails when there is no valid image available
    def test_getimage_bad(self):
        # Check if directory exists
        directory = os.path.join(romspam.rootLoc, "images")
        self.assertTrue(os.path.isdir(directory))

        # Get bad image and check it exists
        with mock.patch('os.listdir', return_value=['test.docx']):
            self.assertTrue(romimage.getimage(directory) == None)
