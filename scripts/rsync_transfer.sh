#!/bin/bash

# Set default values for arguments
local_path=${1:-/path/to/local/path}
username=${2:-user}
remote_ip=${3:-remote_server}
remote_path=${4:-/path/on/server}
private_key_path=${5:-/path/to/private/key}

# Print usage message
usage() {
    echo "Usage: $0 [local_path] [username] [remote_ip] [remote_path] [private_key_path]"
    echo ""
    echo "Transfers a file or directory from the local machine to a remote server using rsync and SSH."
    echo ""
    echo "Arguments:"
    echo "  local_path         Path to the file or directory on the local machine (default: /path/to/local/path)"
    echo "  username           Username for SSH authentication (default: user)"
    echo "  remote_ip          IP address or hostname of the remote server (default: remote_server)"
    echo "  remote_path        Path to the directory on the remote server where the file or directory will be placed (default: /path/on/server)"
    echo "  private_key_path   Path to the private SSH key file on the local machine (default: /path/to/private/key)"
    echo ""
}

# Check if the help flag was provided
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    usage
    exit 0
fi

# Transfer the file or directory using rsync and SSH
if [[ -d "$local_path" ]]; then
    rsync -avz -e "ssh -i ${private_key_path}" -r "${local_path}" "${username}@${remote_ip}:${remote_path}"
elif [[ -f "$local_path" ]]; then
    rsync -avz -e "ssh -i ${private_key_path}" "${local_path}" "${username}@${remote_ip}:${remote_path}"
else
    echo "Error: $local_path is not a valid file or directory."
    exit 1
fi
