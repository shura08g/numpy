# pip install psutil
# import os
import psutil
# from ctypes import string_at
# from sys import getsizeof
from ctypes.wintypes import *
from ctypes import windll


PROCNAME = "EXCEL.EXE"
# print(os.getpid())


def get_all_proc():
    '''Return a list of processes'''
    ls_all_proc = []
    for proc in psutil.process_iter():
        ls_all_proc.append(proc)
    return ls_all_proc


def find_list_proc_by_name(name):
    '''Return a list of processes matching 'name'.'''
    ls_proc = []
    for proc in psutil.process_iter():
        if proc.name() == name:
            ls_proc.append(proc)
    return ls_proc


def find_proc_by_name(name):
    '''Return a list of processes matching 'name'.'''
    for proc in psutil.process_iter():
        if proc.name() == name:
            return proc
    return None


def is_proc(proc):
    if proc is None:
        print("Process {0} not found".format(PROCNAME))
        return False
    else:
        return True


def get_pid(proc):
    return proc.pid


def test_one_proc(name):
    print("------TEST--------")
    proc = find_proc_by_name(name)
    proc_id = None
    if is_proc(proc):
        proc_id = get_pid(proc)
    else:
        proc_id = -1
    print(proc_id)
    print("-----END TEST-----")


def main():
    test_one_proc(PROCNAME)
    ls_proc = find_list_proc_by_name(PROCNAME)
    proc_id = 0
    if len(ls_proc) > 0:
        proc_id = get_pid(ls_proc[0])
    else:
        print("Process {0} not found".format(PROCNAME))
        exit()
    print(proc_id)
    print(ls_proc[0].memory_info())
    rss_mem = int(ls_proc[0].memory_info().rss / 1024)
    print("RSS memory used by process: {0}".format(rss_mem))
    print("% memory: {0}".format(ls_proc[0].memory_percent()))

    mem_address = 0x05B3015C

    # PROCESS_VM_READ = 0x0010
    # PROCESS_VM_WRITE = 0x0020
    # PROCESS_VM_OPERATION = 0x0008
    PROCESS_ALL_ACCESS = 0x1F0FFF
    process = windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, proc_id)
    buf = (ctypes.c_double)()
    pi = ctypes.pointer(buf)
    windll.kernel32.ReadProcessMemory(process, mem_address, pi, 16, 0)
    print(buf)
    # windll.kernel32.WriteProcessMemory(self.h_process, address, c_data, length, byref(count))


if __name__ == "__main__":
    main()
