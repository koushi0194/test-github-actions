# """
# Wallet app
# """

# class Wallet:
#     """
#     Wallet class to add & spend cash
#     """

#     def __init__(self, initial_amount=0):
#         """
#         Initial amount
#         """
#         self.balance = initial_amount

#     def spend_cash(self, amount):
#         """
#         Spend cash
#         """
#         if self.balance < amount:
#             raise Exception('Not enough available to spend {}'.format(amount))
#         self.balance -= amount

#     def add_cash(self, amount):
#         """
#         Add cash to wallet
#         """
#         self.balance += amount

# if __name__ == "__main__":
#     print("This is your wallet")

import multiprocessing
import subprocess
import sys
import psutil


def migrate_shares_multiprocess(copy_cmd_list: list) -> None:
    """Create multiple process to perform migration.
    Args:
        cmd (list): Robocopy command to migrate shares
    """
    no_of_process_mp = multiprocessing.cpu_count() * 4
    print('mp count', no_of_process_mp)
    ps_count = psutil.cpu_count(logical=False)
    ps_count_l = psutil.cpu_count(logical=True)
    print('ps_count', ps_count)
    print('ps_count_logical', ps_count_l)
    no_of_process = 2
    print('the queue')
    the_queue = multiprocessing.Queue()
    print('the pool')
    print('no of process', no_of_process)
    the_pool = multiprocessing.Pool(
        no_of_process,
        mp_queue, (the_queue,))
    print('the commands')
    for i in range(len(copy_cmd_list)):
        the_queue.put(copy_cmd_list[i])
    for i in range(no_of_process):
        the_queue.put(None)
    # prevent adding anything more to the queue and wait for queue to empty
    the_queue.close()
    the_queue.join_thread()
    # prevent adding anything more to the process pool
    #      and wait for all processes to finish
    the_pool.close()
    the_pool.join()


def exec_os_cmd(cmd: str) -> bytes:
    """Execute a command on the OS and return the running process.
    Args:
        cmd: command to execute as a list object.
    Returns:
        (bytes)stdout: Command Output
    """
    print('executing command')
    p = subprocess.Popen(["powershell.exe", cmd], shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print('finished executing command')
    if len(stderr) == 0:
        return stdout
    else:
        print(f"Error while executing {cmd}")
        print(f"Error is : {stderr}")
        sys.exit(1)


def mp_queue(queue) -> None:
    """Runs commands that are in queued order.
    Args:
        queue: The queue of commands to queue up as processes
    """
    while True:
        # block=True means make a blocking call to wait for items in queue
        item = queue.get(block=True)
        if item is None:
            break
        cmd_output = exec_os_cmd(item)
        print(cmd_output)


if __name__ == "__main__":
    copy_cmd_list = ['echo "1"', 'echo "2"']
    migrate_shares_multiprocess(copy_cmd_list)

