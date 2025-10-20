# Assignment 1 — INFO-H600: Computing Foundations of Data Sciences

## Description

Ce projet contient trois exercices fondamentaux en Python dans le cadre du cours **INFO-H600 - Computing Foundations of Data Sciences**.  
Chaque exercice illustre des compétences clés en **programmation logique, manipulation de chaînes et validation de structures de données**.

---

## Exercices

### Exercice 1 — The Sequence (Look-and-say sequence)

**Objectif :**  
Créer une fonction `the_sequence(n)` qui génère les *n* premiers termes de la célèbre **suite “look-and-say”** :  
1, 11, 21, 1211, 111221, 312211, 13112221, …

**Principe :**  
Chaque terme décrit le précédent :
- 1 → "un 1" → 11  
- 11 → "deux 1" → 21  
- 21 → "un 2, un 1" → 1211  

**Exemple d’utilisation :**
```python
print(the_sequence(8))
```

### Sortie attendue
```css
['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211']
```

### Exercice 1 — Sudoku Validator

**Objectif :**
Créer une fonction `is_valid_sudoku(board)` qui vérifie si un plateau 9x9 de Sudoku est valide.
Un plateau est valide si :

- Chaque ligne contient des chiffres uniques (hors “.”)
- Chaque colonne contient des chiffres uniques
- Chaque sous-grille 3×3 contient des chiffres uniques

**Exemple d’utilisation :**

```python
print(is_valid_sudoku(board))
```

### Sortie attendue
```graphql
True
```

### Exercice 3 — Tic-Tac-Toe Validity Checker

**Objectif :**
Créer une fonction `is_valid_tictactoe(board)` qui vérifie si un **état du jeu de morpion (3x3)** est valide.

Les règles prises en compte :

1. Le joueur `X` commence toujours.
2. Le nombre de `X` doit être égal à celui des `O`, ou supérieur d’une unité.
3. Les deux joueurs ne peuvent pas gagner en même temps.

**Exemples d’utilisation :**

```python
print(is_valid_tictactoe(['XXX', ' X ', '   ']))  # False
print(is_valid_tictactoe(['XOX', ' O ', '   ']))  # True
print(is_valid_tictactoe(['O  ', '   ', '   ']))  # False
print(is_valid_tictactoe(['X  ', '   ', '   ']))  # True
print(is_valid_tictactoe(['XOX', ' X ', '   ']))  # False
```

### Exécution du programme

Dans le terminal, exécuter simplement :

```bash
python asg1.py
```

### Sortie attendue
```python
['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211']

True

False
True
False
True
False
```

### Compétences mobilisées

- Structures de contrôle (`for, if, else`)
- Manipulation de chaînes et listes
- Conception d’algorithmes logiques
- Validation de règles de jeu et structures de données

### Auteurs

**Noms :** 
1. Charly MASOBELE
2. SILUE Kolotcholoma
**Cours :** INFO-H600 – Computing Foundations of Data Sciences
**Université :** UNIVERSITE LIBRE DE BRUXELLE (ULB)
**Langage :** Python 3.10+