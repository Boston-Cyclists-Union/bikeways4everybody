import requests
username = 'bcu'
url = 'https://' + username + '.cartodb.com/api/v2/sql'
sql = {'q':'SELECT process_data()'}
res = requests.get(url, data=sql)