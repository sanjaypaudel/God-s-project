from databaseconfiguration import dbconfig
import datetime
class search:
    #==============================================================
    # Attribute Declaration
    #==============================================================
    id=None
    result_id=None
    result_url=None
    url_no=None
    created_date=None
    
    #==============================================================
    # Behaviour Declaration
    #==============================================================
    
    #Add search result into search table on the basis of result
    def AddSearchResults(self):
        db=dbconfig()
        db.cursor.execute("insert into result_url(result_id,result_text,url_no,created_date"+") value('%d','%s','%d','%s')"
        %(self.result_id, self.result_url, self.url_no, self.created_date))
        db.db.commit()

    #Get list of result from the parameter and field passed
    def GetSearchResults(self,By,param):
            search_list=[]
            sql="select * from result_url"
            sql={
                'id':self.QueryBuilder("id",param),
                'result':self.QueryBuilder("result_id",param)
            }[By]    
            db=dbconfig()
            db.cursor.execute(sql)
            result=db.cursor.fetchall()
            for row in result:
                result=self.DBObjectMapper(row)
                search_list.append(result)
            return search_list

    #Map columns from query result to the class attribute
    def DBObjectMapper(self,result):
        search1=search()
        search1.id=result[0]
        search1.result_id=result[1]
        search1.result_url=result[2]
        search1.url_no=result[3]
        search1.created_date=result[4]
        return search1
    
    # Build sql query 
    def QueryBuilder(self,field,param):
        sql="select * from result_url where "+field+"="+str(param)
        return sql

    
