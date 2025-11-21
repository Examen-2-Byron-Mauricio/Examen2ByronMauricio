import unittest
from Examen2 import MiClase

#Cambio en el codigo (linea 4) para probar el funcionamiento de los workflows
# Se realizó un solo archivo para las pruebas unitarias mías y de Mauricio
class TestMiClase(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test: crea una instancia de MiClase con datos de ejemplo."""
        self.obj = MiClase(
            Valencia=5,
            Tempo=120,
            Tonos=12,
            listaCanciones=["Canción 1", "Canción 2"],
            listaBailabilidad=[0.8, 0.9]
        )

    # Tests para ObtieneValencia

    def test_obtiene_valencia_mixto(self):
        """ObtieneValencia: debe contar solo los dígitos impares en un número mixto."""
        resultado = self.obj.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)

    def test_obtiene_valencia_sin_impares(self):
        """ObtieneValencia: si no hay dígitos impares debe devolver 0."""
        resultado = self.obj.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)

    def test_obtiene_valencia_todos_impares(self):
        """ObtieneValencia: si todos los dígitos son impares debe devolver la cantidad total."""
        resultado = self.obj.ObtieneValencia(13579)
        self.assertEqual(resultado, 5)

    # Tests para DivisibleTempo

    def test_divisible_tempo_numero_compuesto(self):
        """DivisibleTempo: un número compuesto debe devolver todos sus divisores."""
        resultado = self.obj.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])

    def test_divisible_tempo_uno(self):
        """DivisibleTempo: para 1 solo debe devolver [1]."""
        resultado = self.obj.DivisibleTempo(1)
        self.assertEqual(resultado, [1])

    def test_divisible_tempo_primo(self):
        """DivisibleTempo: para un número primo solo debe devolver [1, n]."""
        resultado = self.obj.DivisibleTempo(13)
        self.assertEqual(resultado, [1, 13])

    # Tests para ObtieneMasBailable

    def test_obtiene_mas_bailable_lista_normal(self):
        """ObtieneMasBailable: debe devolver el valor máximo de una lista con varios elementos."""
        lista = [0.8, 0.9, 0.7]
        resultado = self.obj.ObtieneMasBailable(lista)
        self.assertEqual(resultado, 0.9)

    def test_obtiene_mas_bailable_un_elemento(self):
        """ObtieneMasBailable: si la lista tiene un solo elemento, debe devolver ese elemento."""
        lista = [0.5]
        resultado = self.obj.ObtieneMasBailable(lista)
        self.assertEqual(resultado, 0.5)

    def test_obtiene_mas_bailable_lista_vacia(self):
        """ObtieneMasBailable: si la lista está vacía, debe devolver None."""
        resultado = self.obj.ObtieneMasBailable([])
        self.assertIsNone(resultado)

    # Tests para VerificaListaCanciones

    def test_verifica_lista_canciones_todas_validas(self):
        """VerificaListaCanciones: debe devolver True si todas las canciones son válidas (no None)."""
        lista = ["Canción 1", "Canción 2", "Canción 3"]
        resultado = self.obj.VerificaListaCanciones(lista)
        self.assertTrue(resultado)

    def test_verifica_lista_canciones_con_none(self):
        """VerificaListaCanciones: debe devolver False si alguna canción es None."""
        lista = ["Canción 1", None, "Canción 3"]
        resultado = self.obj.VerificaListaCanciones(lista)
        self.assertFalse(resultado)

    def test_verifica_lista_canciones_lista_vacia(self):
        """VerificaListaCanciones: una lista vacía se considera válida y debe devolver True."""
        resultado = self.obj.VerificaListaCanciones([])
        self.assertTrue(resultado)

    # Tests para Encuentra

    def test_encuentra_elemento_presente(self):
        """Encuentra: debe devolver True si el elemento está presente en la lista."""
        lista = [1, 2, 3, 4, 5]
        resultado = self.obj.Encuentra(lista, 3)
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()