from sauce import *
# Print all records

def readSauce():
    cursor.execute("SELECT * FROM tblFilms")
    row = cursor.fetchall()
    for record in row:
        print(record)

if __name__=="__main__":
    readSauce()