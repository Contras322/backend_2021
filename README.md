# WEB-SERVER

# STATIC FILES FROM NGINX

 Проверяем работу nginx на отдачу статических файлов (код виртуального сервера находится в фаsudo /etc/init.d/nginx startйле nginx.conf):
 sudo /etc/init.d/nginx start
 
 http://homework3:8089/static/ 
 
 http://homework3:8089/static/img_bg_1_gradient.jpg
 
 # SIMPLE WSGI APP WITH GUNICORN
 
Создаем виртуальное окружение, активируем его:
 
server $ python3 -m venv <venv_dir_name>

server $ source <venv_dir_name>/bin/activate

Осуществляем WSGI, тестируем:

http://127.0.0.1:8000/

http://127.0.0.1:8000/?a=15&b=11

# PROXY ON NGINX 

Добавляем проксирование в конфигурацию nginx, проверяем работу:

gunicorn --workers 9 app:app - запуск gunicorn

http://homework3:8089/api/sdfdsf - <list_iterator object at 0x7fa182f0e730>

http://homework3:8089/api/sdfds - <list_iterator object at 0x7fa1826de130>

# TEST NGINX AND GUNICORN WITH ab

Осуществим тестирование производительности с помощью ab, используем 4 потока, 5000 запросов, информацию о результатах тестирования поместим в текстовые файлы.\
1) ab -c 4 -n 5000 http://homework3:8089/static/ > test_static.txt
2) ab -c 4 -n 5000 http://127.0.0.1:8000/ > test_dynamic.txt
3) ab -c 4 -n 5000 http://homework3:8089/api/alolo > test_proxy.txt
4) ab -c 10040 -n 70000 http://localhost:8089/api/ > test_error.txt
