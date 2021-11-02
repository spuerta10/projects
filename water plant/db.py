import pymysql



def to_DB(dia, max_turb, max_storing, min_turb, min_storing, avg_storing, avg_turb):
    connection = pymysql.connect( #establecer conexion con DB
        host = 'localhost',
        user = "root",
        password = 'Locura123',
        db = "assessment"
    )

    cursor = connection.cursor()

    sql = f"INSERT INTO information(day, max_turb,max_storing,min_turb,min_storing, avg_storing,avg_turb) VALUES ({dia},{max_turb},{max_storing},{min_turb},{min_storing},{avg_storing},{avg_turb})"
    cursor.execute(sql)

    connection.commit() #guardar los cambios en la DB
