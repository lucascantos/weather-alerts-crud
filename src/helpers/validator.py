from cerberus import Validator as CerberusValidator
from src.helpers.response import error_message
import json

class CustomValidator(CerberusValidator):
    def _validate_greater_than(self, to_compare, field, value):
        '''tests whether a field is greater than or equal to another.
        The rule's arguments are validated against this schema:
        {'type': 'string'}
        '''
        if to_compare not in self.document or type(self.document[to_compare]) != type(value) or self.document[to_compare] >= value:
            self._error(field, f"Must be smaller than the field: {to_compare}")

def validate(event, schema, allow_unknown=True, remove_requirement=False):
    '''
    Validade an event using a schema.
    :params event: Target to be evaluated 
    :params schema: Schema to be compared
    :params allow_unknown: True if allow parameters not listed on schema
    '''
    # if isinstance(schema, list):
    #     schema = {'payload': {'oneof_schema': schema, 'type': 'dict'}}

    v = CustomValidator(schema)
    v.allow_unknown = allow_unknown
    result = v.validate(event, update=remove_requirement)
    fixed_data = v.document
    return fixed_data, error_handler(v)

def error_handler(v):
    '''
    Return a error Response in case any validation error occur
    :params v: Validator to be analysed
    '''
    if len(v._errors) > 0:
        status_code = 400
        return error_message(v.errors,status_code)

def special_error_handler(v):
    '''
    Return a error Response in case a validation error occur.
    Can be tailored to send specific Responses in different schema errors.
    :params v: Validator to be analysed
    '''
    if len(v._errors) > 0:
        status_code = 400
        payload = {}
        for i in v._errors:
            if i.child_errors is not None:
                special_code_flag = _get_child_code(i.child_errors[0])
                if special_code_flag:
                    status_code = 422
        return error_message(v.errors,status_code)

def _get_child_code(children):
    '''
    Make a special response status_code based on cerberus error codes.
    :params children: 
    '''
    special_codes = [66, 67]
    if children.code in special_codes:
        return True
    # yield int(children.code)
    if children.child_errors is not None:
        for child in children.child_errors:
            return _get_child_code(child)    

def valid_uuid(uuid):
    '''
    Checks if string is in UUID format
    :params uuid: String
    '''
    import re
    regex = re.compile('[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[a-f0-9]{4}-[a-f0-9]{12}', re.I)
    return bool(regex.match(uuid))