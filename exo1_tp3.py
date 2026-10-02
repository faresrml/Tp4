class Noeud:
    def __init__(self,x):
        self.noeud=x
        self.enfants = []
    def ajout(self,enfants):
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
        res=0
        for i in range (len(self.enfants)):
             if isinstance(dico[i],float):
                  return affichage
             

         
