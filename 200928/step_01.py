f  =  open ( 'nginx_logs_head.txt' , 'r' , кодировка = 'utf-8' )
# print (введите (f))
# print (dir (f))

file_data  =  f . readlines ()
# print (file_data)
для  строки  в  file_data :
    строка  =  строка . полоса ()
    печать ( строка )