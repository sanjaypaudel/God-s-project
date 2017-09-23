from databaseconfiguration import dbconfig
import datetime
class testcases:
    #==========================================================
    #                   Attribute definition
    #==========================================================
    id=None
    input_sentence=None
    language=None
    created_date=None
    source_id=None
    source=None
    test_status=False

    
    #==============================================================
    # Behaviour Declaration
    #==============================================================
    
    #Add test case source in db
    def AddTestcaseSource(self,source):
        db=dbconfig()
        db.cursor.execute("insert into testcases(source) value('%s')"%source)
        db.db.commit()

    #Add test case with details in db
    def AddTestcases(self):
        db=dbconfig()
        db.cursor.execute("insert into testcase_details(input_sentence,source_language_id,created_date,test_case_id,test_status) value('%s','%d','%s','%d','%d')"
                          %(self.input_sentence,self.language,self.created_date,self.source_id,self.test_status))
        db.db.commit()

    #Get test case details from parameter and field passed
    def GetTestCases(self,By,param):
        testcase_list=[]
        sql="select * from testcase_details"
        sql={
            'id':self.QueryBuilder("id",param),
            'language':self.QueryBuilder("source_language_id",param),
            'source':self.QueryBuilder("test_case_id",param),
            'status':self.QueryBuilder("test_status",param)
        }[By]   
        db=dbconfig()
        db.cursor.execute(sql)
        result=db.cursor.fetchall()
        for row in result:
            result=self.DBObjectMapper(row)
            testcase_list.append(result)
        return testcase_list

    #Map columns from query result to the class attribute
    def DBObjectMapper(self,result):
        testcase1=testcases()
        testcase1.id=result[0]
        testcase1.input_sentence=result[1]
        testcase1.language=result[2]
        testcase1.created_date=result[3]
        testcase1.source_id=result[4]
        testcase1.test_status=result[5]
        return testcase1

    #Build sql query
    def QueryBuilder(self,field,param):
        sql="select * from testcase_details where "+field+"="+str(param)
        return sql

    