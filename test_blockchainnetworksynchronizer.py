# test_blockchainnetworksynchronizer.py
"""
Tests for BlockchainNetworkSynchronizer module.
"""

import unittest
from blockchainnetworksynchronizer import BlockchainNetworkSynchronizer

class TestBlockchainNetworkSynchronizer(unittest.TestCase):
    """Test cases for BlockchainNetworkSynchronizer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNetworkSynchronizer()
        self.assertIsInstance(instance, BlockchainNetworkSynchronizer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNetworkSynchronizer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
