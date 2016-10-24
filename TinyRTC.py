from machine import Pin, I2C
class TinyRTC():
	def __init__(self):
		self._addr = 0x68
		# construct an I2C bus
		self._i2c = I2C(scl=Pin(2), sda=Pin(16), freq=100000)

	def _write(self, reg, value):
		self._i2c.writeto_mem(self._addr, reg, bytearray([value]))
		
	def _read(self, reg):
		return self._i2c.readfrom_mem(self._addr, reg, 1)[0]

	def bcd_bin(self, bcd):
		byt = bcd & 0x0f
		byt = byt + ((bcd>>4)*10)
		return byt

	def bin_bcd(self, byt):
		bcd = byt % 10
		bcd = bcd + (int(byt/10)<<4)
		return bcd
		
	def byte_string(self, byt):
		strng = str(byt)
		if (len(strng)<2):
			strng = '0' + strng
		return strng

	def get_time_string(self):
		tim = self.byte_string(self.bcd_bin(self._read(2) & 0x3f))
		tim += ':'
		tim += self.byte_string(self.bcd_bin(self._read(1)))
		tim += ':'
		tim += self.byte_string(self.bcd_bin(self._read(0)))
		return tim
		
	def get_date_string(self):
		tim = self.byte_string(self.bcd_bin(self._read(4)))
		tim += '/'
		tim += self.byte_string(self.bcd_bin(self._read(5)))
		tim += '/20'
		tim += self.byte_string(self.bcd_bin(self._read(6)))
		return tim
		
	def set_time(self, ss, mm, hh, dow, dd, MM, yy):
		self._write(0, self.bin_bcd(ss))
		self._write(1, self.bin_bcd(mm))
		self._write(2, self.bin_bcd(hh))
		self._write(3, self.bin_bcd(dow))
		self._write(4, self.bin_bcd(dd))
		self._write(5, self.bin_bcd(MM))
		self._write(6, self.bin_bcd(yy))
