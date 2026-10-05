#this process does not work, pyodbc needs to be installed but it fails
import pyodbc

#these values can be located in the excel spreadsheets where they reference the SQL server
server = ''
database = ''
username = ''
password = ''
#establish the connection
cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn,cursor()
