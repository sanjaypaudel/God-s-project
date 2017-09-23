from databaseconfiguration import dbconfig
class translator:
    #==============================================================
    # Attribute Declaration
    #==============================================================

    id=None
    name=None
    api_key=None
    input_element=None
    output_element=None
    submit_element=None
    source_language_element=None
    target_language_element=None
    url=None

    def __init__(self):
        None

    #==============================================================
    # Behaviour Declaration
    #==============================================================

    #Add Translator into database
    def AddTranslator(self):
        db=dbconfig()
        db.cursor.execute("insert into translator(name,api_key,input_element,output_element,submit_element,source_language_element,"+
        "target_language_element,url) value('%s','%s','%s','%s','%s','%s','%s','%s')"
        %(self.name, self.api_key, self.input_element, self.output_element, self.submit_element, self.source_language_element,
          self.target_language_element,self.url))
        db.db.commit()

    #Get translator details from id
    def GetTranslatorById(self,id):
        db=dbconfig()
        db.cursor.execute("select * from translator where id='%d'"%id)
        row=db.cursor.fetchone()
        translator1=self.DBObjecttMapper(row)
        return translator1

    #Get all translator in db
    def GetTranslators(self):
        db=dbconfig()
        translator_list=[]
        db.cursor.execute("select * from translator")
        result=db.cursor.fetchall()
        for row in result:
            translator1=self.DBObjecttMapper(row)
            translator_list.append(translator1)
        return translator_list

    #Map columns from query result to the class attribute
    def DBObjecttMapper(self,row):
        translator1=translator()
        translator1.id=row[0]
        translator1.name=row[1]
        translator1.api_key=row[2]
        translator1.input_element=row[3]
        translator1.output_element=row[4]
        translator1.submit_element=row[5]
        translator1.source_language_element=row[6]
        translator1.target_language_element=row[7]
        translator1.url=row[8]
        return translator1
    

