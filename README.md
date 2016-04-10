# New \*niX (NUX) Binaries

This project has been in the making a long time, ever since I started writing my own Shell One-Line Idioms and throwing them in my system bin folder. This repository is a collection of those Idioms. Pull-requests are welcome, one utility per commit; I am not an expert in Shell scripting, improvements would be lovely.

## Tar-XZ (TXZ)

My first shell idiom was Tar-XZ, which I abbreviated to txz. It takes a folder as an argument, tars it up and in place compresses it with XZ and tests the resulting archive to ensure everything went smoothly.

### Required Dependencies:
* `tar` (creates the filesystem image of the folder we wish to compress, conserving filesystem metadata such as permissions and should be on virtually all \*nix systems as it is a standard utility)
* `pv` (pipe-viewer lets us see progress, although this is not as accurate on faster CPUs, you should be able to find it in your package manager or Homebrew as `pv`)
* `du` (calculates the size [disk usage] of the folder we are packaging/compressing and should be on virtually all \*nix systems)
  * OSX systems ship with a different version of `du` which require slight modifications of this idiom.
* `xz` (xz is modern, heavy duty slow compression utility in the same family as 7zip and a native Rar equivalent on \*nix Systems, you should be able to find it in your package manager [most Linux systems ship `xz` by default] or Homebrew as `xz`)

### Usage:

`$ txz folder_I_want_to_recursively_compress`

Output in: `folder_I_want_to_recursively_compress.txz`

## Tar-XZ-Remove (TXZRM)

Building on the previous idiom Tar-XZ, in the interest of compressing and deleting to reclaim disk space, I built Tar-XZ-Remove or `txzrm` for short. It takes a folder as an argument, tars it up and in place compresses it with XZ, tests the compressed Tar to ensure that we can safely delete the source files for what we just compressed.

### Required Dependencies:
* All of `txz`'s dependencies: `tar`, `pv`, `du`, `xz`
* `rm` (for deleting files, this is a standard \*nix utility)

### Usage:

`$ txzrm folder_I_want_to_recursively_compress`

Output in: `folder_I_want_to_recursively_compress.txz` and `folder_I_want_to_recursively_compress` is deleted from the filesystem.
