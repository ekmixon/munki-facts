'''Extract the current CrashPlan user from CrashPlan's config file'''

from __future__ import print_function


def fact():
    '''Return CrashPlan user name'''
    cp_identity_file = '/Library/Application Support/CrashPlan/.identity'
    username = ''
    try:
        with open(cp_identity_file) as identity:
            for line in identity:
                if line.startswith('username='):
                    username = line.partition('=')[2].rstrip()
                    break
    except (IOError, OSError):
        pass

    return {'crashplan_username': username}


if __name__ == '__main__':
    print(fact())
