'''
    Spirit Animal: generousIbex
    Date:          19/10/16
    Challenge #:   4.5
    Sources:
            - Dr. Jones Lecture
'''



import string, random
from subprocess import Popen
import subprocess
import time

# Returns a random char in the letters and numbers
def rand_char():
    return random.choice(string.ascii_letters + string.digits)
# Returns a string with an added random char at a random position
def new_pass(passw):
    t = passw
    rand = random.randint(0,7)
    t = t[:rand] + rand_char() + t[rand+1:]
    return t

#Set up parameters to intiallize loop
url = 'http://www.cs.olemiss.edu/~jones/csci343/pwd/index.php?username=generousIbex&password='
passw = 'abcdefgh'
mini = 0
count = 0
out = ''
#Generates new password, test if a better result and adjust accordingly
while out != 'SUCCESSFUL':
    temp = new_pass(passw)
    u = url + temp
    args = ['wget', '-O', '-', u]
    output = Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = output.communicate()[0]
    if out != 'SUCCESSFUL' and int(out[0:-2]) > mini:
        mini = int(out[0:-2])
        passw = temp
        print 'Attempt: {}, Value: {} and Passw: {}'.format(count, mini, passw)
    count += 1

print 'We made it, password: {} and times {}'.format(temp, count)
