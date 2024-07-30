# This code is used to duplicate the screen, meaning it sets the same resolution for HDMI1 as HDMI0

import subprocess
import re

def get_connected_displays():
    # Run xrandr command to get connected displays
    output = subprocess.check_output(['xrandr']).decode('utf-8')
    
    # Extract connected display names using regular expression
    connected_displays = re.findall(r'^(\S+) connected', output, re.MULTILINE)
    
    return connected_displays

def main():
    # Add new mode for 1024x600
    subprocess.call(['xrandr', '--newmode', '1024x600_60.00', '48.96', '1024', '1064', '1168', '1312', '600', '601', '604', '622', '-HSync', '+Vsync'])
    
    # Get connected display names
    displays = get_connected_displays()
    
    if not displays:
        print("Error: No connected displays detected")
        return
    
    # Add the new mode to each connected display
    for display in displays:
        subprocess.call(['xrandr', '--addmode', display, '1024x600_60.00'])
        
        # Set the display to the new mode and duplicate the screen output
        subprocess.call(['xrandr', '--output', display, '--mode', '1024x600_60.00', '--same-as', displays[0]])

    print("Resolutions set to 1024x600 for all connected displays and screen output duplicated.")

if __name__ == "__main__":
    main()
