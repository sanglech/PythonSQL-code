"""
Name: Christian Sangle
Date: Aug 18 2015
Company: IndexExchange
Notes:Starting point
"""
import SQLIndexTest
import sql_initialSetup
import time

if __name__ == '__main__':
    # service.py executed as script
    # do something
    sql_initialSetup.main()
    time.sleep(5)
    SQLIndexTest.main()
