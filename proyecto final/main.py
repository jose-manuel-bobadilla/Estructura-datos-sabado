# main.py
import pandas as pd
from arbol_decisiones import ArbolDecisiones

def obtener_sintomas():
    # Simulamos la entrada de síntomas por parte del usuario
    tos_persistente = int(input("¿Tienes tos persistente o recurrente? (1: Sí, 0: No): "))
    fiebre_reciente = int(input("¿Has tenido fiebre recientemente? (1: Sí, 0: No): "))
    dificultad_respiratoria = int(input("¿Sientes dificultad para respirar o falta de aire? (1: Sí, 0: No): "))
    aumento_flema = int(input("¿Has notado un aumento de moco o flema? (1: Sí, 0: No): "))
    dolor_pecho = int(input("¿Sientes dolor o malestar en el pecho? (1: Sí, 0: No): "))

    return [tos_persistente, fiebre_reciente, dificultad_respiratoria, aumento_flema, dolor_pecho]

def main():
    # Crear el objeto del árbol de decisiones
    arbol = ArbolDecisiones()

    # Solicitar los síntomas al usuario
    print("Por favor, responde las siguientes preguntas sobre los síntomas del paciente.")
    sintomas = obtener_sintomas()

    # Convertir los síntomas a un DataFrame con las mismas columnas que el modelo
    sintomas_df = pd.DataFrame([sintomas], columns=['Tos_Persistente', 'Fiebre_Reciente', 'Dificultad_Respiratoria', 'Aumento_Flema', 'Dolor_Pecho'])

    # Hacer la predicción
    diagnostico = arbol.predecir(sintomas_df.iloc[0])

    # Mostrar el diagnóstico
    print(f"\nEl diagnóstico para el paciente es: {diagnostico}")

if __name__ == "__main__":
    main()
