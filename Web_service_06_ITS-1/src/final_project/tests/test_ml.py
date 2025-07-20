import joblib
import numpy as np
import unittest


class TestModel(unittest.TestCase):
    def setUp(self):
        """Загружаем модель и создаем тестовые данные."""
        self.model = joblib.load('src/final_project/model.pkl')
        self.test_data = np.array([[45, 1, 200, 30, 1, 0, 1, 0, 1, 1]])

    def test_model_loading(self):
        """Проверяем, что модель загрузилась без ошибок."""
        self.assertIsNotNone(self.model, "Модель не была загружена!")

    def test_model_prediction(self):
        """Проверяем, что модель может делать предсказания."""
        prediction = self.model.predict(self.test_data)
        self.assertEqual(len(prediction), 1, "Модель должна вернуть одно предсказание!")
        self.assertTrue(prediction in [0, 1], "Предсказание модели должно быть 0 или 1!")

    def test_model_prediction_range(self):
        """Проверяем, что вероятность предсказания находится в допустимом диапазоне [0, 1]."""
        probability = self.model.predict_proba(self.test_data)
        self.assertGreaterEqual(probability[0][1], 0, "Вероятность не может быть меньше 0!")
        self.assertLessEqual(probability[0][1], 1, "Вероятность не может быть больше 1!")


if __name__ == '__main__':
    unittest.main()
