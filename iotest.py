import io
import time

try:
    sp1 = io.Spike(1)
    sp2 = io.Spike(2)
    sp3 = io.Spike(3)
    sp4 = io.Spike(4)
    sw1 = io.Switch(1)
    sw2 = io.Switch(2)
    sw3 = io.Switch(3)
    sw4 = io.Switch(4)
    sw5 = io.Switch(5)
    sw6 = io.Switch(6)

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
    io.close()
    raise

finally:
# Release IO lines
    io.close()
