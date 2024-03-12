# System wykrywania udarów
## Opis 
System wykrywa prawdopodobieństwo wystąpienia udaru

## Struktura Repozytorium

1. **`app/`**
   - `app.py` - skrypt do inicjalizacji aplikacji webowej przy użyciu Flask, wczytania wytrenowanego modelu i obsługi formularza.
   - `static/` - katalog z plikami statycznymi, takimi jak pliki HTML.

2. **`model/`**
   - `model.joblib` - plik zawierający wcześniej wytrenowany model Gradient Boosting Classifier.

3. **`data/`**
   - `heart_2020.csv` - plik CSV z danymi do treningu modelu.

4. **`requirements.txt`**
   - Plik z wymaganiami dla środowiska Python.

5. **`README.md`**
   - Plik z informacjami o projekcie, jak go uruchomić, itp.

6. **`maps.py`**
   - Plik z odwzorowaniami zmiennych kategorycznych.
  
## Wymagania
pandas==2.0.3
scikit-learn==1.3.2
ipython==8.17.2
jupyterlab==4.0.8
notebook==7.0.6
## Jak skorzystać?
Frontend jest w folderze app

Aby uruchomić:
1. Zainstaluj niezbędne biblioteki Python, wpisując pip install -r requirements.txt w terminalu.
2. Uruchom skrypt app.py za pomocą polecenia python app.py.
3. Przejdź do przeglądarki i wejdź na http://localhost:8080 w celu uzyskania dostępu do aplikacji.
4. Wypełnij formularz, aby przewidzieć prawdopodobieństwo wystąpienia udaru.

Aby zobaczyć model klasyfikacji:
1. Znajduje się w katalogu model
2. w cmd: python -m jupyterlab
Ewentualnie jest dostępna wersja html

# O modelu

## Dane
Zestaw danych używany do trenowania i testowania modelu jest wczytywany z pliku CSV (heart_2020.csv). Zawiera informacje na temat choroby serca, BMI, palenia papierosów, spożycia alkoholu, zdrowia psychicznego i fizycznego, trudności z chodzeniem, płci, kategorii wiekowej, rasy, stanu zdrowia związanego z cukrzycą, aktywności fizycznej, ogólnego stanu zdrowia, czasu snu, astmy, choroby nerek i raka skóry.

## Przetwarzanie Danych
Dane są dodatkowo przetwarzane przez faktoryzację wartości ciągłych na wartości liczbowe, przy zachowaniu wagi niektórych cech.

## Podział Danych
Zbiór danych jest dzielony na zbiór treningowy i testowy za pomocą funkcji train_test_split z biblioteki scikit-learn. Aby poradzić sobie z niezrównoważoną liczbą wystąpień udarów, generowane są sztuczne próbki poprzez losowe wybieranie próbek z większościowej klasy.

## Trenowanie Modelu
Do trenowania modelu przewidywania udaru używany jest klasyfikator Gradient Boosting. Zbiór treningowy jest wykorzystywany do dopasowania modelu, a zbiór testowy do oceny jego wydajności. Model osiąga dokładność na poziomie około 72%.

## Ocena Modelu
Wydajność modelu jest wizualizowana za pomocą macierzy pomyłek, przedstawiającej zależność między prawdziwymi a przewidzianymi wartościami. Macierz zawiera miary takie jak prawdziwe negatywy, fałszywe pozytywy, fałszywe negatywy i prawdziwe pozytywy. Wyświetlenie jest szczególnie informacyjne w kontekście kompromisu między fałszywymi pozytywami a fałszywymi negatywami, z uwzględnieniem powagi przewidywania wystąpienia udaru.

# Aplikacja
To repozytorium zawiera kod aplikacji webowej napisanej w języku Python z użyciem frameworka Flask do przewidywania prawdopodobieństwa wystąpienia udaru na podstawie danych zdrowotnych. Aplikacja wykorzystuje wcześniej wytrenowany model Gradient Boosting Classifier.

## Informacje dodatkowe
Aplikacja korzysta z wcześniej wytrenowanego modelu Gradient Boosting Classifier do przewidywania udaru na podstawie dostarczonych danych zdrowotnych.

# Odwzorowania Zmiennych Kategorycznych
W pliku maps.py znajdują się odwzorowania zmiennych kategorycznych na ich numeryczne odpowiedniki. Te odwzorowania są kluczowe dla poprawnego przetwarzania danych wejściowych przed przewidywaniem udaru przy użyciu modelu uczenia maszynowego. Poniżej przedstawiono krótki opis każdego odwzorowania:

health_map:

Mapuje oceny zdrowia na liczby, gdzie 'Excellent' to 0, 'Very good' to 1, 'Good' to 2, 'Fair' to 3, a 'Poor' to 4.

race_map:

Przyporządkowuje grupy etniczne do wartości liczbowych, takie jak 'White' - 0, 'Black' - 1, 'Asian' - 2, 'Other' - 3, 'American Indian/Alaskan Native' - 4, 'Hispanic' - 5.

bool_map:

Konwertuje wartości logiczne ('Yes' i 'No') na 1 i 0, odpowiednio.

age_map:

Przyporządkowuje przedziały wiekowe do wartości liczbowych, np. '18-24' - 0, '25-29' - 1, itd.

sex_map:

Konwertuje płeć ('Male' i 'Female') na 1 i 0, odpowiednio.

diabetic_map:

Mapuje informacje dotyczące cukrzycy na liczby, gdzie 'No' to 0, 'Yes' to 1, 'No, borderline diabetes' to 2, a 'Yes (during pregnancy)' to 3.


Dane wprowadzone przez użytkownika są przetwarzane i konwertowane do formatu zrozumiałego dla modelu.

Aplikacja zwraca odpowiedź informującą o prawdopodobieństwie wystąpienia udaru.
   
