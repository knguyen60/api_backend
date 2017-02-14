[uWSGI] getting INI configuration from api_backend.ini
open("./python27_plugin.so"): No such file or directory [core/utils.c line 3684]
!!! UNABLE to load uWSGI plugin: ./python27_plugin.so: cannot open shared object file: No such file or directory !!!
*** Starting uWSGI 2.0.14 (64bit) on [Thu Feb  9 15:53:59 2017] ***
compiled with version: 4.8.3 20140911 (Red Hat 4.8.3-9) on 08 February 2017 21:30:42
os: Linux-4.4.23-31.54.amzn1.x86_64 #1 SMP Tue Oct 18 22:02:09 UTC 2016
nodename: ip-172-31-54-224
machine: x86_64
clock source: unix
detected number of CPU cores: 1
current working directory: /home/ec2-user/api_backend
detected binary path: /usr/local/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
chdir() to /home/ec2-user/api_backend
your processes number limit is 3896
your memory page size is 4096 bytes
detected max file descriptor number: 1024
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uwsgi socket 0 bound to UNIX address /home/ec2-user/api_backend/sapi_backend.sock fd 3
Python version: 3.5.1 (default, Sep 13 2016, 18:48:37)  [GCC 4.8.3 20140911 (Red Hat 4.8.3-9)]
Set PythonHome to /home/ec2-user/.virtualenvs/apiApp
Fatal Python error: Py_Initialize: Unable to get the locale encoding
ImportError: No module named 'encodings'

Current thread 0x00007f63f3300800 (most recent call first):
