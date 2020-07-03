# CA - Epreuve du Feu

## Intro
Le langage choisi est **python**.

Les épreuves sont résolues sans chercher à optimiser les scripts, l'objectif étant d'avoir une solution.

Le dossier resources contient des fichiers utiles pour tester les scripts

## Tri
Je ne sais pas encore dire quel algorithme est implémenté.
### Reste à faire
Découvrir et implémenter d'autres algorithmes

## Sudoku
La première version implémentée permet uniquement de résoudre des cas très très faciles : à chaque "tour" au moins 
une case vide n'a qu'une solution

Les méthode implémentée sont : 
- la recherche des valeurs uniques (ou "solitaire nu")
- L'élimination directe ("solitaire camouflé")


### Trois codes :
#### sudoku.py
- Implémente la technique de l'élimination indirecte [(voir ce lien)](https://fr.wikibooks.org/wiki/R%C3%A9solution_de_casse-t%C3%AAtes/R%C3%A9solution_du_sudoku)
- Permet de résourdre des sudokus simples et moyens.
- Execution plutôt rapide

#### sudoku_backtracking.py
- Implémente la méthode du backtracking : On essaie de remplir le sudoku en testant toutes les possibilités
- Permet de résoudre **tous** les sudoku
- Parfois **très** long car beaucoup d'aller-retours 


#### sudoku_mix.py
- Implément un mix des deux méthodes précédentes. Parfois la première permet de trouver quelques chiffres. Le backtracking est lancé sur le sudoku partiellement résolu.
- Permet de résoudre **tous** les sudoku
- Généralement bien rapide que le backtracking seul.