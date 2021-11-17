# WUT_Azure_proj1
Project 1 for Microsoft Azure on WUT

## Table of contents
* [Team](#the-team)
* [Tematyka projektu](#tematyka-projektu)
* [Opis danych] (#opis-danych)
* [Architektura](#architektura)
* [Rozwiązanie](#rozwiązanie)
* [Instrukcja reprodukcji rozwiązania](#instrukcja-reprodukcji-rozwiązania)
* [Demo dzałania](#demo-działania)

## The Team
* Hubert Kunikowski
* Danuta Stawiarz

## Tematyka projektu
Cel projektu stanowiło utworzenie modelu, który na podstawie wprowadzonych danych o stanie zdrowia pacjenta wykonuje predykcję prawdopodobieństwa, z jakim może ona zapaść na chorobę serca.
Projekt zakładał wykorzystanie i przetestowania działania komponentów platformy Azure.

## Architektura
W projekcie zostały wykorzystane następujące komponenty platformy Azure:
* Azure Storage Account - Blob - w tym serwisie przechowywane są pliki zawierające dane pacjentów
* Machine Learning Studio - w tym serwisie następuje przetworzenie danych oraz tworzenie modelu wykonującego predykcję

Schemat działania przedstawiony został w formie graficznej poniżej:

## Opis danych


## Rozwiązanie
Rozwiązanie zakłada działania na etapie przechowywania danych, ich przetwarzania oraz tworzenia modelu predykcji.

### Przechowywanie danych
W celu trwałego przechowywania danych utworzony został serwis Storage Account. Plik o formacie CSV zawierający informacje dotyczące parametrów zdrowia pacjentów został umieszczony w kontenerze o nazwie "heartdata".

### Przetwarzanie danych
Kolejny krok stanowiło utworzenie serwisu Machine Learning Studio. Na początku należało zaimportować dane przechowywane w Azure Storage. W stym celu utworzono nowy Datastore, a w jego obrębie Dataset, w którym dane z pliku CSV zostały umieszczone w formie tabelarycznej.
Następnie został stworzonony nowe Pipeline, gdzie dane uległy przetworzeniu. Koniecznymi operacjami były:
* zamiana danych kategorycznych na liczbowe (Sex, Exercise Angina)
* przeskalowanie danych kategorycznych (ChestPainType, RestingECG, ST_Slope)
* usunięcie braków

### Trenowanie modelu i ewaluacja


### Pipeline
Pipeline zawierający zarówno przetwarzanie danych, ich podział i trening modelu przedstawia się następująco:

----tu screen finalnego pipelinu :) -----


## Instrukcja reprodukcji rozwiązania

## Demo działania
Pod linkiem umieszczono film, na którym zostało przedstawione działanie projektu:




