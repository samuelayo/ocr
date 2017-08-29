import unittest

from ocr import ocr_image 

class ocrimage(unittest.TestCase):

	def setUp(self):
		self.imagefile = "test.png"
		self.pdffile = "test.pdf"

	def testimage(self):
		self.assertTrue('Charader Encoding Test Results' in ocr_image(self.imagefile))

	def testpdf(self):
		self.assertTrue('Adobe® Portable Document Format (PDF) is a universal file format' in ocr_image(self.pdffile))

if __name__ == '__main__':
    unittest.main()