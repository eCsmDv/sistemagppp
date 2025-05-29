import unittest

class TestOrderManager(unittest.TestCase):
    def test_singleton_instance(self):
        manager1 = OrderManager()
        manager2 = OrderManager()
        self.assertIs(manager1, manager2)  # Ambas as instâncias devem ser iguais