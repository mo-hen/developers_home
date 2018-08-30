import hashlib
passwd="123456"
passwd_hash=hashlib.sha224("{0}".format(passwd).encode('utf-8')).hexdigest()
print (passwd_hash)
