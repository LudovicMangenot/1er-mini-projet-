import tkinter as tk

class PremiereInterface:
    def __init__(self, fenetre):

        self.bouton_maj_parasites = tk.Button(fenetre, text="Mettre à jour les mots-clés parasites", command=self.maj_mots_parasites)
        self.bouton_maj_parasites.pack()

    def maj_mots_parasites(self):
        # Ouvrir un dialogue de fichier pour choisir le fichier contenant la liste des mots-clés parasites
        fichier_mots_parasites = tk.filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])

        if fichier_mots_parasites:
            # Mettre à jour la liste des mots-clés parasites (à ta logique d'implémentation)
            print(f"Le fichier des mots-clés parasites sélectionné est : {fichier_mots_parasites}")
            # Ici, tu peux ajouter la logique pour mettre à jour la liste des mots-clés parasites

        self.fenetre = fenetre
        self.fenetre.title("Analyse de référencement")
        
        # Widgets
        self.label_url = tk.Label(fenetre, text="URL du site :")
        self.label_url.pack()
        self.entry_url = tk.Entry(fenetre)
        self.entry_url.pack()

        self.label_mots_cles = tk.Label(fenetre, text="Mots clés (séparés par des virgules) :")
        self.label_mots_cles.pack()
        self.entry_mots_cles = tk.Entry(fenetre)
        self.entry_mots_cles.pack()

        self.bouton_analyser = tk.Button(fenetre, text="Lancer l'analyse", command=self.passer_a_deuxieme_interface)
        self.bouton_analyser.pack()

    def passer_a_deuxieme_interface(self):
        # Récupérer les valeurs des champs URL et mots-clés
        url = self.entry_url.get()
        mots_cles = self.entry_mots_cles.get().split(',')

        # Créer la deuxième interface en passant les données
        DeuxiemeInterface(self.fenetre, url, mots_cles)
        # Masquer la première interface
        self.fenetre.withdraw()

if __name__ == "__main__":
    root = tk.Tk()
    interface = PremiereInterface(root)
    root.mainloop()








    class DeuxiemeInterface:
    def __init__(self, fenetre, url, mots_cles):
         self.bouton_sauvegarde = tk.Button(self.fenetre, text="Sauvegarder le rapport", command=self.sauvegarder_rapport)
        self.bouton_sauvegarde.pack()

    def sauvegarder_rapport(self):
        # Ouvrir un dialogue de sauvegarde pour choisir l'emplacement et le nom du fichier
        fichier = tk.filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])

        if fichier is None:
            return



        self.fenetre = fenetre
        self.fenetre.title("Rapport d'analyse")

        # Récupérer les informations nécessaires (à remplacer par les vraies données)
        # Ces données sont simulées ici pour l'exemple
        self.urls_trouvees = [
            {
                'url': 'https://www.example.com/page1',
                'liens_sortants': 5,
                'liens_internes': 10,
                'pourcentage_alt': 75,
                'mots_cles_pertinents': ['exemple', 'site', 'page'],
                'mots_cles_present': True
            },
            {
                'url': 'https://www.example.com/page2',
                'liens_sortants': 2,
                'liens_internes': 8,
                'pourcentage_alt': 60,
                'mots_cles_pertinents': ['exemple', 'site', 'autre'],
                'mots_cles_present': False
            },
            # Ajouter d'autres données simulées si nécessaire
        ]

        self.afficher_informations()

    def afficher_informations(self):
        for url_info in self.urls_trouvees:
            label_url = tk.Label(self.fenetre, text=f"URL : {url_info['url']}")
            label_url.pack()

            label_sortants = tk.Label(self.fenetre, text=f"Liens sortants : {url_info['liens_sortants']}")
            label_sortants.pack()

            label_internes = tk.Label(self.fenetre, text=f"Liens internes : {url_info['liens_internes']}")
            label_internes.pack()

            label_alt = tk.Label(self.fenetre, text=f"% de balises alt : {url_info['pourcentage_alt']}")
            label_alt.pack()

            label_mots_cles = tk.Label(self.fenetre, text=f"3 premiers mots clés pertinents : {', '.join(url_info['mots_cles_pertinents'][:3])}")
            label_mots_cles.pack()

            label_mots_cles_present = tk.Label(self.fenetre, text=f"Mots clés présents : {'Oui' if url_info['mots_cles_present'] else 'Non'}")
            label_mots_cles_present.pack()

if __name__ == "__main__":
    root = tk.Tk()
    interface = DeuxiemeInterface(root, "https://www.example.com", ["exemple", "site", "page"])
    root.mainloop()








