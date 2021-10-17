# bandit - overthewire

# bandit0

`ssh bandit0@bandit.labs.overthewire.org -p 2220`

The password is `boJ9jbbUNNfktd78OOpsqOltutMc3MY1`.
Use `ssh` to login.


# bandit1

`ssh bandit1@bandit.labs.overthewire.org -p 2220`

The password is `CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9`.
The filename is `-`. In linux `-` means stdin so how do you get past this?
`cat -` will cat out what you type, `cat "-"` does the same.
I did `cat < "-"`, but there are other ways too. Eg - `cat ./-`


# bandit2

`ssh bandit2@bandit.labs.overthewire.org -p 2220`

The password is `UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK`.
I did cat "spaces in this filename", you can also escape the spaces using `\`.


# bandit3

`ssh bandit3@bandit.labs.overthewire.org -p 2220`

The password is `pIwrPrtPN36QITSp3EQaw936yaFoFgAB`.
The password in a hidden file. Just use `ls -a inhere/` and `cat inhere/.hidden`.


# bandit4

`ssh bandit4@bandit.labs.overthewire.org -p 2220`

The password is `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`.
The files inside the `inhere` directory are all some binary data except for one file.
A simple cat command with some bash magic should do the job.
This is what i did `cat < $(file inhere/* | grep 'ASCII' | cut -d ':' -f1)`, you can
also use `xargs` instead of substituting.


# bandit5

`ssh bandit5@bandit.labs.overthewire.org -p 2220`

The password is `DXjZPULLxYr17uwoI01bNLQbtFemEgo7`.
Using the given hints we can use a simple `find` command to get the file.
I used this command to find the file `find -type f -size 1033c -exec grep [A-Za-z] '{}' \;`
Useful links:
1. [Find human-readable files](https://unix.stackexchange.com/questions/313442/find-human-readable-files)
2. [find: missing argument to -exec](https://stackoverflow.com/questions/2961673/find-missing-argument-to-exec)


# bandit6

`ssh bandit6@bandit.labs.overthewire.org -p 2220`

The password is `HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs`.
Again a simple find command should do the work. Do have a look at the `man` page for the `find` command.
The command I used is `find / -user bandit7 -group bandit6 -size 33c -exec cat '{}' \; 2>/dev/null`.


# bandit7

`ssh bandit7@bandit.labs.overthewire.org -p 2220`

The password is `cvX2JJa4CFALtqS87jk27qwqGhBM9plV`.
Just `grep` for 'millionth' in the `data.txt` file.
I personally used `awk`. The command is `awk '/millionth/{ print $2 }' data.txt`


# bandit8

`ssh bandit8@bandit.labs.overthewire.org -p 2220`

The password is `UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR`.
Originally I came up with this `cat data.txt | xargs -i'{}' grep -c {} data.txt | grep -n 1$ | cut -d':' -f1 | xargs -i'{}' sed -n '{}p' data.txt`,
which ofcourse is the most horrible code I've ever seen. So I googled and found this `sort data.txt | uniq -u`, should have just looked at the `man` page.


# bandit9

`ssh bandit9@bandit.labs.overthewire.org -p 2220`

The password is `truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk`.
The command I used is `strings data.txt | grep '==.*'`.
Note that it doens't return the exact password, instead it returns a few lines and you can find the password from them easily.


# bandit10

`ssh bandit10@bandit.labs.overthewire.org -p 2220`

The password is `IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR`.
A simple `base64` command. The command is `base64 -d data.txt`.


# bandit11

`ssh bandit11@bandit.labs.overthewire.org -p 2220`

The password is `5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu`.
If you have some background in cryptography you should have immediately found that this is a [`Caesar cipher`](https://en.wikipedia.org/wiki/Caesar_cipher) and
`ROT13` is a special case of `Caesar cipher`. I could have wrote a simple python program to crack this, but I wanted
a shell command, so ofcourse I googled and found [https://stackoverflow.com/questions/5442436/using-rot13-and-tr-command-for-having-an-encrypted-email-address](this).
The command I used is `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`.
I don't know man `ROT13` algorithm in a single line of shell script is seriously amazing.


# bandit12

`ssh bandit12@bandit.labs.overthewire.org -p 2220`

The password is `8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL`.
Man that was exhaustive. The file was repeatedly compressed using `tar`, `gzip` and `bzip2`. Every time I had
to run the `file` command to see what kind of file it is. You uncompress the file around 10 or so times until
you get an ASCII file which contains the password.


# bandit13

`ssh bandit13@bandit.labs.overthewire.org -p 2220`

The password is `4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e`.
A simple `ssh` command should do the job. The target is to find how to specify the private key file that is given.
You can do that using the `-i` option. The command is `ssh -i sshkey.private bandit14@localhost`, and you `cat` out
`/etc/bandit_pass/bandit14`.


# bandit14

`ssh bandit14@bandit.labs.overthewire.org -p 2220`

The password is `BfMYroe26WYalil77FoDi9qh59eK5xNr`.
I had no idea on how to go about this level, probably because I have never used `telnet` and so I googled
and found that telnet can be used as a text oriented communication thingy.
The commmand is `telnet localhost 30000`.


# bandit15

`ssh bandit15@bandit.labs.overthewire.org -p 2220`

The password is `cluFn7wTiGryunymYOu4RcffSxQluehd`.
The same goes for this level, I had no idea on what to do. Googled for hints, found that I should be using
`openssl s_client`, read the `man` page and used the command `openssl s_client -connect localhost:30001` to
connect to the localhost using SSL encryption.


# bandit16

`ssh bandit16@bandit.labs.overthewire.org -p 2220`

The password is `xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn`.
You scan all the open ports in the range of 31000 to 32000 on the `localhost` using the command
`nmap -sV localhost -p 31000-32000`. It returns a list of ports and 2 of them run on SSL encryption.
Port `31518` runs a `echo` service while port `31790` runs an unknown service, so obviously I chose
the port `31790` and ran the command `openssl s_client -connect localhost:31790` and then pasted the password
of this level. It in turn printed out a ssh private key, I redirected the output to `/tmp/private.key` and then
ran `ssh -i /tmp/private.key bandit17@localhost` and it said `WARNING: UNPROTECTED PRIVATE KEY FILE!` and that the
permissions for that file is too open. So I changed the permissions to `600` using `chmod 600 /tmp/private.key` and
then ran the ssh command again, now it worked. After getting into the localhost as bandit17, I catted out
`/etc/bandit_pass/bandit17`.


# bandit17

`ssh bandit17@bandit.labs.overthewire.org -p 2220`

The password is `kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd`.
If you have ever worked with `git` or patched files before then this would be easy.
A simple `diff` command would do the work. I personally used the command `diff -u passwords.old passwords.new`.


# bandit18

`ssh bandit18@bandit.labs.overthewire.org -p 2220`

The password is `IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x`.
Logged into the server, got logged out automatically, had no idea what to do, read the `man` page of `ssh`, found out about `-T` option, ran the command
`ssh bandit18@bandit.labs.overthewire.org -p 2220 -T`, was getting a blank screen(as expected but didn't know what to do next).
Googled 'ssh with no tty', found that you can run commands, ran the command `ssh bandit18@bandit.labs.overthewire.org -p 2220 -T "cat ~/readme`.
Another way to do this is `ssh bandit18@bandit.labs.overthewire.org "bash --norc"` and then cat out the file.


# bandit19

`ssh bandit19@bandit.labs.overthewire.org -p 2220`

The password is `GbKksEFF4yrVs6il55v6gwY5aVje5f0j`.
Executed the binary as instructed, didn't read the output correctly, only saw `Example: ./bandit20-do id`.
Didn't exactly know what the binary does, ran `./bandit20-do /etc/bandit_pass/bandit20`, which returned with an
error. Ran `strace` on the binary with the same argument, found that the arguments are passed to `/usr/bin/env`
as it is, came up with an `bash injection` attack and ran the command `./bandit20-do cat /etc/bandit_pass/bandit20`,
got the password, scrolled up and found the line `Run a command as another user`, felt dumb.


# bandit20

`ssh bandit20@bandit.labs.overthewire.org -p 2220`

The password is `gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr`.
Don't know bro.


# bandit21

`ssh bandit21@bandit.labs.overthewire.org -p 2220`

The password is `Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI`.
Cat out whats in the bandit22 cron file and you find that it runs a script `cronjob_bandit22.sh` every minute.
Cat out `cronjob_bandit22.sh` and you find that it's saving the password to a file in `/tmp` directory.
Cat that file out and you have the password.


# bandit22

`ssh bandit22@bandit.labs.overthewire.org -p 2220`

The password is `jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n`.
A simple level to read and understand shell script.
Command I ran `echo I am user bandit23 | md5sum | cut -d ' ' -f1 | xargs -i'{}' cat /tmp/{}`


# bandit23

`ssh bandit23@bandit.labs.overthewire.org -p 2220`

The password is `UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ`.
You can place your own scripts inside `/var/spool/bandit24` thats the take. Since the script is run by
`bandit24` you can cat out the password from `/etc/bandit_pass/bandit24` to another file. The only line
in the `bandit23.sh` script is `cat /etc/bandit_pass/bandit24 > /tmp/bandit_pass` with a shebang. For that the
script should have executable permissions, so you change the permissions using `chmod 777 /tmp/bandit23.sh`.
You then copy the script to `/var/spool/bandit24`.


# bandit24

`ssh bandit24@bandit.labs.overthewire.org -p 2220`

The password is `uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG`.
I originally did `echo $pass $i | nc localhost 30002 >> /tmp/bandit/result` but that was too slow.
Searched google found similar results that were slow. From level 20 I remembered that you read a file
as input. So I camp up with the following code and then ran the command `nc localhost 30002 < /tmp/bandit/result > temp.res`
and then ran `uniq -u temp.res`. The whole thing only took about 5 seconds.

```bash
#!/bin/bash
  
pass="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for i in {9999..0000}; do
    echo $pass $i >> /tmp/bandit/result
done;

```


# bandit25

`ssh bandit25@bandit.labs.overthewire.org -p 2220`

The password is `5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z`.
I was completely lost in this level because `more` was not working for me.
Turns out `more` only works like a pager when the screen size is less the content in it.
Resized the screen and then opened vim by pressing `v` and then read the file
`/etc/bandit_pass/bandit26`.


# bandit26

`ssh bandit26@bandit.labs.overthewire.org -p 2220`

The password is `3ba3118a22e93127a4ed485be72ef5ea`.
Did the same thing and instead of reading from a file, I used `!` to execute shell commands.
First I found that there is a `bandit27-do` file using `ls` and then executed the same using
`!./bandit27-do cat /etc/bandit_pass/bandit27`. Googled afterwards and found that there is a better
way to do this, I could have just executed `!/bin/bash` to get a shell. I am just dumb.


# bandit27

`ssh bandit27@bandit.labs.overthewire.org -p 2220`

The password is `0ef186ac70e04ea33b4c1853d2526fa2`.
A simple `git clone` to the specified repo path would give you the password.


# bandit28

`ssh bandit28@bandit.labs.overthewire.org -p 2220`

The password is `bbc96594b4e001778eee9975372716b2`.
Again a simple `git clone` command just like the last level but there is already a folder named repo
so you have to give it a directory path. The command is
`git clone ssh://bandit28-git@localhost/home/bandit28-git/repo bandit-repo` and then `cd` into the folder
using the command `cd bandit-repo`. Catting out the `README.md` file only gives a placeholder password.
So I quickly did a `git log` and fair enough there is commit that replaces the original password with
this placeholder. Then I did `git checkout <commit-id>` and then catted out the file to get the password.
All this should be easy if you have ever worked with `git` before because these are the basics of `git`.


# bandit29

`ssh bandit29@bandit.labs.overthewire.org -p 2220`

The password is `5b90576bedb2cc04c86a9e924ce42faf`.
Cloning the repo and taking a look at the log didn't give away anything. After trying 2 more commands
I thought maybe there is another branch and then did `git branch` which only listed `master`. Didn't know what
to do, so googled and found that there were remote branches(sad that it didn't strike me that there could be
remote branches). I then did `git branch -a` to list all branches and checked out to the `remotes/origin/dev`
branch and found the password.


# bandit30

`ssh bandit30@bandit.labs.overthewire.org -p 2220`

The password is `47e603bb428404d265f59c42920d81e5`.
Seriously had no idea what to do after exploring all the basic stuff. Turns out that there are something
called as `git tags`. So got the password using `git tag -l` and then `git show secret`. Note that `secret`
is the name of the tag.


# bandit31

`ssh bandit31@bandit.labs.overthewire.org -p 2220`

The password is `56a9bf19c63d650ce78e6ec0354ee45e`.
Just create a file `key.txt` with the specified content, delete `.gitignore` and then commit and push it
origin on branch `master`. You get the password.


# bandit32

`ssh bandit32@bandit.labs.overthewire.org -p 2220`

The password is `c9c3199ddf4121b10cf581a98d51caee`.
Honestly didn't know what to do. If you are familiar with linux you might know that `$0` gets you the
shell name just like how a `C` program gets you the program's name. I knew about this but didn't know
that it can be used to exploit this, lol. Execute `bash` using `$0` and then `cat` out the content
of the file `/etc/bandit_pass/bandit33`.
