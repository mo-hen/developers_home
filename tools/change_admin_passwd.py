from peewee import *
from argparse import ArgumentParser
import sys;
sys.path.append('./');
from models import *

import hashlib


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--passwd', default=123456, type=int, help='change passwd for admin')
    args = parser.parse_args()
    passwd = args.passwd

    db.connect()
    passwd_hash=hashlib.sha224("{0}".format(passwd).encode('utf-8')).hexdigest()
    User.update(passwd=passwd_hash).where(User.username == "admin").execute()
    db.close()
