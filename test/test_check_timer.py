import datetime

from src.send_mail import SendEmail, general_status


user = 'leopoldo'

    
def test_send_record():
    now = datetime.datetime.now()
    call_one = SendEmail()
    date = now.strftime(call_one.format)
    call_one.check_limit('News', user, 'hola')
    assert len(call_one.records[user][date]) == 1
    call_one.check_limit('News', user, 'hola')
    assert len(call_one.records[user][date]) == 1
    call_one.check_limit('News', user, 'hola')
    assert len(call_one.records[user][date]) == 1
    
    general_status["News"][2]["limit"] = 3
    
    call_one.check_limit('News', user, 'hola')
    assert len(call_one.records[user][date]) == 2

    
def test_send_record_used_default_limit():
    now = datetime.datetime.now()
    call_one = SendEmail()
    date = now.strftime(call_one.format)
    call_one.check_limit('X', user, 'hola')
    assert len(call_one.records[user][date]) == 1
    call_one.check_limit('X', user, 'hola')
    assert len(call_one.records[user][date]) == 1
    call_one.check_limit('X', user, 'hola')
    assert len(call_one.records[user][date]) == 1