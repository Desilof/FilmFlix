from sauce import *
import time
# Print delete unique record


def deleteSauce():
    hell = int(input("Enter filmID to complete delete: "))
    cursor.execute(F"DELETE FROM tblFilms WHERE filmID={hell}")
    sauce.commit()

    time.sleep(1)

    print(f"The film with ID {hell} ahd being successfully deleted from database")



if __name__=="__main__":
    deleteSauce()