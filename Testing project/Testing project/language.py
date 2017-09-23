from databaseconfiguration import dbconfig
class Languages:
    #==============================================================
    # Attribute Declaration
    #==============================================================

    id=None
    name=None
    
    #==============================================================
    # Behaviour Declaration
    #==============================================================
    
    #Add new langauge in db
    def AddLanguages(self):
        db=dbconfig()
        db.cursor.execute("insert into languages(name) value('%s')"%self.name)
        db.db.commit()

    #Get all languages
    def GetLanguages(self):
        language_list=[]
        db=dbconfig()
        db.cursor.execute("select * from languages")
        result=db.cursor.fetchall()
        for row in result:
            Language=Languages()
            Language.id=row[0]
            Language.name=row[1]
            language_list.append(Language)
        return language_list

    #Get language detail by id
    def GetLanguageById(self,id):
        db=dbconfig()
        Language1=Languages()
        db.cursor.execute("select * from languages where id='%d'"%id)
        result=db.cursor.fetchone()
        Language1.id=result[0]
        Language1.name=result[1]
        return Language1

