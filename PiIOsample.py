import PiIO
import time

try:
    winch = PiIO.Spike(1)
    upperLimit = PiIO.Switch(1)
    lowerLimit = PiIO.Switch(2)

    winch.stop()
    time.sleep(1)
    winch.fwd()
    time.sleep(1)
    winch.rev()
    time.sleep(1)

    # Run winch to upper limit
    while upperLimit.open():
        winch.fwd()
    winch.stop()
    time.sleep(1)
    
    # Run winch to lower limit
    while lowerLimit.open():
        winch.rev()
    winch.stop()
    
except:
    PiIO.close()
    raise

finally:
# Release IO lines
    PiIO.close()
