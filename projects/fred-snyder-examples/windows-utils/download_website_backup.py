"""
Description
Backup website script

Run this script using pythonw.exe instead of python.exe so that it runs in the background,
pass the path to this script as the argument.
"""

from subprocess import call

# login variables
host = "fredsnyder.net"
port = "22"
login = "XXXXXXXX"
password = "XXXXXXXXXXXXXXXX"

# paths
psftp = "D:\\programs\\_backup\\_bin\\psftp.exe"
script_path = "D:\\programs\\_backup\\fredsnyder.net\\fredsnyder.net_download_psftp_script"
pscp = "D:\\programs\\_backup\\_bin\\pscp.exe"
pscp_source = "/home/fred/custom_backups/*.tar.gz"
pscp_target = "D:\\files\\backup\\backup_fredsnyder.net"


print("pscp starts here")
print("====================")
# http://the.earth.li/~sgtatham/putty/0.60/htmldoc/Chapter5.html
#
# -batch: disable all interactive prompts
# -sftp: force SSH FTP protocol
# -r: copy directories recursively
# -p: preserve file attributes
# -P" connect to specified port
# -pw: login with specified password
#
# combine variables
pscp_command = pscp + " -batch -sftp -r -C -p -P " + port + " -pw " + password + " " + login + "@" + host + ":" + pscp_source + " " + pscp_target

# execute command
call(pscp_command, shell=True)

# If this script give an certificate error, open an prompt and connect to server using psftp
# psftp -P 22 mail@fredsnyder.net
# save certificate
# input password
# exit

# delete downloaded files
print("psftp starts here")
print("====================")
psftp_command = [psftp, "-batch", "-b", script_path, "-P", port, "-pw", password, login+"@"+host]
call(psftp_command)

# command to remove download files which are older than 7 days
print("forfiles starts here")
print("====================")
forfiles_remove = 'forfiles /P ' + pscp_target + ' /M *.tar.gz /D -8 /C "cmd /c del @path"'

# execute the forfiles_remove command
call(forfiles_remove, shell=True)
