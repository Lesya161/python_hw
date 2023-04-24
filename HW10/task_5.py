"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

args = ['ping', 'yandex.ru']
ping_web = subprocess.Popen(args, stdout=subprocess.PIPE)
for el in ping_web.stdout:
    result = chardet.detect(el)
    el = el.decode(result['encoding']).encode('utf-8')
    print(el.decode('utf-8'))