"""
Name: Christian Sangle
Date: Aug 18 2015
Notes: Does the parsing and will
print out the 50 of the domains with the highest precentage growth
"""
import mysql.connector
from mysql.connector import Error
import operator

class IndexSQLTest(object):
    def query(self,config):
        sorted_growth=[]
        self.config=config
        try:
            print('Connecting to MySQL database...')
            conn = mysql.connector.connect(**config)
            """
            Query: Select the domains which had registrations in the past 30 days.
            """
            if conn.is_connected():
                print('connection established.')
                query=""" SELECT domainaddr.domainname, DATE_FORMAT(domainaddr.datecreated, '%m/%d/%Y') \
                FROM domainaddr join mailing on
                domainaddr.mailaddr = mailing.addr \
                WHERE domainaddr.datecreated BETWEEN CURDATE() - INTERVAL 30 DAY AND NOW()
                ORDER BY domainaddr.domainname
                """
                cursor=conn.cursor()
                cursor.execute(query);
                rows = cursor.fetchall()
                emails_made_pastMonth={}

                """
                Create a dictionary that has all the domains registered emails for the past 30 days.
                """
                for row in rows:
                    if(row[0] in emails_made_pastMonth):
                        emails_made_pastMonth[row[0]]+=1;
                    else:
                        emails_made_pastMonth[row[0]]=1;
                """
                Query: Select ALL the domains which had registrations ever.
                """
                query=""" SELECT domainaddr.domainname, domainaddr.datecreated \
                FROM domainaddr join mailing on
                domainaddr.mailaddr = mailing.addr \
                WHERE domainaddr.datecreated BETWEEN DATE('1900-01-01') AND CURDATE()
                ORDER BY domainaddr.domainname
                """
                cursor.execute(query);
                rows = cursor.fetchall()
                #print('Total Row(s):', cursor.rowcount)
                emails_made_AllTime={}
                """
                Create a dictionary that has all the emails registered emails for all time.
                """
                for row in rows:
                    if(row[0] in emails_made_AllTime):
                        emails_made_AllTime[row[0]]+=1;
                    else:
                        emails_made_AllTime[row[0]]=1;
                        if(row[0] not in emails_made_pastMonth):
                            emails_made_pastMonth[row[0]]=0;

                growth={}
                """Calculate the growth for each dictionary key(i.e. domain name)"""
                for k in emails_made_pastMonth:
                    if(emails_made_pastMonth[k]==0):
                        growth[k]=0
                    else:
                        if (emails_made_pastMonth[k]==emails_made_pastMonth[k]):
                            growth[k]=(float(emails_made_pastMonth[k]-emails_made_AllTime[k])/emails_made_pastMonth[k])*100
                sorted_growth=list(sorted(growth, key=growth.__getitem__, reverse=False))
                """Convert dictionary to a list, sort the list based on the value of their growth percentage """
            else:
                print('connection failed.')

        except Error as error:
            print(error)

        finally:
            """Return list to main to print."""
            conn.close()
            print('Connection closed.')
            return sorted_growth

config={'user': 'christian',
          'password': 'christian',
          'port': 3307,
          'host': 'localhost',
          'database': 'domainmail'
          }

def main():
    sqlTesting=IndexSQLTest()
    val=sqlTesting.query(config);
    i=0;
    print("The Top 50 current web domains are: ")
    if len(val) <50:
        for k in val:
            print (k)
    else:
        while i!=50:
            print(val)
            i+=1
if __name__ == '__main__':
    main()
