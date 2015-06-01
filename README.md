#WebDAV Syncer

Очень простой скрипт для закачки файлов по протоколу WebDAV. (Яндекс.Диск, например)

##Зависимости
Зависит только от библиотеки [webdavclient](https://pypi.python.org/pypi/webdavclient/). Версия 1.0.3 лежит в папке wevbdav.

##Использование
`webdavsyncer.py SETTINGS_FILE LOCAL_PATH REMOTE_NAME`
Например: `webdavsyncer.py ~/settings.txt ~/cats_23.jpg cat3.jpg`
Где файл `settings.txt` имеет вид:
```
{
    'webdav_hostname': "https://webdav.URL.com",
    'webdav_login': "LOGIN",
    'webdav_password': "PASSWORD",
    'rem_path': "Backups/"
}
```

Мой сценарий использования: храню много таких файлов настроек для различных сервисов в одной папке, которая шифруется с помощью encfs. Средство создания резервных копий, создания архива, проходит по ней и вызывает синхронизацию для каждого из файлов настроек.

##To-Do
1. Добавить автоматизацию сценария выше
2. Генерация машиночитаемого отчёта