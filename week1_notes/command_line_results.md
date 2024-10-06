# Results from working on command line

```bash
liakasn@cloud-vm:~$ mkdir src
liakasn@cloud-vm:~$ ls
src
liakasn@cloud-vm:~$ pico src/generator.py
liakasn@cloud-vm:~$ pico src/collector.py
liakasn@cloud-vm:~$ sudo python3 src/generator.py 20 /var/www/html
liakasn@cloud-vm:~$ sudo python3 src/collector.py http://34.67.73.252/data.json
server0 71
server1 47
server2 85
server3 89
server4 6
server5 7
server6 19
server7 52
server8 75
server9 67
server10 71
server11 12
server12 81
server13 60
server14 98
server15 3
server16 83
server17 28
server18 49
server19 4
{'under': 9, 'over': 11}
```