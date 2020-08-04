# hwy-bot
Posts pictures of local interstates. 


## Installation (linux server)
```
$ git clone https://github.com/bendotbike/hwy-bot.git /usr/share/pyshared/
$ cd /usr/share/pyshared/hwy-bot
$ sudo chown $user:$user /usr/share/pyshared/hwybot
$ pip install -r requirements.txt
$ npm install pm2@latest -g
$ touch .env #Make .env file like below
# Schedule bot to run under 'hwybot' name at a certain chron interval:
$ pm2 start Main.py --name hwybot --interpreter python3 --chron $chron_interval$ # Schedules bot to run under 'hwybot' name at a certain chron interval
```

## Installation (client-side)
```
$ git clone https://github.com/bendotbike/hwy-bot.git /var/www/apps/hwy-bot /usr/share/pyshared/
$ cd /usr/share/pyshared/hwy-bot
$ sudo chown $user:$user /usr/share/pyshared/hwybot
$ pip install -r requirements.txt
$ touch .env #Make .env file like below
$ python Main.py
```

## .env file
Register your Twitter account as a developer account on Twitter and get the following info for this file.

Create in the same directory as you saved this repo. ```$ touch .env```
Be sure not to upgrade this file to version control.
```
consumer_key="YOUR_CONSUMER_KEY"
consumer_secret="YOUR_CONSUMER_SECRET"
access_token_key="YOUR_ACCESS_TOKEN"
access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
```
