import unittest
import ocr

class OCRTest(unittest.TestCase):
    def test_ocr(self):
        """Test OCR on a test image"""
        self.assertEqual(ocr("ocr_test.png"), "1234")
        
unittest.main()