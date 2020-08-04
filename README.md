# hwy-bot
Posts pictures of local interstates. 


## Installation (linux server)
```
$ git clone https://github.com/bendotbike/hwy-bot.git /var/www/apps/hwy-bot
$ cd /var/www/apps/hwy-bot
$ pip install -r requirements.txt
$ npm install pm2@latest -g
$ pm2 start Main.py --name hwybot --interpreter python3 --chron $chron_interval$ # Schedules bot to run under 'hwybot' name at a certain chron interval
```

## Installation (client-side)
```
$ git clone https://github.com/bendotbike/hwy-bot.git /var/www/apps/hwy-bo c:/apps/hwy-bot
$ cd c:/apps/hwy-bot
$ pip install -r requirements.txt
$ python Main.py
```
