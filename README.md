# hwy-bot
Posts pictures of local interstates. 

## Installation (client-side)
```
$ git clone https://github.com/bendotbike/hwy-bot.git /var/www/apps/hwy-bot
$ cd /var/www/apps/hwy-bot
$ pip install requests python-twitter beautifulsoup
$ python3 Main.py
```

## Installation (server)
git clone https://github.com/bendotbike/hwy-bot.git /var/www/apps/hwy-botr
```
$ git clone https://github.com/bendotbike/hwy-bot.git /var/www/apps/hwy-bot
$ cd /var/www/apps/hwy-bot
$ pip install requests python-twitter beautifulsoup
$ npm install pm2@latest -g
$ $ pm2 start Main.py --name hwybot --interpreter python3 --chron $chron_interval$
```
