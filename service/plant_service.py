import mysql.connector

import properties

insert_plant = """
                insert into Plant(Name,const_humidity) values(%s,%s)
                    """
get_last_inserted_id = "SELECT LAST_INSERT_ID()"


def insertToDatabase(plant):
    mydb = mysql.connector.connect(
        host="136.244.85.251",
        user="unec",
        password="33290177aA+",
        database="haczkathon"
    )
    cursor = mydb.cursor()
    params = (plant.name, plant.opt_Humidity)
    cursor.execute(insert_plant, params)
    cursor.execute(get_last_inserted_id)
    row = cursor.fetchone()
    plant.id = row[0]
    mydb.commit()
    return plant
