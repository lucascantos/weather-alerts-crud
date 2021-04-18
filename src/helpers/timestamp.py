import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
formats = {
    'dashed': "%Y-%m-%d-%H-%M",
    'default': "%Y-%m-%d %H:%M",
    'br': "%d/%m/%Y %H:%M",
    'url': "%Y-%m-%dT%H:%M",

    'date_br': "%d/%m/%Y",
    'date_default': "%Y-%m-%d"
}
    
def date_string (dt=datetime.utcnow(), format='default'):
    '''
    Returns datetime in a string format chosen by default names or custom
    :params dt: datetime input
    :params format: format of string
    '''
    if format in formats:
        format = formats[format]
    else:
        format = format
    try:
        return dt.strftime(format)
    except Exception as e:
        raise ValueError(e)

def normalize_timestamp(timestamp):
    '''
    Split a timestamp and return datetime.strptime. 
    :params timestamp: string of format YYY-mm-dd HH:MM
    '''
    headers = ['year', 'month', 'day', 'hour', 'minute']
    splitted = re.split('-|:| |T',timestamp)
    splitted = [int(i) for i in splitted]
    if len(headers) != len(splitted):
        if len(splitted) == 3:
            splitted.extend([12, 0])
        else:
            raise ValueError('wrong string format')
    return datetime(**dict(zip(headers, splitted)))

def to_datetime(timestamp, format='url'):
    '''
    Converts timestamp string to datetime
    :params timestamp: string with datetime format
    :params format: string with format
    '''
    return datetime.strptime(timestamp, formats[format])

def relative_date(**kwargs):
    '''
    Return a datetime relative to UTC now
    :params kwargs: args of the relative_delta function. eg. hours=2
    '''
    now = datetime.utcnow()
    return now + relativedelta(**kwargs)
