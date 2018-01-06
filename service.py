import time
import xbmc
 
if __name__ == '__main__':
    monitor = xbmc.Monitor()
 
    while not monitor.abortRequested():
        if xbmc.Player().isPlaying():
            xbmc.executebuiltin("CECActivateSource")
            # probably not a good idea to costantly execute so...
	    time.sleep(120)
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break
