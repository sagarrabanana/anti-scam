import requests
import random
import string
import csv

cont=0
veces=0


f = open("nombres.csv","r")
dt = csv.reader(f)
nombres = list(dt)
f.close()

p = open("apellidos.csv","r")
dp = csv.reader(p)
apellidos = list(dp)
p.close()


while True:
  nombresList=[]
  apellidosList=[]
  for x in nombres:

    nombresList.append(x[0].capitalize())

  name=nombresList[random.randint(1,9000)]
  print(name)

  for x in apellidos:

    apellidosList.append(x[0].capitalize())
  surname=apellidosList[random.randint(1,25000)]
  print(surname)
  numb=random.randint(600000000,729999999)
  print(numb)
  print('34'+str(numb))

#-------
  extensions = ['com']
  domains = ['gmail','yahoo','hotmail','outlook']
  randomChar=['','.','_']

  winext = extensions[random.randint(0,len(extensions)-1)]
  windom = domains[random.randint(0,len(domains)-1)]
  winchar=randomChar[random.randint(0,len(randomChar)-1)]

  acclen = random.randint(0,3)

  winacc = ''.join(random.choice(string.ascii_lowercase) for _ in range(acclen))
 
  numb=random.randint(0,100)
  mail = name.replace(' ','')+ winchar+winacc +str(numb ) + '@' + windom + '.' + winext
  veces=veces+1
  print(veces)
  print(mail)
#-----


  url=['https://somethingf.com/thankyou.php'
  ,'https://fvanish.com/thankyou.php'
  ,'https://azinnovates.pro/thankyou.php'
  ,'https://somberf.com/thankyou.php'
  ,'https://esprofitmax57.xyz/thankyou.php'
  ,'https://ch1system.top/thankyou.php'
  ,'https://whomeverf.com/thankyou.php'
  ,'https://waryf.com/thankyou.php'
  ,'https://cscrape.com/thankyou.php'
  ,'https://additionalk.com/thankyou.php'
  ,'https://afidastore.com/thankyou.php'
  ,'https://waryf.com/thankyou.php'
  ,'https://whoeverf.com/thankyou.php'
  ,'https://whicheverf.com/thankyou.php'
  ,'https://whetherk.com/thankyou.php'
  ,'https://obesek.com/thankyou.php'
  ,'https://adamantc.com/thankyou.php'
  ,'https://naughtyk.com/thankyou.php'
  ,'https://rusticio.com/thankyou.php']

  data={
  'f_name': name,
  'l_name': surname,
  'email': mail,
  'phone': str(numb),
  'politics': 'on',
  'over': 'on',
  'pixel_id': '',
  'phone2': '34'+str(numb),
  'url_params': '',
  }
  urlObj=url[random.randint(0,len(url)-1)]
  response=requests.post(urlObj,data=data)
  print(urlObj)
  print('Respuesta: '+ str(response.status_code))
