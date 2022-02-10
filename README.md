# CraftBeerPi4 Kettle Logic for PID Auto Tune

- Initial Version which is based on the CraftbeerPi3 Plugin from IndyJoeA (https://github.com/IndyJoeA/cbpi_PIDAutoTune)
	- The purpose of this plugin is to autotune your System and determine automatically P, I and D values to optimize the heating for your system.
	- The derived values have to be entered later in your PID Kettle Logic.
	- For more info on PID and autotuning, you can check out the following articles:
    - (https://github.com/Manuel83/craftbeerpi/wiki/Autotune-PID)
    - (https://github.com/Manuel83/craftbeerpi/wiki/Manual-PID-adjustment)


- Installation:
	You can install it directly via pypi.org:	
	- sudo pip3 install cbpi4-PID-AutoTune 

	Alternativeley you can install (or clone) it from the GIT Repo. In case of updates, you will find them here first:
	- sudo pip3 install https://github.com/avollkopf/cbpi4-PID_AutoTune/archive/main.zip

	Afterwards you will need to activate the plugin:
	- cbpi add cbpi4-PID_AutoTune
	
	- cbpi >= 4.0.0.45 is required

	Important: Don't mix up the '-' and '_'
	
- Parameters:	
	- Output Step: Defines the output power in % used for steps to ramp up to a temperature. Default is 100%.
	- Max Outpuz: Defines the maximum outpout power in % you are using with your system. Default is 100%.
	- Lockback Seconds: Defines the time in seconds how far the routine is locking back to identify temperature peaks. 30 seconds is typical. If you experience issues, increase the time (e.g. 60 seconds)
	
- Hardware Setup:
	- After installation go to hardware settings
	- Select PIDAutoTune as Kettle logic.
	- Select the Heater, Agitator and Sensor for your Kettle
	- Enter the parameters with the default values or change them to your needs as shown in the image below.
	
![PIDAutoTune Settings](https://github.com/avollkopf/cbpi4-PID_AutoTune/blob/main/Settings_Autotune.png?raw=true)

- Usage:
	- Go tou your cbpi4 dashboard and add a Kettle and KettleLogic.
	- You should run the Autotune as realistic as possible.
		- Therefore you should at least use the typical amount of water you are using also for a mash
		- Set a Kettle temperature via the Kettle Logic. I selected for instance 67C which is somehow between the typical mash temps of 62C and 73C
		- In my case I added even malt which is easy with the braumeister malt pipe as I just added the pipe back into the kettle after a full brewing step and was using the same amount of water
	- Start the automatic Kettle Logic (Click on the car symbol) and have a beer as it'll take sme thime. The system will heat up to the setpoint and overshoots intentionally.
	- If you are having a pump in your system or other agitators that may impact the heating cycle, you should run them also during the Autotune process
	- It is waiting until the temp is going down 0.5C below the target value.
	- Then it is repeating this procedure several times.
	- While running, it is writing a log file into the logs directory -> autotune.log
	- If successfull, the P, I and D values are listed in the log file and a message is displayed in the dashboard. 
	- You can copy this message and enter the values then afterwards into your real Kettle Logic you are using for the mashing.
	
![PIDAutoTune Results](https://github.com/avollkopf/cbpi4-PID_AutoTune/blob/main/AutoTune.png?raw=true)	
	
Changelog:

- 10.02.22: (0.0.8): Fix to display correct power in actor button and mqtt when process is starting
- 09.02.22: (0.0.7): Added default target temp in case user did not choose target tamp and alarm if target temp is below current temp
- 20.11.21: (0.0.6): Switch heater off at end of autotune. Usage of power settings (cbpi >= 4.0.0.45 required)
- 15.11.21: (0.0.5): Updated README 
- 02.04.21: (0.0.4): Bug fixing
- 15.03.21: Support for cbpi >= 4.0.0.33
