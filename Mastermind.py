# Exécuter cadeau() pour lancer le jeu
# Les couleurs ne fonctionnent pas sur tous les environnements.

from random import randint

def cadeau():

    def ask(demande,Lattendus):
        while True:
            r=input(demande)
            if r in Lattendus or r=='STOP':
                return r
            print(c(31)+'Mauvaise entrée :(\n'+c(0))

    def askT(demande,taille):
        while True:
            r=input(demande)
            if r=='STOP':
                return r
            b=True
            L=[str(i) for i in range(1,9)]
            for x in r:
                if not x in L:
                    b=False
            if b and len(r)==taille:
                return r
            print(c(31)+'Mauvaise entrée !'+c(0)+' (taille attendue :',taille,'| les couleurs sont dans [|1,n|] )\n')

    def combinaison_aleatoire(nb_couleurs,taille):
        L=[str(randint(1,nb_couleurs)) for _ in range(taille)]
        return ''.join(L)

    def c(n):
        """ Couleurs :
        30-Noir
        31-Rouge
        32-Vert
        33-Jaune
        34-Bleu
        35-Violet
        36-Cyan
        37-Blanc
        """
        return "\033[0;"+str(n)+"m"

    def compare(sol,ess,diff,taille):
        # ici, len(sol)=len(ess)=taille
        aff=''
        corrects,bons=0,0
        for i in range(taille):
            if ess[i]==sol[i]:
                aff+='O'
                corrects+=1
            elif sol.count(ess[i])>0:
                aff+='*'
                bons+=1
            else:
                aff+='-'
        if diff==1:
            return aff
        elif diff==2:
            return str(corrects)+'  O, '+str(bons)+'  *'

    def jeu(nb_couleurs,taille,diff):
        sol=combinaison_aleatoire(nb_couleurs,taille)
        # print(sol)
        C=[str(i) for i in range(1,nb_couleurs+1)]
        Cc=''
        for couleur in C:
            Cc+=(c(int(couleur)+30)+couleur)
        regles=' (Taille du code : '+str(taille)+' | Couleurs utilisées : '+Cc+c(0)+')'
        indice=''
        trouve=False
        nb_essais=0
        aide='    ( O : Bien placé(s) | * : Pas au bon endroit)\n'
        while not trouve:
            if nb_essais==0:
                ess=askT('Ton premier essai ?'+regles+'\n',taille)
            else:
                print('\n'+'='*taille+indice+aide)
                ess=askT('Essaie encore:'+regles+'\n',taille)
            if ess==sol:
                trouve=True
            elif ess=='STOP':
                return 'STOP'
            else:
                essC=''
                for x in ess:
                    essC+=(c(int(x)+30)+x)
                indice+='\n'+essC+c(0)+'   '+compare(sol,ess,diff,taille)
            nb_essais+=1
        print(c(36)+'\n=================================\nBravo, tu as trouvé en',str(nb_essais),'essais !\n=================================\n'+c(0))
        r=ask('Veux-tu rejouer ? ('+c(32)+'oui'+c(0)+'/'+c(31)+'non'+c(0)+')\n',['oui','non'])
        if r=='STOP' or r=='non':
            return 'STOP'
        elif r=='oui':
            r=ask('Même difficulté ? ('+c(32)+'oui'+c(0)+'/'+c(31)+'non'+c(0)+')\n',['oui','non'])
            if r=='STOP':
                return 'STOP'
            elif r=='oui':
                return jeu(nb_couleurs,taille,diff)
            elif r=='non':
                return '831'

    def jn():
        joyeuxnoel='\n\n=================================================================\n|                                                               |\n|   @@@  @@  @   @ @@@@ @  @  @ @     @  @  @@  @@@@ @       @  |\n|    @  @  @  @ @  @    @  @   @      @@ @ @  @ @    @       @  |\n|  @ @  @  @   @   @**  @  @  @ @     @ @@ @  @ @**  @       *  |\n|   @    @@    @   @@@@  @@  @   @    @  @  @@  @@@@ @@@@    o  |\n|                                                               |\n=================================================================\n\n\n\n'
        jnc=''
        for x in joyeuxnoel:
            n=randint(31,37)
            jnc+=(c(n)+x)
        print(jnc+c(0))

    def mastermind():
        r=choix_diff()
        if r=='STOP':
            return 'STOP'
        nb_couleurs,taille,diff=r
        return jeu(nb_couleurs,taille,diff)

    def choix_diff():
        r=ask('\nDifficulté ? (1: Débutant, 2: Expert, 3: Personnalisé)\n',['1','2','3'])
        if r=='STOP':
            return 'STOP'
        elif r=='1':
            return (6,4,1)
        elif r=='2':
            return (8,5,2)
        elif r=='3':
            L1=[str(i) for i in range(1,9)]
            L2=[str(i) for i in range(1,6)]
            r1=ask('Nombre de couleurs ? (entre 1 et 8)\n',L1)
            if r1=='STOP':
                return 'STOP'
            nb_couleurs=int(r1)
            r2=ask('Taille du code ? (entre 1 et 5)\n',L2)
            if r2=='STOP':
                return 'STOP'
            taille=int(r2)
            r3=ask('Type d\'indice ? (1: Facile, 2: Difficile)\n',['1','2'])
            if r3=='STOP':
                return 'STOP'
            diff=int(r3)
            return nb_couleurs,taille,diff

    # Début du code

    jn()
    r=ask('Ecris '+c(32)+'831'+c(0)+' puis appuie sur '+c(35)+'Entrée'+c(0)+'\nPour fermer le jeu, écris '+c(31)+'STOP'+c(0)+'. (Fonctionne à tout moment)\n',['831','832'])
    while r=='831':
        r=mastermind()
    if r=='832':
        print("Pas le droit de jouer !")
    if r=='STOP':
        print("\nMerci d'avoir joué "+c(31)+"<3"+c(0)+" !\n"+c(30)+"Pour Younes - Mastermind - Noël 2020 - Vivien Ducros")
