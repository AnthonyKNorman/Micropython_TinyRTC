A simple library to read from, and write to, the cheap RTC modules you see on ebay
It defaults to using pin 2 for scl and pin 16 for sda, but you can easily change these

Note: With the module that I used, there a two SMD resistors pulling up scl and sda to +5v.
You need to remove these and use pullups to 3v3 with the ESP8266. On my module they are R2 and R3. 

The main features are:

**TinyRTC.get_time_string()**

returns the time as a formatted 'hh:mm:ss' string


**TinyRTC.get_date_string()**

retruns the date as a formatted 'dd/mm/yyyy' string


**TinyRTC.set_time(ss, mm, hh, dow, dd, MM, yy)**

set the clock. After power up the clock will not run until this is executed

I have included a **main.py** that will show the time and date on a Nokia 5110 using my library

