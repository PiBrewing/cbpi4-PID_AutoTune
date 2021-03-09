# CraftBeerPi4 Kettle Logic for PID Auto Tune

- Initial Version which is based on the CraftbeerPi3 Plugin from IndyJoeA (https://github.com/IndyJoeA/cbpi_PIDAutoTune)
	- The purpose of this plugin is to autotune your System and determine automatically P, I and D values to optimize the heating for your system.
	- The derived values have to be entered later in your PID Kettle Logic.
	- For more info on PID and autotuning, you can check out the following articles:
    - (https://github.com/Manuel83/craftbeerpi/wiki/Autotune-PID)
    - (https://github.com/Manuel83/craftbeerpi/wiki/Manual-PID-adjustment)


- Installation:
	- pip install cbpi4-PID-AutoTune (Alternativeley you can clone it from the GIT Repo)
	- cbpi add cbpi4-PID_AutoTune
	
	- cbpi >= 4.0.0.31 is required
	
- Parameters:	
	- Output Step: Defines the output power in % used for steps to ramp up to a temperature. Default is 100%.
	- Max Outpuz: Defines the maximum outpout power in % you are using with your system. Default is 100%.
	- Lockback Seconds: Defines the time in seconds how far the routine is locking back to identify temperature peaks. 30 seconds is typical.
	
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
	- Start the automatic Kettle Logic and have a beer as it'll take sme thime. The system will heat up to the setpioint and overshoots intentionally.
	- If you are having a pump in your system or other agitators that may impact the heating cycle, you should run them also during the Autotune process
	- It is waiting until the temp is going down 0.5C below the target value.
	- Then it is repeating this procedure several times.
	- While running, it is writing a log file into the logs directory -> autotune.log
	- If successfull, the P, I and D values are listed in the log file and a message is displayed in the dashboard. 
	- You can copy this message and enter the values then afterwards into your real Kettle Logic you are using for the mashing.
	
![PIDAutoTune Results](https://github.com/avollkopf/cbpi4-PID_AutoTune/blob/main/AutoTune.png?raw=true)	
	

