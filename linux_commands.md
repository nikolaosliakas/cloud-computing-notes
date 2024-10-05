# Linux Commands

## Description
Linux operating system shell has a set of commands. 
Cloud Computing teaches these and below are some used ones.


## Table of Contents

## Account Management

```commandline
liakasn@cloud-vm:~$ sudo adduser bolano
```
`liakasn` - before the @ character denotes the user executing the command
<br> `sudo` - executable superuser do or substitute user do - run as a superuser without needed to change user permissions
<br> `adduser` - command for adding users

- `pwd` → Shows the directory path
- `ls` → Lists files and folders
- `cd testfolder` → Navigates to the testfolder
- cd .. → Navigates up one directory level
- `mkdir` → Creates a new directory
- `pico` → Unix editor (we need to save and exit using a combination of keys)
- `cp a.txt b.txt` → Create a copy of file a.txt to a new file b.txt
- `rm a.txt` → Deletes the a.txt file

- `cp -r folder_A folder_B` → Creates a copy of a folder `folder_A` and its contents to a new folder `folder_B`
- `rm -rf` → Forces deletion of a folder recursively
- `cat afile.txt` → Reads file sequentially in the standard output


- `sudo` _command_ → Runs a command as a superuser

- `adduser frodo` → Creates a new user `frodo``
- `usermod -aG sudo frodo` → Makes `frodo` a superuser
- `su - frodo` → Switch between users, by navigating into their home directory
- `passwd frodo` → Change `frodo`'s password.
- `userdel frodo` → Deletes `frodo`, but not `frodo`'s home directory
