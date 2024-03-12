# Importowanie niezbędnych modułów i bibliotek dla aplikacji webowej.
from flask import Flask, request
import joblib
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
from maps import *
import numpy as np

# Inicjalizacja aplikacji webowej przy użyciu frameworka Flask.
app = Flask(__name__)

# Wczytanie wcześniej wytrenowanego modelu uczenia maszynowego z pliku.
model = joblib.load("../model/model.joblib")

# Definicja trasy dla podstawowego adresu URL ('/'), która wyświetla formularz HTML.
@app.route('/')
def index():
    # Odczytanie zawartości pliku HTML formularza i zwrócenie go jako odpowiedzi na żądanie.
    return open("static/index.html", "r", encoding='utf-8').read()

# Zdefiniowanie funkcji do przetwarzania danych wejściowych dla prognozy uczenia maszynowego.
def factorize(data):
    # Wyświetlenie danych wejściowych dla celów diagnostycznych.
    print(data)
    
    # Konwersja każdej wartości wejściowej na typ float, obsługując nie numeryczne wartości.
    for i, x in enumerate(data):
        try:
            data[i] = float(x)
        except:
            continue
    
    # Zdefiniowanie nazw kolumn dla ramki danych.
    head = ['HeartDisease', 'BMI', 'Smoking', 'AlcoholDrinking', 
       'PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory',
       'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime',
       'Asthma', 'KidneyDisease', 'SkinCancer']
    
    # Utworzenie ramki danych pandas z danymi wejściowymi.
    temp = pd.DataFrame(columns=head)
    temp.loc[0] = data
    
    # Mapowanie zmiennych kategorycznych na wartości numeryczne przy użyciu wcześniej zdefiniowanych odwzorowań.
    temp['AgeCategory'] = temp['AgeCategory'].map(age_map)
    temp['GenHealth'] = temp['GenHealth'].map(health_map)
    temp['Race'] = temp['Race'].map(race_map)
    temp['Sex'] = temp['Sex'].map(sex_map)
    temp['Diabetic'] = temp['Diabetic'].map(diabetic_map)
    
    # Konwersja pozostałych kolumn typu object na typ boolowski przy użyciu odwzorowań boolowskich.
    for i in temp:
        if temp[i].dtype == object:
            temp[i] = temp[i].map(bool_map)
    return temp.values

# Definicja trasy do obsługi przesyłania formularza pod adresem '/submit'.
@app.route('/submit', methods=['POST'])
def submit():
    # Wyodrębnienie danych formularza z żądania POST.
    data = [*request.form.values()]
    
    # Sprawdzenie, czy metoda żądania to POST.
    if request.method == 'POST':
        # Przewidzenie prawdopodobieństwa udaru przy użyciu wczytanego modelu uczenia maszynowego.
        prediction = model.predict(factorize(data))[0]
        
        # Zwrócenie odpowiedzi użytkownikowi w zależności od prognozy modelu.
        if prediction == 1:
            return "prawdopodobnie dostaniesz udaru :("
        else:
            return "prawdopodobnie nie dostaniesz udaru :)"

# Uruchomienie aplikacji webowej Flask na porcie 8080, jeśli skrypt jest uruchamiany bezpośrednio.
if __name__ == '__main__':
    app.run(port=8080)
