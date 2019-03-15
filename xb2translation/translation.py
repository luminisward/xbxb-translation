import os
import sqlite3

class Translation:
  def __init__(self):
    db_path = os.path.join(os.path.dirname(__file__), 'common_ms.db')
    self.conn = sqlite3.connect(db_path)
    # self.conn.set_trace_callback(print)
    self.c = self.conn.cursor()

  def query(self, language, query_string, tablename = None, limit=100):
    table_filter = ''
    if tablename:
      table_filter = 'AND tablename=' + '"' + tablename + '"'
      sql = 'SELECT tablename,id,cn,fr,gb,ge,it,jp,sp,tw FROM common WHERE %s LIKE ? %s LIMIT %d;' % (language, table_filter, limit)
    else:
      sql = 'SELECT tablename,id,cn,fr,gb,ge,it,jp,sp,tw FROM common WHERE %s LIKE ? LIMIT %d;' % (language, limit)

    # print(sql)
    self.c.execute(sql, ('%' + query_string + '%', ))
    data = map(lambda row: row + ('all',), self.c.fetchall())
    return data

  def query_dialogue(self, language, query_string, tablename = None, limit=100):
    table_filter = ''
    if tablename:
      table_filter = 'AND tablename=' + '"' + tablename + '"'
      sql = 'SELECT dialogue.tablename,id,cn,fr,gb,ge,it,jp,sp,tw,game FROM dialogue INNER JOIN dialogue_table ON dialogue.tablename=dialogue_table.tablename WHERE %s LIKE ? %s LIMIT %d;' % (language, table_filter, limit)
    else:
      sql = 'SELECT dialogue.tablename,id,cn,fr,gb,ge,it,jp,sp,tw,game FROM dialogue INNER JOIN dialogue_table ON dialogue.tablename=dialogue_table.tablename WHERE %s LIKE ? LIMIT %d;' % (language, limit)
    
    self.c.execute(sql, ('%' + query_string + '%', ))
    return self.c.fetchall()


  def __del__(self):
    self.c.close()
    self.conn.commit()
    self.conn.close()
