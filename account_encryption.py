#!/usr/bin/env python
import os
import hashlib

def encryption(password):
    hash_md5 = hashlib.md5(password)
    return hash_md5.hexdigest()

def check_user_exists(username):
    all_username = []
    f = open('account.txt', 'r')
    for user_info in f.readlines():
        user = user_info.split()[0]
        all_username.append(user)
#    print username, username in all_username
    if username in all_username:
        print 'the %s already exists' % username
        exit(0)

def regist():
    pass

def login():
    pass

def test():
    pwd = 'nihao123'
    pwd_md5 = encryption(pwd)
    print pwd_md5
    

def main():
    username = raw_input('please input your users:')
    password = raw_input('please input your password:')
    check_user_exists(username)
    if len(password) == 0:
        exit(1)
#    print 'jiamipassword'
    encryption_password = encryption(password)
    account_info ={
        'name': username,
        'password': encryption_password,
    }
#    print account_info
    cunru_str = '%s %s \n' % (account_info['name'], account_info['password'])
#    print cunru_str
    f = open('account.txt', 'a')
    f.write(cunru_str)
    f.close()
    print 'The %s has registered successfully!' % account_info['name']

if __name__ == '__main__':
    main()    
