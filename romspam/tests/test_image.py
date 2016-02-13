from unittest import TestCase
import os
from romspam import romimage
from romspam import romspam

class TestImage(TestCase):
    # Test to see if we can get an image
    def test_getimage(self):
        # Check if directory exists
        directory = os.path.join(romspam.rootLoc, "images")
        self.assertTrue(os.path.isdir(directory))

        # Get image and check it exists
        image = romimage.getimage(directory)
        self.assertTrue(image.endswith(".png") or image.endswith(".jpg") or image.endswith(".gif"))
        self.assertTrue(os.path.isfile(image) or image == None)
