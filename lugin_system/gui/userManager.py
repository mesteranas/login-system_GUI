from . import models
import subprocess
def lugin(user_name):
    setion=models.get_session()
    log=models.Auth(serial=get_serial_number(),User=user_name)
    setion.add(log)
    setion.commit()
def get_serial_number():
    try:
        result = subprocess.run(['wmic', 'bios', 'get', 'serialnumber'], capture_output=True, text=True)
        serial_number = result.stdout.strip().split('\n')[1].strip()
        return serial_number
    except Exception as e:
        return None
def is_login():
    user=models.Auth
    try:
        setion=models.get_session()
        log=setion.query(user).filter_by(serial=get_serial_number()).first()
        if log:
            a=True
        else:
            a=False
    except:
        a=False
    return a
def logout():
    setion=models.get_session()
    log=setion.query(models.Auth).filter_by(serial=get_serial_number()).first()
    setion.delete(log)
    setion.commit()
