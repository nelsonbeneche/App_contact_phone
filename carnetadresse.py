import tkinter
import tkinter as tk
import json
import base64
import csv
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFile
from contact import Contact
import regex
import os


class Carnetadresse(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Contact telephonique')
        self.geometry('400x200')
        menucontextuel = tk.Menu(self, tearoff=0)
        sousmenu = tk.Menu(menucontextuel, tearoff=0)
        sousmenu.add_command(label='tout', command='')
        # creation de menu deroulant
        mainmenu = tk.Menu(self, tearoff=0)
        menu1 = tk.Menu(mainmenu, tearoff=0)
        menu2 = tk.Menu(mainmenu, tearoff=0)
        menu3 = tk.Menu(mainmenu, tearoff=0)
        menu1.add_command(label='Ajouter', command=lambda: fenajout())
        menu1.add_command(label='Rechercher', command=lambda: fenlire())
        menu1.add_command(label='Modifier', command='')
        menu1.add_separator()
        menu1.add_command(label='Supprimer', command='')
        menu2.add_command(label='Vers un fichier csv', command=lambda: exporter())
        menu3.add_command(label="Concernant l'application contact telephonique")

        mainmenu.add_cascade(label='Contact', menu=menu1)
        mainmenu.add_cascade(label='Exporter les donnees', menu=menu2)
        mainmenu.add_cascade(label='Aide', menu=menu3)
        self.configure(menu=mainmenu)

        def creer():
            print("hello")
            with open('contact.json', 'w') as json_file:
                data = {'contact': [{'id': 12, 'nom': 'beneche', 'prenom': 'paul'}]}
                json.dump(data, json_file)
                json_file.write('\n')

        menucontextuel.add_command(label='Creer', command=lambda: creer())
        # dans le code suivant, on peut ajouter des sous menus
        menucontextuel.add_cascade(label='Lister', menu=sousmenu)
        menucontextuel.add_separator()
        menucontextuel.add_cascade(label='Supprimer', menu=sousmenu)

        def menu_contextuel(event):
            try:
                menucontextuel.tk_popup(event.x_root, event.y_root)

            finally:
                menucontextuel.grab_release()

        self.bind('<Button-3>', menu_contextuel)

        def fenajout():
            global txtnom, txtad, cmbsexe, txtemail, txttelpriv, txtteldom, txtfax, lbph, chemin
            fenajout = tk.Toplevel(self)
            larg = 330
            haut = 440
            largecran = fenajout.winfo_screenwidth()
            hautecran = fenajout.winfo_screenheight()
            x = (largecran / 2) - (larg / 2)
            y = (hautecran / 2) - (haut / 2)
            fenajout.geometry('%dx%d+%d+%d' % (larg, haut, x, y))
            fenajout.title("Ajouter | Carnet d'adresses")
            lbnom = tk.Label(fenajout, text='Nom')
            txtnom = tk.Entry(fenajout, width=30)
            lbad = tk.Label(fenajout, text='Adresse')
            txtad = tk.Entry(fenajout, width=30)
            lbsexe = tk.Label(fenajout, text='Sexe')
            cmbsexe = tk.Entry(fenajout, width=30)
            lbemail = tk.Label(fenajout, text='Email')
            txtemail = tk.Entry(fenajout, width=30)
            lbtelpriv = tk.Label(fenajout, text='Telephone prive')
            txttelpriv = tk.Entry(fenajout, width=30)
            lbteldom = tk.Label(fenajout, text='Telephone domicile')
            txtteldom = tk.Entry(fenajout, width=30)
            lbfax = tk.Label(fenajout, text='Fax')
            txtfax = tk.Entry(fenajout, width=30)
            lbda = tk.Label(fenajout, text='Nom')
            img = Image.open('images/311465180_431748872399430_7328635287821028835_n.jpg')
            im = ImageTk.PhotoImage(img.resize((200, 150)), master=fenajout)
            lbph = tk.Label(fenajout, background='gray', image=im)
            butpar = tk.Button(fenajout, text='Selectionner une image', command=lambda: parcourir())
            butenreg = tk.Button(fenajout, text='Enregistrer', command=lambda: ajouter())

            def parcourir():
                global chemin
                chemin = filedialog.askopenfilename(initialdir='/', filetypes=(('jpeg files', ['*.jpeg', '*.png']), ('All files', '*.*')))
                image = Image.open(chemin)
                img = ImageTk.PhotoImage(image.resize((200, 150)), master=fenajout)
                lbph.img = img
                lbph.configure(image=img)
                # return chemin
            # positionner les composants de la fenetre
            lbnom.grid(row=0, column=0, padx=5, pady=5)
            txtnom.grid(row=0, column=1, padx=5, pady=5)
            lbad.grid(row=1, column=0, padx=5, pady=5)
            txtad.grid(row=1, column=1, padx=5, pady=5)
            lbsexe.grid(row=2, column=0, padx=5, pady=5)
            cmbsexe.grid(row=2, column=1, padx=5,pady=5)
            lbtelpriv.grid(row=3, column=0, padx=5, pady=5)
            txttelpriv.grid(row=3, column=1, padx=5, pady=5)
            lbteldom.grid(row=4, column=0, padx=5, pady=5)
            txtteldom.grid(row=4, column=1, padx=5, pady=5)
            lbemail.grid(row=5, column=0, padx=5, pady=5)
            txtemail.grid(row=5, column=1, padx=5, pady=5)
            lbfax.grid(row=6, column=0, padx=5, pady=5)
            txtfax.grid(row=6, column=1, padx=5, pady=5)
            lbph.grid(row=7, column=1)
            butpar.grid(row=8, column=1)
            butenreg.grid(row=9, column=1, padx=5, pady=5)
            fenajout.resizable(width=False, height=False)
            fenajout.transient(self)
            fenajout.mainloop()

        def fenlire():
            global parcourir, butre, fenrechercher, txtnom_rech, lbad, txtad_rech, lbsexe, cmbsexe_rech,lbemail, txtemail_rech,lbtelpriv, txttelpriv_rech, lbteldom, txtteldom_rech, lbfax, txtfax_rech, lbph_rech
            fenrechercher = tk.Toplevel(self)
            larg = 270
            haut = 80
            largecran = fenrechercher.winfo_screenwidth()
            hautecran = fenrechercher.winfo_screenheight()
            x = (largecran / 2) - (larg / 2)
            y = (hautecran / 2) - (haut / 2)
            fenrechercher.geometry('%dx%d+%d+%d' % (larg, haut, x, y))
            fenrechercher.title("Rechercher | Carnet d'adresses")
            lbnom = tk.Label(fenrechercher, text='Nom')
            txtnom_rech = tk.Entry(fenrechercher, width=30)
            lbad= tk.Label(fenrechercher, text='Adresse')
            txtad_rech = tk.Entry(fenrechercher, width=30)
            lbsexe = tk.Label(fenrechercher, text='Sexe')
            cmbsexe_rech = tk.Entry(fenrechercher, width=30)
            lbemail = tk.Label(fenrechercher, text='Email')
            txtemail_rech = tk.Entry(fenrechercher, width=30)
            lbtelpriv = tk.Label(fenrechercher, text='Telephone prive')
            txttelpriv_rech = tk.Entry(fenrechercher, width=30)
            lbteldom = tk.Label(fenrechercher, text='Telephone domicile')
            txtteldom_rech = tk.Entry(fenrechercher, width=30)
            lbfax = tk.Label(fenrechercher, text='Fax')
            txtfax_rech = tk.Entry(fenrechercher, width=30)
            lbph_rech= tk.Label(fenrechercher, background='gray', width=200, height=100)
            butre = tk.Button(fenrechercher, text='Rechercher', command=lambda: lire())
            txtnom_rech.bind('<Return>', lire)
            # positionner les composants de la fenetre
            lbnom.grid(row=0, column=0, padx=5, pady=5)
            txtnom_rech.grid(row=0, column=1, padx=5, pady=5)
            butre.grid(row=1, column=1, padx=5, pady=5)
            fenrechercher.resizable(width=False, height=False)
            fenrechercher.transient(self)
            fenrechercher.mainloop()

        def ajouter():
            # chemin = parcourir()
            nom = txtnom.get()
            patter_nom = regex.search("^[a-zA-Z\\s]+$", nom)
            adresse = txtad.get()
            sexe = cmbsexe.get()
            email = txtemail.get()
            telephoneprive = txttelpriv.get()
            telephonedomicile = txtteldom.get()
            fax = txtfax.get()
            dateenregistrement = '20-01-1990'

            # appel a la methode inserer
            try:
                if chemin:
                    # messagebox.showerror('Information', 'Le chemin est vide ou inexistant.')
                    with open(chemin, 'rb') as f:
                        photo = base64.b64encode(f.read()).decode('utf-8')
                    if nom == '':
                        messagebox.showerror('Information', 'Vous devez remplir ce champ')
                    elif patter_nom:
                        Contact.creer(nom, adresse, sexe, telephoneprive, telephonedomicile, email, photo, fax, dateenregistrement)
                        messagebox.showinfo("Information", 'Votre contact a été ajouté avec succès.')
                    else:
                        if patter_nom is None:
                            messagebox.showerror('Information', 'Le nom ne correspond pas.')
            except:
                messagebox.showerror('Information', "Aucun image n'a ete selectionne.")

        def lire():
            nom = txtnom_rech.get()
            rech_ = Contact.lire(nom)  # appel a la fonction lire
            txtad_rech.delete(0, 'end')
            txtad_rech.insert(tkinter.END, rech_[0][2])
            cmbsexe_rech.delete(0, 'end')
            cmbsexe_rech.insert(tkinter.END, rech_[0][3])
            # redimensionner la fenetre et afficher la fenetre fille au centre
            large, haut = 530, 250
            large_ec = fenrechercher.winfo_screenwidth()
            haut_ec = fenrechercher.winfo_screenheight()
            x = (large_ec/2)-(large/2)
            y = (haut_ec/2)-(haut/2)
            fenrechercher.geometry('%dx%d+%d+%d' % (large, haut, x, y))  # redimensionner pour une fenetre plus large
            fenrechercher.title(f'{nom}|Carnet Adresses')  # afficher le nom de la personne dans le titre de la fenetre
            # positionner les composants
            butre.grid(row=0, column=2)
            lbad.grid(row=1, column=0, padx=5, pady=5)
            txtad_rech.grid(row=1, column=1, padx=5, pady=5)
            lbsexe.grid(row=2, column=0, padx=5, pady=5)
            cmbsexe_rech.grid(row=2, column=1, padx=5, pady=5)
            lbtelpriv.grid(row=3, column=0, padx=5, pady=5)
            txttelpriv_rech.grid(row=3, column=1, padx=5, pady=5)
            lbteldom.grid(row=4, column=0, padx=5, pady=5)
            txtteldom_rech.grid(row=4, column=1, padx=5, pady=5)
            lbemail.grid(row=5, column=0, padx=5, pady=5)
            txtemail_rech.grid(row=5, column=1, padx=5, pady=5)
            lbfax.grid(row=6, column=0, padx=5, pady=5)
            txtfax_rech.grid(row=6, column=1, padx=5, pady=5)
            lbph_rech.grid(row=1, column=2, rowspan=12, columnspan=12, sticky=('N', 'W', 'E', 'S'))
            # encoder en utf8 afin de construire l'image de la personne
            pho = str(rech_[0][7]).encode('utf-8')
            f = open('{}.png'.format(rech_[0][1]), 'wb')  # format de l'image avec extension png
            phot = base64.decodebytes(pho)
            f.write(phot)
            f.flush()
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            imgg = Image.open(f'{rech_[0][1]}.png')
            images = ImageTk.PhotoImage(imgg.resize((200, 300)), master=self)
            lbph_rech.images = images
            lbph_rech.configure(image=images)  # configurer l'image dans un label
            f.close()  # fermeture du fichier
            os.remove(f'{rech_[0][1]}.png')  # supprimer le fichier generer

        def exporter():
            if messagebox.askokcancel('Exporter les donnees vers un fichier csv', 'Voulez-vous continuer?'):
                # lire tous les enregistrements
                datacontact = Contact.liretout()
                # on utilise une comprehension de liste pour stocker les donnees de chaque attribut
                ident = [x[0] for x in datacontact]
                nom = [x[1] for x in datacontact]
                prenom = [x[2] for x in datacontact]
                sexe = [x[3] for x in datacontact]
                ecrire = [['id', 'nom', 'prenom', 'sexe']]
                # on fusionne tous les listes
                for ide, no, pre, se in zip(ident, nom, prenom,  sexe):
                    ecrire.append([ide, no, pre, se])
                with open('data_contact.csv', 'w', newline='', encoding='utf-8') as file:
                    ecrire_csv = csv.writer(file, delimiter=',')
                    # ecrire les valeurs de la liste dans le fichier csv
                    ecrire_csv.writerows(ecrire)
                    # on affiche un message de succes
                    messagebox.showinfo('Information', 'Votre contact a ete sauvegarde avec succes..')
                    # print('reussie..')


if __name__ == '__main__':
    app = Carnetadresse()
    app.state('zoomed')

    def fermer():
        if messagebox.askokcancel('Information', "Voulez-vous fermer le logiciel?"):
            app.destroy()
    app.protocol('WM_DELETE_WINDOW', fermer)
    app.mainloop()
