__author__ = 'wblack'

import subprocess

subnetBlock = "7"

for i in range(0,256):
    cleanSubnet = subprocess.check_output("host 137.164." + subnetBlock + "." + str(i) +
                                          " | awk '{print $5}'", shell=True)
    print "137.164." + subnetBlock + "." + str(i) + " : " + cleanSubnet