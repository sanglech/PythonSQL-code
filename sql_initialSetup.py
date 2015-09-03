"""
Name: Christian Sangle
Date: Aug 18 2015
Notes: Creates the initial database and populates it with data.
"""
import mysql.connector
from mysql.connector import Error
import operator

def setup(config):
      try:
          conn = mysql.connector.connect(**config)
          if conn.is_connected():
              cursor=conn.cursor()
              sqlCreate='CREATE DATABASE IF NOT EXISTS domainmail'
              cursor.execute(sqlCreate)
              #print('Created MySQL database domainmail')

              sqlCreate='USE domainmail'
              cursor.execute(sqlCreate)
              config['database']='domainmail'

              sqlCreate='''CREATE TABLE IF NOT EXISTS mailing \
              (addr VARCHAR(255) NOT NULL)'''
              cursor.execute(sqlCreate)
              #print('Created table mailing in domainmail')

              sqlCreate='''CREATE TABLE IF NOT EXISTS domainaddr
              (id int(11) NOT NULL AUTO_INCREMENT,\
              mailaddr VARCHAR(255) NOT NULL REFERENCES mailing(addr),\
              domainname VARCHAR(255) NOT NULL,\
              datecreated VARCHAR(255) NOT NULL,\
              PRIMARY KEY (id)
              )'''
              #print('Created table domanaddr in domainmail')
              f=open('domainmail.sql','r')
              sql=f.read()
              cursor.execute(sql)
      except Error as e:
          print(e)
      finally:
          conn.close()

config={'user': 'christian',
          'password': 'christian',
          'port': 3307,
          'host': 'localhost',
          }
def main():
    setup(config)

if __name__ == '__main__':
    main()
