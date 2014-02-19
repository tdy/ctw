**NOTE:** Find the original website archived [in the Wayback Machine][1].

---

# CurseTheWeather

This is a curses application that displays the weather in a terminal. It can give
the current weather as well as forecasts for up to 10 days.

``weatherfeed.py`` is a module that it uses and it can be used by other frontends
to get the weather information. Each time it is instantiated, it grabs the
weather from [weather.com][2].

## License

Licensed under the GNU GPL version 2.0. See GPL.gz for more information.

## Installation

Installation is easy on unix systems. Untar the distribution (obviously
you've done this if you're reading this now) and then run the command:
``python setup.py install``

Done!

## Usage

To run curse the world, type ``ctw`` at the command line.  It will tell you
right away that you need to pass the ``--location`` parameter first, and it will
give you directions on how to do that.

[1]: http://web.archive.org/web/20120715025016/http://opensource.hld.ca/trac.cgi/wiki/CurseTheWeather
[2]: http://www.weather.com/
