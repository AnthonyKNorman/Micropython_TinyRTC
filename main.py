import time
from PCD8544 import PCD8544
import lcd_gfx
import network
from TinyRTC import TinyRTC

d = PCD8544()
d.reset()
d.begin()
time.sleep(5)
d.clear()
d.display()
d.p_string('The quick brown fox jumped over the lazy dog')
d.display()
time.sleep(5)
d.clear()
lcd_gfx.drawTrie(42,2,21,23,63,23,d,1)
d.display()
time.sleep(1)
lcd_gfx.drawFillRect(10,12,20,20,d,1)
d.display()
time.sleep(1)
lcd_gfx.drawCircle(70,24,10,d,1)
d.display()
time.sleep(5)
nic = network.WLAN(network.STA_IF)
ip, subnet, gateway, dns = nic.ifconfig()
d.clear()
d._row = 0
d._col = 2
d.p_string('IP Address')
d._row = 1
d._col = 0
d.p_string(ip)
d._row = 3
d._col = 3
d.p_string('Gateway')
d._row = 4
d._col = 0
d.p_string(gateway)
d.display()
d.clear()

t = TinyRTC()


def showtime(disp, tim):
	disp._row = 2
	disp._col = 3
	disp.p_string(tim.get_time_string())
	disp._row = 3
	disp._col = 2
	disp.p_string(tim.get_date_string())
	disp.display()

def runtime(disp, tim):
	lastsec = 0
	while(1):
		sec = tim._read(0)
		if(sec != lastsec):
			showtime(disp,tim)
			lastsec = sec
		time.sleep_ms(50)









