# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Moduł walidacji zamówień i naliczania rabatów. Pure-Python, standard library only — no
dependencies, no build step, no package layout. Code and identifiers are in Polish.

## Commands

```bash
python3 -m unittest discover -v          # run all tests
python3 -m unittest test_rabaty -v       # run one test module
python3 -m unittest test_rabaty.TestRabaty.test_prog_100   # run one test
```

## Architecture

Two independent modules, each paired with a `test_*.py` unittest file:

- `walidator.py` — order validation. `waliduj_zamowienie(dict)` is the entry point; it
  returns a **list of Polish error strings** (empty list = valid), rather than raising or
  returning a bool. It composes the field-level checks `waliduj_email` / `waliduj_ilosc`.
- `rabaty.py` — discount tiers. `PROGI` is an ordered list of `(threshold, rate)` pairs,
  highest first; `oblicz_rabat` returns the rate for the first threshold the amount
  exceeds. `cena_po_rabacie` applies it and rounds to 2 decimals.

## Known state

`test_prog_100` and `test_prog_500` currently **fail**: the tests expect the discount to
apply *at* the threshold, but `oblicz_rabat` uses strict `>` (`kwota > prog`). This is the
inherited state from commit `baa723c` — decide with the user whether the tests or the
boundary condition is authoritative before "fixing" either side. This is known issues but its not fixed yet.

## Business's decision
znizki powinny dzialac na wartosci rowne dla danego progu czyli jesli jest wartosc 500 to ta wartosc powinna wpadac w prog 500 a nie w 100, jesli wartosc jest rowna 100 to prog powinien ja lappac do 100 a nie usuwac znizke.

## NOT TO DO
nie wolno modyfikowac plikow test_*.py, jest to wymagane zeby testy przeszly, jesli test i kod sie nie zgadzaja poprawiamy kod

## Working Rule
kazda zmiana powinna byc na osobnym branchu, nie na main
przed kazdym commitem wykonaj komende python3 -m unittest discover -v i sprawdz czy liczba FAIL nie wzrosla
