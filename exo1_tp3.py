class Noeud:
    """Représente un noeud d'un arbre d'expression mathématique.

    Un noeud correspond à une valeur (constante, variable ou opérateur)
    et possède une liste de noeuds enfants représentant les sous-expressions
    sur lesquelles l'opérateur s'applique.
    """
    def __init__(self,x):
        self.noeud=x
        self.enfants = []
    def ajout(self,enfants):
        """Ajoute un noeud à la liste des noeuds enfants.

        :param noeud: l'objet Noeud à ajouter comme enfant
        """
        if not isinstance(enfants,Noeud):
            enfant=Noeud(enfants)
        self.enfants.append(enfant)
    def affichage(self):
        if len(self.enfants) == 0:
            return str(self.noeud) 
        resultat =str(self.noeud)  
        for enfant in self.enfants:
            resultat += " " + enfant.affichage()
    
        return resultat
    def evaluer(self,dico):
        """Évalue l'expression symbolique pour des valeurs données des variables.

        :param dict: dictionnaire associant chaque nom de variable à sa valeur
        :return: la valeur numérique (float) de l'expression
        :raises ValueError: si une variable n'a pas de valeur associée dans dict
        """
        res=0
        for i in range (len(self.enfants)):
             if isinstance(dico[i],float):
                  return affichage
             

         
