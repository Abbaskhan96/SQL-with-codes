import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.mydb = connector.connect(host = "127.0.0.1", 
                               user ="root", 
                               password="Abbas@123",
                               database="sql_join")
        

        self.curr = self.mydb.cursor(buffered=True)
    def creating_table(self, table_name):
        table_query = "create table if not exists {} (userName varchar(30), phone varchar(10), Salary varchar(6))".format(table_name)
        self.curr.execute(table_query)
        print("Table Created")
        self.curr.execute("describe users")
       

    def insert_table(self, table_name,userName, phone, Salary):
        insert_query = "insert into {} (userName, phone, Salary) values (%s, %s, %s)".format(table_name)
        values = (userName, phone, Salary)
     # 
        data=self.curr
        data.execute(insert_query, values)
        print("Data inserted")
        self.mydb.commit()

    def fetch_all(self, table_name):
        
            fetch_query = "select * from {}".format(table_name)
            print(table_name)
            curr= self.mydb.cursor()
            data = self.curr.execute(fetch_query)
            fetch = self.curr.fetchall()
            for x in fetch:
                print(x)

    # Deleting the table from the UserName and showing the result
    def delete_user(self, table_name, userName):
        delete_query = "delete '{}' where userName = '{}'".format(table_name, userName)
      
        data = self.curr.execute(delete_query)
 
        
    def update_user(self, table_name, name, newname, newphone, newsalary):
        print(name, table_name, newname, newphone, newsalary)
        query="update {} set userName='{}', phone='{}', Salary='{}'".format(table_name, newname)
    
obj = DBHelper()
#obj.creating_table("Users")
#obj.insert_table("Users","Moiz", "1234567890","100000")
obj.fetch_all("Users")
#obj.delete_user("users", "Moiz")