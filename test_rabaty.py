import unittest
from rabaty import oblicz_rabat, cena_po_rabacie


class TestRabaty(unittest.TestCase):
    def test_brak_rabatu(self):
        self.assertEqual(oblicz_rabat(50), 0.0)

    def test_prog_100(self):
        self.assertEqual(oblicz_rabat(100), 0.02)

    def test_prog_500(self):
        self.assertEqual(oblicz_rabat(500), 0.05)

    def test_powyzej_1000(self):
        self.assertEqual(oblicz_rabat(1500), 0.10)

    def test_cena_po_rabacie(self):
        self.assertEqual(cena_po_rabacie(200), 196.0)

    def test_cena_z_groszami(self):
        self.assertEqual(cena_po_rabacie(101), 98.98)

    def test_prog_1000(self):
        self.assertEqual(oblicz_rabat(1000), 0.10)


if __name__ == "__main__":
    unittest.main()
