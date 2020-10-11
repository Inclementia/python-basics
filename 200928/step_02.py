f  =  open ( 'nginx_logs_head.txt' , 'r' , кодировка = 'utf-8' )

# file_data = f.readlines ()
# file_data = f.read (). splitlines ()
# для строки в file_data:
# f.readlines () -> []
# f.read () -> ''
# print (введите (f.readlines ()))
# print (введите (f.read ()))
# для строки в f.read (). split ('\ n'):
для  строки  в  f . читать (). splitlines ():
    печать ( строка )
    # remote_IP_address, row_tail = row.split (maxsplit = 1)
    # _, _request_datetime = row_tail.split ('[', maxsplit = 1)
    # request_datetime, row_tail = _request_datetime.split (']', maxsplit = 1)
    #
    # _, _request_method, row_tail = row_tail.split ('"', maxsplit = 2)
    # request_method, required_resource, _ = _request_method.split (maxsplit = 2)
    #
    # parsed_row = [удаленный_IP_адрес, дата_запроса, метод_запроса, запрошенный_ресурс]
    # parsed_row = список (карта (str.strip, parsed_row))
    # печать (parsed_row)

печать ( ф . закрыто )
f . закрыть ()
печать ( ф . закрыто )