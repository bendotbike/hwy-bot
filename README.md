# hwy-bot
Posts pictures of local interstates. 


## Installation (linux server)
```
$ git clone https://github.com/bendotbike/hwy-bot.git /usr/share/pyshared/
$ cd /usr/share/pyshared/hwy-bot
$ sudo chown $user:$user /usr/share/pyshared/hwybot
# (Chrome and chrome driver instructions thanks to - https://gist.github.com/ziadoz/3e8ab7e944d02fe872c3454d17af31a5)
$ sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
$ sudo echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
$ sudo apt-get -y update
$ sudo apt-get -y install google-chrome-stable
$ pip3 install -r requirements.txt
$ chrome_driver_version=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE`
$ wget -N https://chromedriver.storage.googleapis.com/$chrome_driver_version/chromedriver_linux64.zip -P ~/
$ unzip ~/chromedriver_linux64.zip -d ~/
$ rm ~/chromedriver_linux64.zip
$ sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
$ sudo chown root:root /usr/local/bin/chromedriver
$ sudo chmod 0755 /usr/local/bin/chromedriver
$ npm install pm2@latest -g
$ touch .env #Make .env file like below
# Schedule bot to run under 'hwybot' name at a certain chron interval:
$ pm2 start Main.py --name "hwybot" --interpreter python3 --cron "cron_pattern (use http://cron.guru or something)"
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
