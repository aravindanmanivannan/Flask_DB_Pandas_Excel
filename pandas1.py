from app import app
import pymysql
from config import  mysql
from flask import flash, request ,Response ,render_template , url_for , send_file
import pandas as pd
import os
import datetime
import random

@app.route('/')
def my_functions():
    try:
        conn = mysql.connect( )
        query = 'select * from students'
        my_data=pd.read_sql(query , conn )
        print(f"my_data : {my_data}")
        my_data1 = my_data[my_data['age']>=30]
        my_data2 = my_data[my_data['age']<30]
        
        file_name = (f" {datetime.datetime.now().strftime('%Y%m%d_%H%M%S')} + {random.randint(1,1000)}.xlsx")
        file_path = os.path.join(os.path.dirname(__file__) ,'Excel' , file_name) 
        #file_path = os.path.join(os.path.dirname(__file__) , 'Excel','my_filepandas346.xlsx') , 
        
        print(f"file_path : {file_path}")
        print(f"os.path.dirname(__file__) : {os.path.dirname(__file__)}")
        with pd.ExcelWriter(file_path) as output:
            my_data.to_excel(output,sheet_name = 'Full_Details' , index = False)
            my_data1.to_excel(output,sheet_name = 'Age_Above_30', index = False) 
            my_data2.to_excel(output, sheet_name='Age_below_30', index = False)
        
        print(f"path : {__file__ }")
        return  send_file (output, as_attachment=True, mimetype='application/vnd.ms-excel')
    
    except Exception as e:
        return f"There is an Error {e}"
    
if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))