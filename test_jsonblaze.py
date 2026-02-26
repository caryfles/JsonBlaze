# test_jsonblaze.py
"""
Tests for JsonBlaze module.
"""

import unittest
from jsonblaze import JsonBlaze

class TestJsonBlaze(unittest.TestCase):
    """Test cases for JsonBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JsonBlaze()
        self.assertIsInstance(instance, JsonBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JsonBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
