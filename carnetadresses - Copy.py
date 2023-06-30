import \
    sqlite3.dbapi2
import tkinter as tk
import json
import base64
import csv
import pandas as pd
from PIL import Image, ImageTk
from sqlite3 import dbapi2
connection = dbapi2.connect('opl.db')
connection.execute("PRAGMA key='hello'")
cursor = connection.cursor()
cursor.execute('insert into nom values(?,?)', ('salt', 'hello'))
connection.commit()
print('okay')
cursor.close()
connection.close()
#
#
# class Contact(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title('Contact telephonique')
#         self.geometry('400x200')
#         menucontextuel = tk.Menu(self, tearoff=0)
#         sousmenu = tk.Menu(menucontextuel, tearoff=0)
#         sousmenu.add_command(label='tout', command='')
#         # creation de menu deroulant
#         mainmenu = tk.Menu(self, tearoff=0)
#         menu1 = tk.Menu(mainmenu, tearoff=0)
#         menu1.add_command(label='Ajouter', command=lambda: fenajout())
#         menu1.add_command(label='Rechercher', command=lambda: lire())
#         menu1.add_command(label='Modifier', command='')
#         menu1.add_separator()
#         menu1.add_command(label='Supprimer', command='')
#
#         mainmenu.add_cascade(label='Contact', menu=menu1)
#         self.configure(menu=mainmenu)
#
#         def creer():
#             print("hello")
#             with open('contact.json', 'a') as json_file:
#                 data = {'contact': [{'id': 12, 'nom': 'beneche', 'prenom': 'paul'}]}
#                 json.dump(data, json_file)
#                 json_file.write('\n')
#
#         menucontextuel.add_command(label='Creer', command=lambda: creer())
#         # dans le code suivant, on peut ajouter des sous menus
#         menucontextuel.add_cascade(label='Lister', menu=sousmenu)
#         menucontextuel.add_separator()
#         menucontextuel.add_cascade(label='Supprimer', menu=sousmenu)
#
#         def menu_contextuel(event):
#             try:
#                 menucontextuel.tk_popup(event.x_root, event.y_root)
#
#             finally:
#                 menucontextuel.grab_release()
#
#         self.bind('<Button-3>', menu_contextuel)
#
#         def fenajout():
#             data = [['id', 'nom', 'prenom', 'image']]
#             data.append(
#                 [
#                     29,
#                     'nelson',
#                     'jetrude',
#                     ''])
#             with open('images/chucky_01.jpeg', 'rb') as f:
#                 img = base64.b64encode(f.read()).decode('utf-8')
#             with open('contact_person.csv', 'w', newline='', encoding='utf-8') as file:
#                 writer = csv.writer(file, delimiter=',')
#                 writer.writerows(data)
#                 # file.close()
#
#             # fenajout = tk.Toplevel(self)
#             # with open('images/chucky_01.jpeg', 'rb') as f:
#             #     img = base64.b64encode(f.read()).decode('utf-8')
#             # # les donnees du formulaire enregistrement dans une structure de liste de dictionnaire
#             # data = {'id': 4, 'nom': 'AAllert', 'prenom': 'paul', 'image': ''}
#             #
#             # with open('contact_person.json', 'w') as json_file:
#             #     json_enreg = json.dumps(data, separators=(',', ':'))
#             #     json_file.write(json_enreg)
#             #     json_file.write('\n')
#             #     print('enregistrement reussie..')
#
#         def lire():
#             # liref = pd.read_csv('contact_person.csv')
#             # print(liref)
#             with open('contact_person.csv', 'r') as file:
#                 lirefic = csv.reader(file)
#                 # print(lirefic)
#                 for data in lirefic:
#                     print(f'le nom est:{data[1]}')
#             #
#             #         image_data = base64.b64decode(data[3])
#             #         with open( 'image_decoded.jpg','wb') as image_file:
#             #             image_file.write(image_data)
#             # with open('contact.json', 'r') as file:
#             #     json_lire = file.read()
#             #     dat = json.loads(json_lire)
#             #     for row in dat:
#             #         # imag = base64.b64decode(dat['image'])
#             #         id = dat['id']
#             #         print(id)
#                 # for cont in dat['contact']:
#                 #     print(cont['id'])
#
#
#
# if __name__ == '__main__':
#     app = Contact()
#     app.mainloop()
