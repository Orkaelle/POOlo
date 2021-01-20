# POOlo

## Instructions

Vous allez devoir écrire des classes (selon la POO) à l'image de légumes que vous choisissez, pour executer du code décrit dans la section "Modalités d'évaluation".   
   
Il faut créer 3 classes (légumes) héritant de 'Vegetable',   

Votre code doit utiliser les notions d'héritage. La classe mère 'Vegetable', qui est une classe abstraite, doit avoir au minimum la signature suivante :   
```python
def grow(self, number=0) # donne le nombre de graine à planter
```
   
​Il est nécessaire également de construite la classe Garden (code de la section "Modalités d'évaluation") afin de pouvoir executer le code.   

Pour cela inspirez vous du "design pattern dependency injection".   
   
**BONUS 1** : Créer une classe Jardinier qui s'occupera de planter les graines en mettant en place un design pattern factory   
**BONUS 2** : Lorsque les graines sont supérieures à 30 dans le jardin afficher une erreur ou alors donner une instance d'une autre classe garden   
**BONUS 3** : Mettre en place une variable de classe contenant le nombre de type de Légumes dans le jardin   
   
## Utilisation
Le code a executer conformément aux modalités d'évaluation se trouve dans le fichier test_valid_brief.py
Le fichier main contient une démonstration du fonctionnement général.

