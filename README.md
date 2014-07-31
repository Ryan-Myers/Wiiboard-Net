# Wiiboard Net

## A Wii balance board weight reporter

A complete system for utilizing the Wii Balance board to track your weight over time. 
It logs all information to a database and enables a minimal web front end to show
the history over time.

## Requirements

This project was built with a Raspberry Pi in mind, so the requirements assume a base Raspbian image.

`# apt-get install bluez bluez-utils python-bluez python-bottle`

As of 2014-07-30 Raspbian uses BlueZ 4.99 by default, and this is a requirement.  
BlueZ 5+ changes the DBus API in incompatible ways.

## Setup

First determine balance boards MAC address and sync the balance board with the computer through bluetooth.  
This is most easily achieved with `./xwiibind.sh 00:26:59:6B:AE:A3` and following the on screen prompts.

Next, create the database with `./create-db.py`

Then add `wiiboard-connect.py` and `webhost.py` to you startup scripts and reboot.

## Usage

Once the setup is complete and the computer rebooted, you can now simply use the front button on the balance board
to connect. Once the front LED stops flashing it's connected, and you will see it pulse once more to let you know you
can step on to be weighed. Wait a couple of seconds and step off and the balance board will turn itself off.
  
When you want to view the data visit the URL you setup earlier (`http://localhost:8080/` by default).  

`gr8w8upd8m8` uses the `bluez-test-device` utility of `bluez-utils` to disconnect the board at the end, which causes
the board to shut off. Pairing it with the OS will allow you to use the front button to reconnect to it and run the
script.

Calculating the final weight is done by calculating the mode of all the event data, rounded to one decimal digit.

## Credits

This software is made possible due in great part to the following people and projects.  
[Stavros Korokithakis](http://www.stavros.io/) - [GitHub profile](https://github.com/skorokithakis) - [Inspiring post](http://www.stavros.io/posts/your-weight-online/)  
[wiiboard-simple](https://code.google.com/p/wiiboard-simple/) for the basis of the gr8w8upd8m8.py script.  
[xwiimote](https://github.com/dvdhrm/xwiimote) for the xwiibind.sh script to pair the balance board permanently.  
[Highstock](http://www.highcharts.com/) for the web graph.

## License

This software is made available under the [Lesser GPL license](http://www.gnu.org/licenses/lgpl.html).
