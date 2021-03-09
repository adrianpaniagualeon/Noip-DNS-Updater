import requests 


#####################################
#             VARIABLE              #
#####################################
DOMAIN = ""
EMAIL = ""
PASSWORD = ""
#####################################




credentials = EMAIL+":"+PASSWORD
credentials = base64.b64encode(bytes(credentials, 'utf-8'))
credentials = str(credentials).replace("b'","")
headers = {"Authorization": "Basic "+credentials, "User-Agent": "Adrian Paniagua DNS UPDATER maintainer-github@adrianpaniagua.es"}


def get_ip():
	global my_ip

	my_ip = requests.get('http://icanhazip.com/').text
	my_ip = my_ip.strip()

def change_dns():
	global status
	url = "http://dynupdate.no-ip.com/nic/update?hostname="+HOST+"&myip="+my_ip
	r= requests.get(url,headers = headers)
	status = r.text

while True:
	print ("-------------------------------------------")
	print ("WEB ["+DOMAIN+"]")
	get_ip()
	print ("CURRENT IP ["+my_dns_ip+"]")
	change_dns()
	print ("STATUS ["+status+"]")
	print ("WAITING 5 MINUTES BEFORE THE NEXT EXECUTION")
	print ("-------------------------------------------\n\n")
	time.sleep(300)
