import sqlalchemy as db

db_engine = db.create_engine('sqlite:///refdataDB.db')
conn = db_engine.connect()
#conn.execute('CREATE TABLE markets (market_id text PRIMARY KEY NOT NULL, status integer NOT NULL);')
conn.execute('INSERT INTO markets (market_id, status)  VALUES (\'SL\', 1);')
conn.execute('INSERT INTO markets (market_id, status)  VALUES (\'IND\', 0);')

result = conn.execute('select * from markets')

for row in result:
    print (row)
