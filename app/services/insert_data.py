from app.models.Cars import Cars
from app.utils.pgsql import SqlDB
from sqlalchemy import insert

sql = SqlDB()


def all_tools(data):
    with sql.transaction() as session:
        insert_data = insert(Cars).values(data)
        session.execute(insert_data)
        return "Done"
