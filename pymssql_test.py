import pymssql
'''
Contains a sample of how to structure pymssql to make a connection using tsql configs and execute queries.
'''

def testpymssql():

	#This string has been set up in a way that it can accept defined parameters.  This is demonstrated below when the command executes.
	str_SQL = "SELECT * FROM TestTable WHERE ColumnOne = %s AND ColumnTwo = %s)"

	#You will need to replace USERNAME, PASSWORD, and DB_NAME with your own values. 'testconnection' is the connection defined in the
	#tsql config file described in the Readme file.
    try:
        conn = pymssql.connect( 'testconnection',
                                'USERNAME',
                                'PASSWORD'),
                                'DB_NAME',
                                as_dict=True)

        cursor = conn.cursor()

        #This will insert the values into the str_SQL string command
        #If our string was completely static, then we can just pass str_SQL as
        #a single parameter into execute without overloading the method.
    	cursor.execute(str_SQL, ("valueOne", "valueTwo"))
    	for row in cursor:
    		print row

    	cursor.close()
    	conn.close()

    except pymssql.ProgrammingError as e:
	print >> sys.stderr, ("testpymssql: " + str(e))
            return {'error': e}
    except pymssql.OperationalError as e:
	print >> sys.stderr, ("testpymssql: " + str(e))
            return {'error': e}
