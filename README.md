# plugin.video.CecOnMaker

All this really does is listen on Kodi for something playing and then activates the HDMI CEC source if true.

## Use case

Mainly this is useful for turning on the TV and AVR from the Kodi remote app. You select the thing you want to watch or listen to and the TV and/or AVR turns on automatically.

## Annoyances
#You can't check to see if the CEC source has been activated already so we just keep sending the activation constantly.
#Because of the above annoyance if you start playing a video or song you'll miss a couple of seconds waiting for the CEC source to activate.
#This affects being able to stop playback when the TV has been put on standby
