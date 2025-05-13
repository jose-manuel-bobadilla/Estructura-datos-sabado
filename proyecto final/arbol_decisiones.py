# arbol_decisiones.py
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class ArbolDecisiones:
    def __init__(self):
        # Crear un DataFrame con los síntomas y diagnóstico
        data = {
            'Tos_Persistente': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            'Fiebre_Reciente': [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
            'Dificultad_Respiratoria': [1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
            'Aumento_Flema': [1, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            'Dolor_Pecho': [0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
            'Diagnóstico': ['Enfermedad Respiratoria Común', 'Tuberculosis', 'Cáncer de Pulmón', 
                            'Enfermedad Respiratoria Común', 'Cáncer de Pulmón', 'Tuberculosis', 
                            'Enfermedad Respiratoria Común', 'Cáncer de Pulmón', 'Tuberculosis', 'Cáncer de Pulmón']
        }

        # Convertir a DataFrame
        self.df = pd.DataFrame(data)

        # Mapeo de los diagnósticos a números
        self.diagnostico_map = {'Enfermedad Respiratoria Común': 0, 'Tuberculosis': 1, 'Cáncer de Pulmón': 2}
        self.df['Diagnóstico'] = self.df['Diagnóstico'].map(self.diagnostico_map)

        # Separar las características (síntomas) y la variable objetivo (diagnóstico)
        self.X = self.df.drop('Diagnóstico', axis=1)
        self.y = self.df['Diagnóstico']

        # Entrenar el modelo
        self.modelo = DecisionTreeClassifier(random_state=42)
        self.modelo.fit(self.X, self.y)

    def predecir(self, sintomas):
        # Predecir sobre un nuevo conjunto de síntomas
        prediccion = self.modelo.predict([sintomas])
        return list(self.diagnostico_map.keys())[list(self.diagnostico_map.values()).index(prediccion[0])]

