#!/usr/bin/env python
#coding: utf8 

import os
import tdclient
import time
import sys
from tabulate import tabulate
import csv

apikey = os.getenv("TD_API_KEY")
db_name = str(None)
query_str = str(None)
output_format = str(None)

#__Assign query elements from command line arguments__
       
def executeQuery():
    try:
        db_name = sys.argv[1]
   	table_name = sys.argv[2]
        column_list = sys.argv[3]
    except: 
    	print("DatabaseName, TableName and ColumnList are required inputs")
    else:
    	if len(sys.argv) > 4:
	    min_time = sys.argv[4]
    	else:
	    min_time = 'NULL'

        if len(sys.argv) > 5:
	    max_time = sys.argv[5]
        else:
	    max_time = 'NULL'

        if len(sys.argv) > 6:
	    query_engine = sys.argv[6]
	    print 'QueryEngine: {0}'.format(query_engine)
       
	if len(sys.argv) > 7:
            output_format = sys.argv[7]
	    print 'OutputFormat: {0}'.format(output_format)
	else:
	    output_format = None

#__Construct query__
    	query_str = "SELECT "+column_list+" from "+table_name+" WHERE TD_TIME_RANGE(time,"+min_time+","+max_time+")"
    	print 'Query: {0}'.format(query_str)
	print 'DatabaseName: {0}'.format(db_name)

    	with tdclient.Client(apikey) as client:
    	    job = client.query(db_name, query_str, result_url=None, priority=None, retry_limit=None, type=query_engine)
    	    job.wait()
	    if output_format == 'tabular' or output_format == None:
		headers = column_list.split(",")
		print tabulate(job.result(),headers,tablefmt="grid")
	    elif output_format == 'csv':
		with open('TD_QueryResults.csv', 'wb') as csvfile:
    		    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    		    headers = column_list.split(",")
		    spamwriter.writerow(headers)
		    for row in job.result():
			spamwriter.writerow(row)
	    else:
                 print 'Invalid output format requested'
executeQuery();
