from databaseconfiguration import dbconfig
import datetime
class test_result:
    #==============================================================
    # Attribute Declaration
    #==============================================================

    id=None
    testcase_id=None
    translator_id=None
    target_language_id=None
    forward_translation=None
    result=None
    created_date=None
    reverse_translation=None
    def __init__(self):
        None

    
    #==============================================================
    # Behaviour Declaration
    #==============================================================
    
    #Add new test case
    def AddTestCases(self):
        db=dbconfig()
        db.cursor.execute("insert into result(test_case_detail_id,translator_id,target_language_id,forward_translation,result,created_date,reverse_translation"+
        ") value('%d','%d','%d','%s','%f','%s','%s')"
        %(self.testcase_id, self.translator_id, self.target_language_id, self.forward_translation, self.result, self.created_date, self.reverse_translation))
        db.db.commit()
    
    #Get test results on the basis of field and parameter passed
    def GetTestResults(self,By,param):
        result_list=[]
        sql="select * from result"
        sql={
            'id':self.QueryBuilder("id",param),
            'testcase':self.QueryBuilder("test_case_detail_id",param),
            'language':self.QueryBuilder("target_language_id",param),
            'translator':self.QueryBuilder("translator_id",param)
        }[By]    
        db=dbconfig()
        db.cursor.execute(sql)
        result=db.cursor.fetchall()
        for row in result:
            result=self.DBObjectMapper(row)
            result_list.append(result)
        return result_list

    
    #Map columns from query result to the class attribute
    def DBObjectMapper(self,result):
        test_result1=test_result()
        test_result1.id=result[0]
        test_result1.testcase_id=result[1]
        test_result1.translator_id=result[2]
        test_result1.target_language_id=result[3]
        test_result1.forward_translation=result[4]
        test_result1.result=result[5]
        test_result1.created_date=result[6]
        test_result1.reverse_translation=result[7]
        return test_result1
        
    #Build sql query
    def QueryBuilder(self,field,param):
        sql="select * from result where "+field+"="+str(param)
        return sql
