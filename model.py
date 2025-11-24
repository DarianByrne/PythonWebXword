import DBcm

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
