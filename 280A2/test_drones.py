import unittest     # Import the Python unit testing framework
from drones import DroneStore, Drone        # Our code to test


class DronesTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add_success(self):
        # Arrange
        dr = Drone("drone123")
        store = DroneStore()

        # Act
        store.add(dr)
        
        # Assert
        self.assertEqual(dr, store.get(dr.id)) 

    def test_add_already_exists(self):
        # Arrange
        dr = Drone("drone123")
        store = DroneStore()

        # Act
        store.add(dr)
        with self.assertRaises(Exception) as ctx:
            store.add(dr)
        
        # Assert
        self.assertEqual('Drone already exists in store', str(ctx.exception))

    def test_remove_success(self):
        # Arrange
        dr = Drone("drone123")
        store = DroneStore()

        # Act
        store.add(dr)
        store.remove(dr)
        
        # Assert
        self.assertNotIn(dr.id, store.list_all())

    def test_remove_doesnt_exist(self):
        # Arrange
        dr = Drone("drone123")
        store = DroneStore()

        # Act
        with self.assertRaises(Exception) as ctx:
            store.remove(dr)
        
        # Assert
        self.assertEqual('Drone does not exist in store', str(ctx.exception))


# This allows running the unit tests from the command line
if __name__ == '__main__':
    unittest.main()