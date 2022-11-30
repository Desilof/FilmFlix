from sauce import *
import addSauce
# Print alter/change existing record

def amendSauce():
    locate = int(input("FilmID of edition: "))
    fieldName = str(input("Field name of edition (title, yearReleased, rating, duration, genre)? "))
    Newdata = str(input(f"Enter new {fieldName}: "))
    Newdataquote = "'" + Newdata + "'"


    cursor.execute(f"UPDATE tblFilms SET {fieldName} = {Newdataquote} WHERE filmID={locate}")
    print(f"FilmID {locate} has being successfully edited; {fieldName} for {Newdata}")


if __name__=="__main__":
    amendSauce()