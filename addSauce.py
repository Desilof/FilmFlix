from sauce import *
import time
# Print add new record


def addSauce():
    record =[]
    title = str(input("Title of film: "))
    yearReleased  = int(input("Year of release: "))
    rating = str(input("Film rating: "))
    duration = int(input("Time lenght film (minutes): "))
    genre = str(input("Genre category: "))
    
    record.append(title)
    record.append(yearReleased)
    record.append(rating)
    record.append(duration)
    record.append(genre)

    cursor.execute("INSERT INTO tblFilms VALUES (NULL, ?,?,?,?,?)", record)
    sauce.commit()
    print(f"Title {title} successfully added to database")

    time.sleep(2)
    cursor.execute("SELECT * FROM tblFilms")
    row = cursor.fetchall()
    for items in row:
        print(items)



if __name__=="__main__":
    addSauce()