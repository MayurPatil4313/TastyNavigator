pip install -r requirements.txt 
python3.9 manage.py collectstatic
set MYSQLCLIENT_CFLAGS=-I/path/to/mysqlclient/includes
set MYSQLCLIENT_LDFLAGS=-L/path/to/mysqlclient/libs
