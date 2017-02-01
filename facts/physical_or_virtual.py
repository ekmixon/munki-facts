#!/usr/bin/python
import plistlib
import subprocess


def fact():
    '''Return the machine type: physical, vmware, parallels or Unknown'''
    try:
        proc = subprocess.Popen(['/usr/sbin/system_profiler', '-xml',
                                 'SPEthernetDataType', 'SPHardwareDataType'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()
        plist = plistlib.readPlistFromString(output)
        name = plist[0]['_items'][0]['_name']
        if name == 'iBridge':
            stdout = 'physical'
        else:
            br_version = plist[1]['_items'][0]['boot_rom_version']
            ethernet_vid = plist[0]['_items'][0]['spethernet_vendor-id']
            if 'VMW' in br_version:
                stdout = 'vmware'
            elif '0x1ab8' in ethernet_vid:
                stdout = 'parallels'
            else:
                stdout = 'physical'

    except (IOError, KeyError, OSError):
        stdout = 'Unknown'

    return {'physical_or_virtual': stdout.strip()}


if __name__ == '__main__':
    print fact()
