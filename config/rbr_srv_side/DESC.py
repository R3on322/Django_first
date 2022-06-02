import psutil


# {'host_information': {'sysname': ..., 'hostname': ...},
#  'network': [{'interface': up / down, 'mtu': ...}...],
#  'disk': [{'disk: ..., 'mountpoint': ..., 'file_system_type', 'total': ..., 'used': ....} ],
#  'memory': {'memory_total': ..., 'memory_used': ..., 'memory_percent': ...},
# 'cpu': {'cpu_cores': ..., 'cpu_physical_cores': ..., 'cpu_freqency': {...}},
#'load_average': {'1 min': ..., '5 min': ..., '15 min': ...}}}

class PC_info:

    def main_inf():
        user_name = psutil.users()[0][0]
        return f'Name: {user_name}'

    def network_inf():
        net_io = psutil.net_io_counters()
        bytes_send = net_io[0]
        bytes_rec = net_io[1]
        net_stats = psutil.net_if_stats()
        net_stats_key = list(net_stats)[0]
        return f'network: ' \
               f'internet_connection_status(UP/DOWN) = {"UP" if bytes_send > 0 and bytes_rec > 0 else "DOWN"}, ' \
               f'interface_status(UP/DOWN) = {"UP" if net_stats[net_stats_key][0] == True else "DOWN"}, ' \
               f'bytes sent = {bytes_send}, ' \
               f'bytes recived = {bytes_rec}, ' \
               f'line speed = {net_stats[net_stats_key][2]}, ' \
               f'mtu = {net_stats[net_stats_key][3]}'


    def disk_inf():
        disk_params = []
        all_disks = psutil.disk_partitions()
        for i in range(len(all_disks)):
            disk_dict = {}
            disk_mem_info = psutil.disk_usage(all_disks[i][1])
            disk_dict['disk'] = all_disks[i][0]

    def memory_inf():
        pass

    def cpu_inf():
        pass

    def load_average_inf():
        pass


a = PC_info
print(a.main_inf())
print(a.network_inf())
print(a.disk_inf())

# print(psutil.disk_usage('/'))
print(psutil.disk_partitions())

# print(psutil.disk_usage(psutil.disk_partitions()[0][0]))
# print(psutil.disk_usage(psutil.disk_partitions()[1][0]))
# print(psutil.disk_usage(psutil.disk_partitions()[2][0]))
# print(psutil.disk_usage(psutil.disk_partitions()[3][0]))

