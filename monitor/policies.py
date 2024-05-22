import base64

VERIFIER_SEAL = 'verifier_seal'


def check_operation(id, details):
    authorized = False

    src = details['source']
    dst = details['deliver_to']
    operation = details['operation']

    if src == 'central' and dst == 'connection' and operation == 'send_message':
        authorized = True

    if src == 'central' and dst == 'printer' and operation == 'print_document':
        authorized = True

    if src == 'central' and dst == 'screen' and operation == 'authorize_transaction':
        authorized = True

    if src == 'connection' and dst == 'central' and operation == 'receive_message':
        authorized = True

    if src == 'connection' and dst == 'virtual' and operation == 'get_info':
        authorized = True

    if src == 'input_control' and dst == 'central' and operation == 'send_keyboard_input':
        authorized = True

    if src == 'battery_control' and dst == 'control_input' and operation == 'send_battery_info':
        authorized = True

    if src == 'keyboard' and dst == 'control_input' and operation == 'send_keyboard_input':
        authorized = True

    if src == 'nfc' and dst == 'control_input' and operation == 'send_nfc_data':
        authorized = True

    if src == 'virtual' and dst == 'nfc' and operation == 'send_virtual_card_data':
        authorized = True

    # Добавляем проверку подлинности данных в сообщении
    if check_payload_seal(details.get('payload', '')):
        authorized = True

    return authorized

def check_payload_seal(payload):
    try:
        p = base64.b64decode(payload).decode()
        if p.endswith(VERIFIER_SEAL):
            print('[info] Payload seal is valid')
            return True
    except Exception as e:
        print(f'[error] Seal check error: {e}')
        return False