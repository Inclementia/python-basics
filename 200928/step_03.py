# f = open ('nginx_logs_head.txt', 'r', кодировка = 'utf-8')

# диспетчер контекста
# __войти__
# __exit__ -> f.close ()
# transaction.atomic () -> точка восстановления
с  open ( 'nginx_logs_head.txt' , 'r' , encoding = 'utf-8' ) как  f :
    для  строки  в  f . читать (). splitlines ():
        печать ( строка )

# print (f.closed)
