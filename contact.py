import sqlite3


class Contact:
    def __init__(self, id, nom, adresse, sexe, telephoneprive, telephonedomicile, email, photo, fax, dateenregistrement):
        self.id = id
        self.nom = nom
        self.adresse = adresse
        self.sexe = sexe
        self.telephoneprive = telephoneprive
        self.telephonedomicile = telephonedomicile
        self.email = email
        self.photo = photo
        self.fax = fax
        self.dateenregistrement = dateenregistrement

    @classmethod
    def creer(cls, nom, adresse, sexe, telephoneprive, telephonedomicile, email,photo, fax, dateenregistrement):
        connection = sqlite3.connect('contact_personne.db')
        cursor = connection.cursor()
        cursor.execute('insert into contact values(?,?,?,?,?,?,?,?,?,?)', (cursor.lastrowid, nom, adresse, sexe, telephoneprive, telephonedomicile, email, photo, fax, dateenregistrement))
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def lire(cls, nom):
        connection = sqlite3.connect('contact_personne.db')
        cursor = connection.cursor()
        req = cursor.execute("select * from contact where nom='"+nom+"'")
        connection.commit()
        result = req.fetchall()
        return result

    @classmethod
    def liretout(cls):
        connection = sqlite3.connect('contact_personne.db')
        cursor = connection.cursor()
        cursor.execute('select * from contact')
        connection.commit()
        result = cursor.fetchall()
        return result



# if __name__ == "__main__":
#     c = Contact('', '', '', '', '', '', '', '', '','').liretout()
#     print(c[1][1])

#     c = Contact('', '', '', '', '', '', '', '', '','').lire('a','l')
#     print(c)
# #      Contact('', '', '', '', '', '', '', '', '').creer(10, '2', '', '', '', '', '', '')