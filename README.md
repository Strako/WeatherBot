# WeatherBot
A weather bot for Discord

Readme ! 

-Requirements
--------------------------------

	Python 3.10.6 Lastest
	Add your own discord token in the variable called DISCORD_TOKEN
	located in /bot-env/src/main.py	
-Dependencies:
--------------------------------

		Discord.py
			Python3.10 -m pip install -U discord.py
			----------------------------------------
			verify installation: 
			pip3 show discrod.py 
				or
			pip show discord.py		

		Certifi:
			pip3 install certifi
			----------------------------------------
			verify installation: 
			pip3 show certifi 
				or
			pip show certifi	

Activate virtual environment					
----------------------------------

	Run the following command inside the '/WeatherBot' folder

	$ source bot-env/bin/activate



Source Files
----------------------------------

Bot python source files are located inside '/WeaterBot/bot-env/src'


-Prefix & Commands
----------------------------------
	Bot commands can be added/modified inside the file main.py located at bot-env/src/main.py adding a new decorator @bot.command() 
	-Bot prefix
		'$'
	
	-Commands
		temp: Retrieve the actual temp in the specified argument and round to 2 digits of decimal point.
		humidity: Retrieve the actual temp in the specified argument and round to 2 digits of decimal point
	
	-Example
		$temp your_city
			Return: "Hi user: your_user 
					The actual temp in your_city its about actua_temp °C"
		$humidity your_city
			Return: "Hi user: your_user 
					The actual humidity in your_city its about actua_humidity %"
		

-Useful Links
----------------------------------
	discord.py
	https://discordpy.readthedocs.io/en/stable/intro.html

	open-meteo
	https://open-meteo.com/en/docs#latitude=19.4271&longitude=-99.1276&hourly=temperature_2m,precipitation&timezone=auto&start_date=2022-08-17&end_date=2022-08-17

	Timezone GMT
	https://stackoverflow.com/questions/15742045/getting-time-zone-from-lat-long-coordinates

	timezonefinder 6.1.0
	https://pypi.org/project/timezonefinder/?fbclid=IwAR03zYsDysU8HBt1KTGa-cKWmB7Nn-93Rho3Y5tPEIdcEUrVbyPGVoTbcEY

	nominatim 
	https://nominatim.openstreetmap.org/search?q=San=Luis+Potosi&format=json&polygon=1&addressdetails=1

	encryptoenv 0.0.2
	https://pypi.org/project/encryptoenv/#:~:text=To%20encrypt%20the%20.,key%20in%20their%20own%20program.

	Storing Tokens and Secrets
	https://tutorial.vcokltfre.dev/tips/tokens/

