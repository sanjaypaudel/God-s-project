from DatabaseConfiguration import dbconfig
class Languages:
    #==============================================================
    # Attribute Declaration
    #==============================================================
    
    #==============================================================
    # Behaviour Declaration
    #==============================================================
    
    #Add new langauge in db
    def AddLanguages(self, name):
        db=dbconfig()
        add_language = "INSERT INTO languages(name) VALUES(%s)"
        db.cursor.execute(add_language,(name,))
        db.db.commit()

    #Get all languages
    def GetLanguages(self):
        db=dbconfig()
        get_language = "SELECT name from languages"
        db.cursor.execute(get_language)
        language_list = [row[0] for row in db.cursor.fetchall()]
        return language_list

    #Get language detail by id
    def GetLanguageById(self,id):
        db=dbconfig()
        get_language = "SELECT name from languages where id = %s"
        db.cursor.execute(get_language,(id,))
        language_list = [row[0] for row in db.cursor.fetchall()]
        return language_list

#==============================================================
# Example of Class Declaration
#==============================================================

#languagesClass = Languages()
#languagesClass.AddLanguages("Hokkien")

#for row in languagesClass.GetLanguages():
    print (row)

#for row in languagesClass.GetLanguageById(9):
    print (row)