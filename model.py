import DBcm

import platform

if "aws" in platform.uname().release:
    creds = {
        "user": "C00296036",
        "password": "xwordpasswd",
        "host": "C00296036.mysql.pythonanywhere-services.com",
        "database": "C00296036$default",
    }
else:
    creds = {
        "user": "xworduser",
        "password": "xwordpasswd",
        "host": "localhost",
        "database": "xwordDB",
    }

def add_to_database(p, m):
    SQL = """
        insert into log
          (pattern, matches)
        values
            (%s, %s)
    """
    with DBcm.UseDatabase(creds) as db:
        db.execute(SQL, (p, m))

def get_log_data():
    SQL = """
        select *
        from log
    """
    with DBcm.UseDatabase(creds) as db:
        db.execute(SQL)
        res = db.fetchall()
    return res
