from app import app
import pymysql
from config import  mysql
from flask import flash, request ,Response ,render_template , url_for , send_file
import pandas as pd
import os
#import xlswritter

   
@app.route('/')
def my_functions():
    try:
        conn = mysql.connect( )

        """ cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute ('select * from students')
        data = cursor.fetchall() """

        query = 'select * from students'
        #query1 = 'Select * from students where age >=30'
        #query2 = 'Select * from students where age <30'
        my_data=pd.read_sql(query , conn )
        my_data1 = my_data[my_data['age']>=30]
        my_data2 = my_data[my_data['age']<30]

        #my_data1=pd.read_sql(query1 , conn)
        #my_data2=pd.read_sql(query2 , conn)
        print(f"my_data : {my_data}")

        #output ='C:\\Users\\DELL\\Projects\\Flask_MySql_Excel\\Excel\\my_filepandas346.xlsx'
        file_path = os.path.join(os.path.dirname(__file__) , 'Excel', 'my_filepandas346.xlsx')
        with pd.ExcelWriter(file_path) as output:
            my_data.to_excel(output,sheet_name = 'Full_Details' , index = False)
            my_data1.to_excel(output,sheet_name = 'Age_Above_30', index = False) 
            my_data2.to_excel(output, sheet_name='Age_below_30', index = False)
        
        print(f"path : {__file__ }")
        return  send_file (output, as_attachment=True, mimetype='application/vnd.ms-excel')
    
        #return f"File downloaded {my_data.to_excel('my_filepanda32.xlsx')}"
        #return my_data.to_excel('my_filepandas23.xlsx') 
        #Response (my_data.to_excel('my_filepandas23.xlsx'), mimetype="application/ms-excel")
    except Exception as e:
        return f"There is an Error {e}"
    
if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))