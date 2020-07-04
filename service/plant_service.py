from sqlalchemy import text
from sqlalchemy import exc as execute

insert_plant = text("""
                insert into Plant(name,optional_humidity) values(:name,:optimal_humidity)
                    """)

def insertToDatabase(plant):

    rs = execute(insert_plant, name=plant.name,optimal_humidity=plant.opt_Humidity)

    return None