

import unittest

SERVER = "server b"
class All_Assert_Test(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("soy_un_fokin_numero")

    def test_assert_in(self):
        self.assertIn(10, [5,10,9,8])
        self.assertNotIn(5, [6,7,10])

    def test_assert_dict_equal(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual({"first_name": "Luis", "last_name": "Martinez"},user)

        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3})
    @unittest.skip("esta en progreso la funcion")
    def test_skip(self):
        self.assertEqual("holaa","adios mamahuevo")

    @unittest.skipIf(SERVER == 'server b', "saltada por que no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100,100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,150)