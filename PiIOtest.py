import PiIO
import time

try:
    sp1 = PiIO.Spike(1)
    sp2 = PiIO.Spike(2)
    sp3 = PiIO.Spike(3)
    sp4 = PiIO.Spike(4)
    sw1 = PiIO.Switch(1)
    sw2 = PiIO.Switch(2)
    sw3 = PiIO.Switch(3)
    sw4 = PiIO.Switch(4)
    sw5 = PiIO.Switch(5)
    sw6 = PiIO.Switch(6)

    cycle = 0  #0=stop, 1=fwd, 2=rev
    
    while sw6.open():
	if cycle == 0:
	    sp1.stop()
	    sp2.stop()
            sp3.stop()
            sp4.stop()
            cycle = 1
        elif cycle == 1:
            sp1.fwd()
            sp2.fwd()
            sp3.fwd()
            sp4.fwd()
            cycle = 2
        else:
            sp1.rev()
            sp2.rev()
            sp3.rev()
            sp4.rev()
            cycle = 0
        
        print sw1.closed(),sw2.closed(),sw3.closed(),sw4.closed(),sw5.closed(),sw6.closed()
        
        time.sleep(.5)
    

except:
    PiIO.close()
    raise

finally:
# Release IO lines
    PiIO.close()
