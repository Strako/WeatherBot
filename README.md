# WeatherBot
A weather bot for Discord

Readme ! 

-Requirements
--------------------------------

	Python 3.10.6 Lastest
	
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

	-Bot prefix
		'$'
	
	-Commands
		test: prints 'Aloha Wachin concatenated with the user name who sends the message'.

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

Bot info [Important!]
----------------------------------
Invite link
https://discord.com/api/oauth2/authorize?client_id=1009683608312746046&permissions=2048&scope=bot%20applications.commands

Token -Base64 [ Character set: UTF-8, Newline separator: LF(Unix) ] (Decode before use in code)
TVRBd09UWTRNell3T0RNeE1qYzBOakEwTmcuR1pNZDRvLmpHcDVVTlRFMjY2cXdHakNYQ0tiaVp3OW9lbE05T3ZkRmxHamk0
