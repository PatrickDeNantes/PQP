import machine, time
import pqp_relais as r

r.off()

def start():
	# clignotement relais
	for i in range(0,3):
		time.sleep_ms(250)
		r.on()
		time.sleep_ms(250)
		r.off()
	




