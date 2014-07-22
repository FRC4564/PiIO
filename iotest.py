import io
import time

try:
    winch = io.Spike(1)
    upperLimit = io.Switch(6)
    lowerLimit = io.Switch(5)

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
    io.close()
    raise

finally:
# Release IO lines
    io.close()
