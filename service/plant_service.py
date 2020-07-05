import mysql.connector

from models.plant import Plant

insert_plant = """
                insert into Plant(Name,const_humidity) values(%s,%s)
                    """
get_last_inserted_id = "SELECT LAST_INSERT_ID()"

get_plants = "select * from Plant"
get_plant_by_id = "select * from Plant where Id = %s "


# todo delete db credential at pushing
def connect_to_db():
    return mysql.connector.connect(
        database="hackathon"
    )


def insertToDatabase(plant):
    mydb = connect_to_db()
    cursor = mydb.cursor()
    params = (plant.name, plant.opt_humidity)
    cursor.execute(insert_plant, params)
    cursor.execute(get_last_inserted_id)
    row = cursor.fetchone()
    plant.id = row[0]
    mydb.commit()
    return plant


def get_plant_from_db(id):
    mydb = connect_to_db()
    cursor = mydb.cursor()
    data = []
    if id is None:
        cursor.execute(get_plants)
        rows = cursor.fetchall()
        if rows is not None:
            for row in rows:
                print(row)
                data.append(Plant(row[0], row[1], row[2]))
    else:
        cursor.execute(get_plant_by_id, (id,))
        row = cursor.fetchone()
        if row is not None:
            data.append(Plant(row[0], row[1], row[2]))


    return data
