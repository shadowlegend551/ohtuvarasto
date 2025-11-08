import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_init_with_wrong_tilavuus_and_saldo(self):
        wrong_tilavuus_and_saldo = Varasto(-1, alku_saldo=-1)
        self.assertAlmostEqual(wrong_tilavuus_and_saldo.tilavuus, 0)
        self.assertAlmostEqual(wrong_tilavuus_and_saldo.saldo, 0)

    def test_init_with_too_large_alku_saldo(self):
        wrong_alku_saldo = Varasto(1, alku_saldo=2)
        self.assertAlmostEqual(wrong_alku_saldo.saldo, 1)

    def test_add(self):
        # Of form (value_to_add, resulting_value)
        values = [(-1, 0), (2, 1)]
        for added, actual in values:
            with self.subTest(added=added, actual=actual):
                varasto = Varasto(1)
                varasto.lisaa_varastoon(added)
                self.assertAlmostEqual(varasto.saldo, actual)

    def test_remove(self):
        values = [(-1, 0), (2, 1)]
        for expected, actual in values:
            with self.subTest(expecte=expected, actual=actual):
                varasto = Varasto(1, alku_saldo=1)
                self.assertAlmostEqual(varasto.ota_varastosta(expected),
                                       actual)

    def test_string_dunder(self):
        varasto = Varasto(1)
        self.assertEqual(varasto.__str__(), 'saldo = 0, vielä tilaa 1')
