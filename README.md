# New \*niX (NUX) Binaries

This project has been in the making a long time, ever since I started writing my own Shell One-Line Idioms and throwing them in my system bin folder. This repository is a collection of those Idioms. Pull-requests are welcome, one utility per commit; I am not an expert in Shell scripting, improvements would be lovely.

## License
The contents of this repository are licensed under the [GNU GPLv3](LICENSE), and as such, as a user you have 4 basic freedoms ([See GNU's Definition of Free Software](https://www.gnu.org/philosophy/free-sw.en.html)):
* The freedom to run the program as you wish, for any purpose (freedom 0).
* The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1).
* The freedom to redistribute copies so you can help your neighbor (freedom 2).
* The freedom to distribute copies of your modified versions to others (freedom 3). By doing this you can give the whole community a chance to benefit from your changes.

Under this license, as a user you agree to the following:
* Redistribution must include the [source code](bin/) and a copy of the original [license](LICENSE)
* You may not change the license
* Any changes you make should be explicitly stated in some form for the end user

You may find out more at [choosealicense.com](http://choosealicense.com/licenses/gpl-3.0/#).

## Installation
If I get the chance at some point, it would be nice to write a generic installation script, maybe based on `rsync`, but until then, to install on any \*nix system, you are going to need to copy the binaries you want into your `$PATH`, this is a matter of personal preference, but I prefer `/bin`. In addition, if you don't have `bash` at the location of `/bin/bash`, you will need to change the shebang (`#!`) lines to point to your local `bash` or a `bash` compatible shell like `zsh`. You can find the location of any binary in your `$PATH` with the command `which`. If you are running on OSX, these scripts were designed for Linux and thus will require some modifications, `du` on OSX does not support the `-b` flag so the `-b` flag should be replaced with a `-k` flag and a `k` added at the end of the temporary `du/awk` variable. Therefore, `txz` becomes the following on OSX:
  * `tar -cf - "$1" | pv -s $(du -sk "$1" | awk '{print $1}')k | xz -9e -c - > "$1".txz && xz -tv "$1".txz`

From this on Linux:
  * `tar -cf - "$1" | pv -s $(du -sb "$1" | awk '{print $1}') | xz -9e -c - > "$1".txz && xz -tv "$1".txz`

In addition, if running a Mac, you will need to install via Homebrew, `pv` and if you want the XZ Family, `xz`.

## The XZ Family
These Idioms serve as wrappers for my favorite compressor, `XZ`, running on its highest possible setting, `-9e`, with added functionality such as `tar`ing up folders and/or adding a progress bar for those of us who are impatient.

### Tar-XZ (TXZ)

My first shell idiom was Tar-XZ, which I abbreviated to txz. It takes a folder as an argument, tars it up and in place compresses it with XZ and tests the resulting archive to ensure everything went smoothly.

#### Required Dependencies:
* `tar` (creates the filesystem image of the folder we wish to compress, conserving filesystem metadata such as permissions and should be on virtually all \*nix systems as it is a standard utility)
* `pv` (pipe-viewer lets us see progress, although this is not as accurate on faster CPUs, you should be able to find it in your package manager or Homebrew as `pv`)
* `du` (calculates the size [disk usage] of the folder we are packaging/compressing and should be on virtually all \*nix systems)
  * OSX systems ship with a different version of `du` which require slight modifications of this idiom.
* `awk` (for extracting the data we want from `du`, should be on most \*nix Systems)
* `xz` (xz is modern, heavy duty slow compression utility in the same family as 7zip and a native Rar equivalent on \*nix Systems, you should be able to find it in your package manager [most Linux systems ship `xz` by default] or Homebrew as `xz`)

#### Usage:

`$ txz folder_I_want_to_recursively_compress`

Output: `folder_I_want_to_recursively_compress.txz`

### Tar-XZ-Remove (TXZRM)

Building on the previous idiom Tar-XZ, in the interest of compressing and deleting to reclaim disk space, I built Tar-XZ-Remove or `txzrm` for short. It takes a folder as an argument, tars it up and in place compresses it with XZ, tests the compressed Tar to ensure that we can safely delete the source files for what we just compressed.

#### Required Dependencies:
* All of `txz`'s dependencies: `tar`, `pv`, `du`, `xz`, `awk`
* `rm` (for deleting files, this is a standard \*nix utility)

#### Usage:

`$ txzrm folder_I_want_to_recursively_compress`

Output: `folder_I_want_to_recursively_compress.txz` and `folder_I_want_to_recursively_compress` is deleted from the filesystem.

### Compress File with XZ (CFXZ)

Soon I realized that I was using my Tar-XZ idiom no just on folders, which I had designed it for, but also on normal files, so it was time to once again build a new idiom. This one takes a file as an argument, pipes it though pipe-viewer, compresses it with XZ and tests the resulting archive to ensure everything went smoothly.

#### Required Dependencies:
* `dd` (for reading and placing raw file data into the pipe and should be on virtually all \*nix systems as it is a standard utility)
* `pv` (pipe-viewer lets us see progress, although this is not as accurate on faster CPUs, you should be able to find it in your package manager or Homebrew as `pv`)
* `du` (calculates the size [disk usage] of the folder we are packaging/compressing and should be on virtually all \*nix systems)
  * OSX systems ship with a different version of `du` which require slight modifications of this idiom.
* `awk` (for extracting the data we want from `du`, should be on most \*nix Systems)
* `xz` (xz is modern, heavy duty slow compression utility in the same family as 7zip and a native Rar equivalent on \*nix Systems, you should be able to find it in your package manager [most Linux systems ship `xz` by default] or Homebrew as `xz`)

#### Usage:

`$ cfxz file_I_want.compressed`

Output: `file_I_want.compressed.xz`

### Compress File with XZ then Remove (CFXZRM)

Following the same line of thought behind `txzrm` and `cfxz`, once I had built the `cfxz` idiom, it made sense to build its archiving cousin `cfxzrm` who carries out the same functionality, but on a successful compression deletes the source file.

#### Required Dependencies:
* All of `cfxz`'s dependencies: `dd`, `pv`, `du`, `xz`, `awk`
* `rm` (for deleting files, this is a standard \*nix utility)

#### Usage:

`$ cfxzrm file_I_want.compressed`

Output: `file_I_want.compressed.xz` and `file_I_want.compressed` is deleted from the filesystem.

## The DD Family
`dd` is one of my favorite utilities in part because it is so versatile in what you can use it to do.

### DD with Progress Bar (ddpv)
In my community, I am considered to be everyone's local "Linux Expert", so when people do decide that they want to give Linux a try, often they come to me so that I will prepare them a live USB stick using a live hybrid iso. `dd` is classically the solution when it comes to burning a live USB and by far what I prefer to use, however, its lack of any indication of progress I found to be troubling, especially given the power and potential behind `dd`. The people I burn USB Sticks for, didn't like the lack of an indication of progress either, nor did they like the standard signal based response based on `watch`/`kill` so after giving it some thought and realizing that I was already occupying a idiom-like incantation every time I burned a USB, I decided to make it an idiom on its own, `ddpv`, the perfect union between `dd` and `pv` for showing progress whenever you decide to make a live USB stick (I imagine it could be used for other things too, like perhaps burning CDs and DVDs).

#### Required Dependencies:
* `dd` (for reading and placing raw file data into the pipe and should be on virtually all \*nix systems as it is a standard utility)
* `pv` (pipe-viewer lets us see progress, although this is not as accurate on faster CPUs, you should be able to find it in your package manager or Homebrew as `pv`)
* `du` (calculates the size [disk usage] of the folder we are packaging/compressing and should be on virtually all \*nix systems)
  * OSX systems ship with a different version of `du` which require slight modifications of this idiom.
* `awk` (for extracting the data we want from `du`, should be on most \*nix Systems)

#### Usage:

`$ ddpv source.image destination.image`

Output: `destination.image` should reflect `source.image` byte for byte

## The SU Family
Despite all the people who firmly believe that `SUDO` is superior to `SU`, it is my belief that, at the very least in my use case, personal use computing where I am the only administrator, I prefer the inherent security provided by having a separate login for my root user in addition to the additional responsibility that comes from using `SU`. All too often I have seen my peers screw up their systems because they lack a full understanding and respect for what `SUDO` does. Now perhaps they would make all the same mistakes if they used `SU`, however I think once a user comes to understand that what they are doing is escalating privileges and running as a different user, their perspective changes and they suddenly understand that they need trend more carefully. To further complicate my use case, occasionally, I share my password with others so that they may unlock my machine in the middle of presentations and the like. For this use case, I change my password to something very weak via `passwd` in confidence that they will not have root access. So perhaps `su` isn't for everyone, but `sudo` isn't either, but in my case `su` and the peace of mind that it gives me is a nice fit.

### Makepkg with SU (makepkg.su)
I am a recent convert to Archlinux as my full time system and love compiling packages out of the AUR, however upon discovering that Makepkg calls `SUDO` if it finds it on your system (I do use `sudo -iu user` for changing users, I could just as easily use `su - user`, but out of habit I use `sudo` more often to switch users and `su` always for privilege escalation), I was a bit repulsed and horrified, so I edited the script to never call `su` by modifying the condition of a single `if` statement. The original line is commented (see line 227, 228 for the modification I have made to my `Makepkg`).

#### Required Dependencies:
If Archlinux's vanilla `makepkg` works on your system, my modified version, `makepkg.su` should work as well.

Officially these dependencies are listed as:
* awk
* bsdtar (libarchive)
* bzip2
* coreutils
* fakeroot
* file
* find (findutils)
* gettext
* gpg
* grep
* gzip
* openssl
* sed
* tput (ncurses)
* xz

#### Usage:
Where I have made a minimal change to `Makepkg` in order to better serve my personal philosophy on security and the `su` vs. `sudo` debate. My typical personal usage is:

`$ makepkg.su -si`

where:

* `-s` installs dependencies that the package you are building requires.
* `-i` installs the package after you build it.

Output: AUR package installed on your system.
