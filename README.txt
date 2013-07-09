# Licensed under the GNU GPL version 2.0
# See GPL.gz in source distribution for more information

Overview:
---------

CurseTheWeather is a curses application which displays the weather in a
terminal.  It can give the current weather as well as forecast weather for up
to 10 days.

weatherfeed.py is a module that it uses and it can be used by other frontends
to get the weeather information.  Each time it is instantiated, it grabs the
weather from weather.com.

Installation:
--------------
Installation is easy on unix systems.  Untar the distribution (obviously
you're done this if you're reading this now) and then run the command:
python setup.py install

Done!

Usage:
------
To run curse the world, type "ctw" at the command line.  It will tell you
right away that you need to pass the --location parameter first and it will
give you directions on how to do that.

The application's original website (currently down):
	http://opensource.hld.ca/trac.cgi/wiki/CurseTheWeather
