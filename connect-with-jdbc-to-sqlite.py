import jaydebeapi
conn = jaydebeapi.connect(
    "org.sqlite.JDBC",
    "jdbc:sqlite:sample.db",
    [],
    "jar/sqlite-jdbc-3.34.0.jar")
curs = conn.cursor()
curs.execute('drop table PERSON')
curs.execute('create table PERSON (id integer, name string)')
curs.execute("insert into PERSON values (1, 'Alice')")
curs.execute("insert into PERSON values (1, 'Bob')")
curs.execute("select * from PERSON")

for row in curs.fetchall():
    print(row)

curs.close()
conn.close()
