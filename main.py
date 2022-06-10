import requests, logging
import json
from rbr_srv_side import DESC


def POST_zapros():
    try:
        descript = str(DESC.PC_info.main_inf())
        logger.info('Загружаем массив данных о системе из файла...')
        logger.info(descript)
        logger.info('Массив данных загружен, отправляем на сервер...')
        new_data = {
                    'name': 'hostname',
                    'ip_address': requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'),
                    'description': descript,
                    'server_is_active': True
                    }
        url = 'http://127.0.0.1:8000/api/servers/add_post'
        response = requests.post(url, json=new_data)
        print(response.json())
        logger.info('Массив успешно отправлен на сервер!')
    except ConnectionError:
        logger.error('Возникла ошибка соединения с сервером! Проверьте соединение с сервером...')
    except TypeError:
        logger.error('Ошибка объединения несовместимых объектов...Проверьте аргументы в функциях...')
    except NameError:
        logger.error('Ошибка в имени переменной, проверьте верность указанных переменных...')
    except:
        logger.error('Возникла ошибка!')
    finally:
        logger.info('Логгер завершен!')

def logg_info(name):
    logger = logging.getLogger(name)
    format_log = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s', datefmt='%d %b %Y %H:%M:%S')
    logger.setLevel(logging.DEBUG)
    str_handler = logging.StreamHandler()
    str_handler.setFormatter(format_log)
    str_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(filename='logs/log_file.log', mode='w')
    file_handler.setFormatter(format_log)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(str_handler)
    logger.addHandler(file_handler)
    logger.info('Логгер запущен...')

logg_info('app')
logger = logging.getLogger('app.main')

if __name__ == "__main__":
    POST_zapros()