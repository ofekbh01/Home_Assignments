#!/usr/bin/env python3\

import subprocess as sp
from multiprocessing import Pool
from functools import partial

SERVERS = ['10.0.2.4', '10.0.2.5']
USERNAME = 'vboxuser'
PASSWORD = 'Password1'


def run_command(cmd, server):
    """
    Prints the output of the command from server.
    connecting using sshpass with given user and password,
    and running the users' command.
    If the command is successful - prints 'Success' and output,
    And if the command failed - prints 'Error' and the error.
    :param cmd: the user-selected command
    :param server: each server from user-provided list
    :return: stdout / stderr
    """
    # Could be with sshpass (if installed and the server has password) as well as with keys
    ssh_command = f'sshpass -p {PASSWORD} ssh {USERNAME}@{server} {cmd}'
    ssh = sp.Popen(ssh_command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    result, error = ssh.communicate()
    if result.decode() == "":
        return f"Error\n{error.decode()}"
    else:
        return f"Success\n{result.decode()}"


def main():
    """Takes user input command and runs run_commend func,
    in each server in parallel, then takes each output and prints it with the servers' IP."""
    cmd = input(f"Please enter your desired command:\n")
    with Pool() as pool:
        output = pool.map(partial(run_command, cmd), SERVERS)

    for server, result in zip(SERVERS, output):
        print(f"Server: {server}\n{result}")


if __name__ == '__main__':
    main()
