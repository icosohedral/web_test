#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main(https=False):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
    try:
        from django.core.management import execute_from_command_line
    except:
        raise ImportError("Couldn't import Django.")
    script_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
    if https:
        argv = [sys.argv[0], "runserver_plus", '0.0.0.0:443', '--cert', '%sserver.crt' % script_dir, '--key', '%sserver.key' % script_dir]
    else:
        argv = [sys.argv[0], "runserver_plus", '0.0.0.0:8000']
    execute_from_command_line(argv)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(https=True)
    else:
        main()