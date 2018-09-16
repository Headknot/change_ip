# change_ip

change_ip is a tool for changing network adapter IP, Mask & Gateway in a Windows environment.
The need came out of the minor annoyance of clicking through "change adapter options" every time you need to change IP.
If you find yourself doing this a lot because of work f.ex, then this might save you a bit of time.

The GUI was made with QT/Pyside2 and the actual changing of IP is done via netsh commands in the backend.
I have uploaded an .exe of the software in the repo, but please remember to start it as administrator, or you will not have sufficient permission to change parameters via netsh.

See example screenshot below:

![Example screenshot](https://github.com/Headknot/change_ip/blob/master/screenshots/change_ip.PNG)

* "Clear" - clears all of your fields
* "Set Config" - Runs the commands that changes your chosen network adapters IP/Mask/GW to what you have chosen.
* "Show Current Config" - Prints current adapter IP
* "Quit" - Exits the software
