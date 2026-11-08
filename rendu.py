def rendu_monnaie(a_rendre: int):
    rendus_possibles = [50,20,10,5,2,1]
    nb_rendus=[]
    n = 0
    for i in range(len(rendus_possibles)):
        while a_rendre >= rendus_possibles[n]:
            a_rendre -= rendus_possibles[n]
            nb_rendus[n]+=1
        if a_rendre == 0:
            return nb_rendus
        else:
            n+=1