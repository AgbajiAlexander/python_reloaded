import unittest
from transformations import (
    convert_hex,
    convert_bin,
    convert_case,
    fix_a_an,
    fix_punctuation,
    fix_quotes,
    process_text,
)


class TestTransformations(unittest.TestCase):

    def test_convert_hex(self):
        self.assertEqual(
            convert_hex("1E (hex) files were added"),
            "30 files were added"
        )

    def test_convert_bin(self):
        self.assertEqual(
            convert_bin("It has been 10 (bin) years"),
            "It has been 2 years"
        )


if __name__ == "__main__":
    unittest.main()