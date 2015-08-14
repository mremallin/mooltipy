#!/usr/bin/env python
"""A command line utility for administrating the mooltipass.

"""

from optparse import OptionParser
import time

from mooltipy import Mooltipass

def main_options():
    """Handles command-line interface, arguments & options. """

    usage = 'Usage: %prog {context} [OPTIONS]\n' + \
            'Example: %prog Lycos.com --login=jsmith --password="not_random"'

    parser = OptionParser(usage)
    parser.add_option('--login', dest='login', metavar='USER',
            help='login for context')
    parser.add_option('--password', dest='password', metavar='PASS',
            help='password for login')

    (options, args) = parser.parse_args()

    if not len(args) == 1:
        parser.error('Incorrect number of arguments; see --help.')

    return (options, args)

if __name__ == '__main__':

    (options, args) = main_options()

    mooltipass = Mooltipass()
    quiet_bool = False
    while mooltipass.get_status() != 5:
        if not quiet_bool:
            print('Insert a card and unlock the Mooltipass...')
        quiet_bool = True
        time.sleep(2)

    while not mooltipass.set_context(args[0]):
        mooltipass.add_context(args[0])

    mooltipass.set_login(options.login)
    mooltipass.set_password(options.password)

    #TODO: theres a lot left to be desired here
