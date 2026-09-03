import unittest
from walidator import waliduj_email, waliduj_ilosc, waliduj_zamowienie


class TestWalidator(unittest.TestCase):
    def test_email_poprawny(self):
        self.assertTrue(waliduj_email("kacper@example.com"))

    def test_email_bez_malpy(self):
        self.assertFalse(waliduj_email("kacper.example.com"))

    def test_ilosc_ujemna(self):
        self.assertFalse(waliduj_ilosc(-1))

    def test_zamowienie_z_dwoma_bledami(self):
        bledy = waliduj_zamowienie({"email": "zly", "ilosc": 0})
        self.assertEqual(len(bledy), 2)


if __name__ == "__main__":
    unittest.main()
