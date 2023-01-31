import psutil
from psutil import virtual_memory as virt_mem
from psutil import disk_partitions as all_disks
from psutil import disk_usage as disk_mem_info
import speedtest
import logging

logger = logging.getLogger('app.DESC')

class PCInfo:

    @classmethod
    def main_inf(cls):
        all_inf_dict = {'Host_information': {}, }
        all_inf_dict['Host_information']['Name'] = psutil.users()[0][0]
        all_inf_dict['Network'] = cls.network_inf()
        all_inf_dict['Disk'] = cls.disk_inf()
        all_inf_dict['Memory'] = cls.memory_inf()
        all_inf_dict['Cpu'] = cls.cpu_inf()
        all_inf_dict['Load_average'] = cls.load_average_inf()
        logger.info('Получен массив данных о системе...')
        return all_inf_dict


    def network_inf(speed_chek=False): #поменять на True, если хотим получить скорость интернета в инфо
        network_list = [] # список для вывода

        bytes_dict = {} # словарь для сохранения информации
        net_io = psutil.net_io_counters()
        bytes_dict['internet_connection_status(UP / DOWN)'] = "UP" if net_io[0] > 0 and net_io[1] > 0 else "DOWN"
        bytes_dict['bytes_sent'] = net_io[0]
        bytes_dict['bytes_recived'] = net_io[1]
        network_list.append(bytes_dict)

        stats_dict = {} # словарь для сохранения информации
        st = speedtest.Speedtest()
        net_stats = psutil.net_if_stats()
        net_stats_key = list(net_stats)[0]
        stats_dict['max_speed'] = f'{net_stats[net_stats_key][2]} (Mbps)'
        stats_dict['mtu'] = net_stats[net_stats_key][3]


        if speed_chek == True:
            print("Wait a seconds, I'm testing the Internet speed...")
            stats_dict['download_speed'] = f'{round(st.download() / 10 ** 6, 2)} (Mbps)'
            stats_dict['upload_speed'] = f'{round(st.upload() / 10 ** 6, 2)} (Mbps)'

        network_list.append(stats_dict)

        return  network_list


    def disk_inf():
        disk_params = []
        for i in range(len(all_disks())):
            disk_dict = {}
            disk_mem = disk_mem_info(all_disks()[i].device)
            disk_dict['disk'] = str(all_disks()[i].device).rstrip('\\')
            disk_dict['file_system_type'] = all_disks()[i].fstype
            disk_dict['total'] = f'{round(disk_mem.total / 2 ** 30, 2)} Gb'
            disk_dict['used'] = f'{round(disk_mem.used / 2 ** 30, 2)} Gb'
            disk_dict['free'] = f'{round(disk_mem.free / 2 ** 30, 2)} Gb'
            disk_dict['used_percent'] = f'{disk_mem.percent} %'
            disk_params.append(disk_dict)

        return disk_params



    def memory_inf():
        mem_dict = {}
        mem_dict['memory_total'] = f'{round(virt_mem().total / 2 ** 30, 2)} Gb'
        mem_dict['memory_used'] = f'{round(virt_mem().used / 2 ** 30, 2)} Gb'
        mem_dict['memory_free'] = f'{round((virt_mem().total - virt_mem().used) / 2 ** 30, 2)} Gb'
        mem_dict['memory_percent'] = f'{virt_mem().percent} %'
        return mem_dict

    def cpu_inf():
        cpu_dict = {}
        cpu_dict['cpu_cores'] = psutil.cpu_count()
        cpu_dict['cpu_physical_cores'] = psutil.cpu_count(logical=False)
        cpu_freq_dict = dict(zip(['current', 'min', 'max'], psutil.cpu_freq()))
        cpu_dict['cpu_frequency'] = cpu_freq_dict
        return cpu_dict

    def load_average_inf():
        load_aver_dict = dict(zip(['1 min', '5 min', '15 min'], psutil.getloadavg()))
        return load_aver_dict