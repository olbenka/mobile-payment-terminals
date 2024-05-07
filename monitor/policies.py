def check_operation(id, details):
    authorized = False
    
    print(f"[info] checking policies for event {id},"
          f" {details['source']}->{details['deliver_to']}: {details['operation']}")
    
    src = details['source']
    dst = details['deliver_to']
    operation = details['operation']
    
    # Проверяем различные операции для разных источников и получателей
    if src == 'central' and dst == 'printer' and operation == 'print_document':
        authorized = True
    
    if src == 'central' and dst == 'screen' and operation == 'display_message':
        authorized = True
    
    if src == 'central' and dst == 'connection' and operation == 'send_message':
        authorized = True

    if src == 'connection' and dst == 'central' and operation == 'receive_message':
        authorized = True

    if src == 'control_input' and dst == 'central' and operation == 'send_data':
        authorized = True
    
    
    return authorized
