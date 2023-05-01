#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

def transfer_file(local_file_path, username, remote_ip, remote_path, private_key_path):
    """Transfers a file to a remote server using rsync and SSH.

    Args:
        local_file_path (str): Path to the file on the local machine.
        username (str): Username for SSH authentication.
        remote_ip (str): IP address or hostname of the remote server.
        remote_path (str): Path to the directory on the remote server where the file will be placed.
        private_key_path (str): Path to the private SSH key file on the local machine.

    Raises:
        FileNotFoundError: If the local file does not exist.
    """
    if not os.path.exists(local_file_path):
        raise FileNotFoundError(f"{local_file_path} not found")
    subprocess.run(["rsync", "-avz", "-e", f"ssh -i {private_key_path}", local_file_path, f"{username}@{remote_ip}:{remote_path}"])

def transfer_directory(local_directory_path, username, remote_ip, remote_path, private_key_path):
    """Transfers a directory to a remote server using rsync and SSH.

    Args:
        local_directory_path (str): Path to the directory on the local machine.
        username (str): Username for SSH authentication.
        remote_ip (str): IP address or hostname of the remote server.
        remote_path (str): Path to the directory on the remote server where the directory will be placed.
        private_key_path (str): Path to the private SSH key file on the local machine.

    Raises:
        FileNotFoundError: If the local directory does not exist.
    """
    if not os.path.exists(local_directory_path):
        raise FileNotFoundError(f"{local_directory_path} not found")
    subprocess.run(["rsync", "-avz", "-e", f"ssh -i {private_key_path}", "-r", local_directory_path, f"{username}@{remote_ip}:{remote_path}"])

def main(args):
    """Main function for the rsync_transfer script.

    Args:
        args (argparse.Namespace): Command-line arguments.
    """
    if args.directory:
        transfer_directory(args.path, args.username, args.ip, args.remote_path, args.private_key)
    else:
        transfer_file(args.path, args.username, args.ip, args.remote_path, args.private_key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transfers a file or directory to a remote server using rsync and SSH.")
    parser.add_argument("path", help="Path to the file or directory on the local machine.")
    parser.add_argument("-u", "--username", default="user", help="Username for SSH authentication. (default: user)")
    parser.add_argument("-i", "--ip", default="remote_server", help="IP address or hostname of the remote server. (default: remote_server)")
    parser.add_argument("-r", "--remote-path", default="/path/on/server", help="Path to the directory on the remote server where the file or directory will be placed. (default: /path/on/server)")
    parser.add_argument("-k", "--private-key", default="/path/to/private/key", help="Path to the private SSH key file on the local machine. (default: /path/to/private/key)")
    parser.add_argument("-d", "--directory", action="store_true", help="Transfer a directory instead of a file.")
    args = parser.parse_args()
    main(args)
