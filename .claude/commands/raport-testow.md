---
description: "Uruchamia testy i tworzy raport QA: status, pokrycie, ryzyka"
argument-hint: "[nazwa-modulu]"
allowed-tools: Bash(python3:*), Bash(pytest:*), Bash(git status:*), Read
model: haiku
---

## Kontekst

Stan repozytorium: !`git status --short`
Pliki testowe: !`ls tests/ 2>/dev/null || echo "brak katalogu tests"`

## Zadanie

Uruchom testy dla modulu: $ARGUMENTS
Jesli nie podano modulu, uruchom wszystkie testy.

Przygotuj krotki raport zawierajacy:

1. Liczbe testow przechodzacych i niepowodzen
2. Nazwy testow, ktore nie przeszly, wraz z przyczyna
3. Obszary kodu, ktore Twoim zdaniem sa niedostatecznie pokryte testami

Nie modyfikuj zadnych plikow.
