#!/usr/bin/env python
# Copyright 2004 Dan Cardamore <dan@hld.ca>

from distutils.core import setup

setup(name="CurseTheWeather",
		version="0.6",
		description="Weather feed backend and ncurses front end for current and forecast weather",
		author="Dan Cardamore",
		author_email="dan@hld.ca",
		url="http://opensource.hld.ca/trac.cgi/wiki/CurseTheWeather",
		py_modules = ['weatherfeed'],
		scripts= ['ctw'])
