import unittest     # Import the Python unit testing framework
from operators import Operator, OperatorStore         # Our code to test
from datetime import date


class OperatorTest(unittest.TestCase):
    ''' Unit tests for our OperatorStore functions'''
    def test_operator_passes_all(self):
        # Arrange
        op = Operator()
        op.first_name = "John"
        op.family_name = "Smith"
        op.date_of_birth = date(1990,1,1)
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 5
        op.drone = None

        opStore = OperatorStore()
        #act
        act = opStore.add(op)

        #assert
        self.assertTrue(act.is_valid)

    def test_operator_no_name(self):
        # Arrange
        op = Operator()
        op.first_name = None
        op.family_name = "Smith"
        op.date_of_birth = date(1990,1,1)
        op.drone_license = 2

        opStore = OperatorStore()
        #act
        act = opStore.add(op)

        #assert
        self.assertFalse(act.is_valid())
        self.assertIn("First name is required", act.messages)

    def test_operator_no_date_of_birth(self):
        # Arrange
        op = Operator()
        op.first_name = "John"
        op.family_name = "Smith"
        op.date_of_birth = None
        op.drone_license = 1

        opStore = OperatorStore()
        #act
        act = opStore.add(op)

        #assert
        self.assertFalse(act.is_valid())
        self.assertIn("Date of birth is required", act.messages)
    
    def test_operator_no_drone_license(self):
        # Arrange
        op = Operator()
        op.first_name = "John"
        op.family_name = "Smith"
        op.date_of_birth = date(1990,1,1)
        op.drone_license = None
        op.operations = 5

        opStore = OperatorStore()
        #act
        act = opStore.add(op)

        #assert
        self.assertFalse(act.is_valid())
        self.assertIn("Drone license is required", act.messages)

    def test_operator_class_2_license(self):
        # Arrange
        op = Operator()
        op.first_name = "John"
        op.family_name = "Smith"
        op.date_of_birth = date(2005,1,1)
        op.drone_license = 2

        opStore = OperatorStore()
        #act
        act = opStore.add(op)

        #assert
        self.assertFalse(act.is_valid())
        self.assertIn("Operator should be at least twenty to hold a class 2 license", act.messages)

    def test_operator_drone_endorsement(self):
        # Arrange
        op = Operator()
        op.first_name = "John"
        op.family_name = "Smith"
        op.date_of_birth = date(1990,1,1)
        op.drone_license = 1
        op.rescue_endorsement = True
        op.operations = 4

        opStore = OperatorStore()

        #act
        act = opStore.add(op)

        #assert
        self.assertFalse(act.is_valid())
        self.assertIn("Operator must have been involved in five prior rescue missions", act.messages)

    def test_operator_added_to_store(self):
        # Arrange
        op = Operator()
        op.first_name = "John"
        op.family_name = "Smith"
        op.date_of_birth = date(1990,1,1)
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 5

        opStore = OperatorStore()
        
        #act
        act = opStore.add(op)
        act.commit()

        #assert
        self.assertTrue(opStore.get(1) == op)



# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()