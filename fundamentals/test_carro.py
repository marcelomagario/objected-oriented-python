# Example of Unit Test
from unittest import TestCase
from fundamentals.carro import Motor


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)



