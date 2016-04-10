# New \*niX (NUX) Binaries

This project has been in the making a long time, ever since I started writing my own Shell One-Line Idioms and throwing them in my system bin folder. This repository is a collection of those Idioms. Pull-requests are welcome, one utility per commit; I am not an expert in Shell scripting, improvements would be lovely.

## Tar-XZ (TXZ)

My first shell idiom was Tar-XZ, which I abriviated to txz. It takes a folder as an argument, tars it up and in place compresses it with XZ.

### Required Dependencies:
* `tar` (creates the filesystem image of the folder we wish to compress, conserving filesystem metadata such as permisions and should be on virtually all \*nix systems as it is a standard utility)
* `pv` (pipe-viewer lets us see progress, although this is not as accurate on faster CPUs, you should be able to find it in your package manager or Homebrew as `pv`)
* `du` (calculates the size [disk usage] of the folder we are packaging/compressing and should be on virtually all \*nix systems)
  * OSX systems ship with a different version of `du` which require slight modifications of this idiom.
* `xz` (xz is modern, heavy duty slow compression utility in the same family as 7zip and a native rar equivalent on \*nix Systems, you should be able to find it in your package manager or Homebrew as `xz`)

### Usage:

`$ txz folder_I_want_to_recursively_compress`

Output in: `folder_I_want_to_recursively_compress.txz`
