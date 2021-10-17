# leviathan0

`ssh leviathan0@leviathan.labs.overthewire.org -p 2223`

The password for leviathan1 is `rioGegei8m`.
The password was in a `bookmarks.html` file inside the `.backup` directory.
A simple grep for `password` on the file gave the password away.


# leviathan1

`ssh leviathan1@leviathan.labs.overthewire.org -p 2223`

The password for leviathan2 is `ougahZi8Ta`.
There is `check` binary file which asks me for a password.
`strings` didin't work, so I used `ltrace` and that gave away the password.


# leviathan2

`ssh leviathan2@leviathan.labs.overthewire.org -p 2223`

The password for leviathan3 is `Ahdiemoo1j`.
A little confusing will write up on this later.


# leviathan3

`ssh leviathan3@leviathan.labs.overthewire.org -p 2223`

The password for leviathan3 is `vuH0coox6m`.
Run `ltrace` on the file `level3` with a random argument. You find that it
compares the argument to a string `snlprintf`. Pass it as the argument.
That's it.


# leviathan3

`ssh leviathan4@leviathan.labs.overthewire.org -p 2223`

The password for leviathan3 is `Tith4cokei`.
Run the file, prints a binary text, convert it to ASCII. Done.

# leviathan 5

`ssh leviathan5@leviathan.labs.overthewire.org -p 2223`

The password for leviathan3 is `UgaoFee4li`.
Create a symbolic link to the `/etc/leviathan_pass/leviathan6` file.


# leviathan 6

`ssh leviathan5@leviathan.labs.overthewire.org -p 2223`

The password for leviathan3 is `ahy7MaeBo9`.
Brute force the password using this code.
```bash
for i in {0000..9999};
    do echo $i; ./leviathan6 $i;
done;
```
