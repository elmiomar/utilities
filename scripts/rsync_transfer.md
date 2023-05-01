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

Before using the script, you need to set the execute permission on the file using the following command:

```sh
chmod +x rsync_transfer.sh
```

## Examples

Transfer a file:

```sh
./rsync_transfer.sh /path/to/local/file user remote_server /path/on/server /path/to/private/key
```

Transfer a directory:

```sh
./rsync_transfer.sh /path/to/local/directory user remote_server /path/on/server /path/to/private/key
```

# rsync_transfer.py

A Python script for transferring files or directories from a local machine to a remote server using rsync and SSH.

## Usage

```sh
./rsync_transfer.py [path] [-u USERNAME] [-i IP] [-r REMOTE_PATH] [-k PRIVATE_KEY_PATH] [-d]
```

Transfers a file or directory from the local machine to a remote server using rsync and SSH.

### Arguments

* `path` (str): Path to the file or directory on the local machine.
* `-u`, `--username` (str): Username for SSH authentication. (default: `user`)
* `-i`, `--ip` (str): IP address or hostname of the remote server. (default: `remote_server`)
* `-r`, `--remote-path` (str): Path to the directory on the remote server where the file or directory will be placed. (default: `/path/on/server`)
* `-k`, `--private-key` (str): Path to the private SSH key file on the local machine. (default: `/path/to/private/key`)
* `-d`, `--directory` (flag): Transfer a directory instead of a file.

Before using the script, you need to set the execute permission on the file using the following command:

```sh
chmod +x rsync_transfer.py
```

## Examples

Transfer a file:

```sh
./rsync_transfer.py myfile -u user -i remote_server -r /path/on/server -k /path/to/private/key
```

Transfer a directory:

```
./rsync_transfer.py mydir -u user -i remote_server -r /path/on/server -k /path/to/private/key -d
```
