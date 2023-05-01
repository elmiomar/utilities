# rsync_transfer.sh

A Bash script for transferring files or directories from a local machine to a remote server using rsync and SSH.

## Usage

```sh
./rsync_transfer.sh [local_path] [username] [remote_ip] [remote_path] [private_key_path]
```

Transfers a file or directory from the local machine to a remote server using rsync and SSH.

### Arguments

* `local_path`: Path to the file or directory on the local machine (default: `/path/to/local/path`).
* `username`: Username for SSH authentication (default: `user`).
* `remote_ip`: IP address or hostname of the remote server (default: `remote_server`).
* `remote_path`: Path to the directory on the remote server where the file or directory will be placed (default: `/path/on/server`).
* `private_key_path`: Path to the private SSH key file on the local machine (default: `/path/to/private/key`).

## Examples

Transfer a file:

```sh
./rsync_transfer.sh /path/to/local/file user remote_server /path/on/server /path/to/private/key
```

Transfer a directory:

```sh
./rsync_transfer.sh /path/to/local/directory user remote_server /path/on/server /path/to/private/key
```
