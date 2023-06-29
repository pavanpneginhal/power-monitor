
import tkinter as tk
import os
import time

def get_power():
    power = os.popen("cat /sys/class/power_supply/BAT0/power_now").read()
    return int(power)

def get_energy():
    energy = os.popen("cat /sys/class/power_supply/BAT0/energy_now").read()
    return int(energy)

def get_voltage():
    voltage = os.popen("cat /sys/class/power_supply/BAT0/voltage_now").read()
    return int(voltage)

def get_capacity():
    capacity = os.popen("cat /sys/class/power_supply/BAT0/capacity").read()
    return int(capacity)

def get_status():
    status = os.popen("cat /sys/class/power_supply/BAT0/status").read()
    return status

def get_cpu_usage():
    cpu = str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())
    return cpu

def get_mem_usage():
    mem = os.popen("free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2 }'").readline()
    return mem



def disk_usage():
    du = str(os.popen("df -h | awk '$NF==\"/\"{printf \"%s\", $5}'").readline().strip())
    return du

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds


def main():
    root = tk.Tk()
    root.title("Power Consumption and Activity Monitor")
    root.geometry("400x270")
    # root.resizable(False, False)


    power = tk.Label(root, text="Power: " + str(get_power()) + " uW")
    power.pack()

    energy = tk.Label(root, text="Energy: " + str(get_energy()) + " uWh")
    energy.pack()

    voltage = tk.Label(root, text="Voltage: " + str(get_voltage()) + " uV")
    voltage.pack()

    capacity = tk.Label(root, text="Capacity: " + str(get_capacity()))
    capacity.pack()

    status = tk.Label(root, text="Status: " + str(get_status()))
    status.pack()

    cpu = tk.Label(root, text="CPU Usage: " + str(get_cpu_usage()) + " %")
    cpu.pack()

    mem = tk.Label(root, text="Memory Usage: " + str(get_mem_usage()))
    mem.pack()

    disk = tk.Label(root, text="Disk Usage: " + str(disk_usage()) )
    disk.pack()

    uptime = tk.Label(root, text="Uptime: " + str(get_uptime()) + " seconds")
    uptime.pack()



    root.mainloop()

if __name__ == "__main__":
    main()

        
