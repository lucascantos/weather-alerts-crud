user_schema = {   
    'id': {
        'type': 'string',
        'required': True,
        'coerce': (str, lambda x: x.lower())
    },
    'latitude':{
        'type': 'float',
        'required': True,
        'min': -60.0,
        'max': 10,
        'coerce': (float, lambda x: round(x, 5))
    },
    'longitude':{
        'type': 'float',
        'required': True,
        'min': -80.0,
        'max': -30.0,
        'coerce': (float, lambda x: round(x, 5))
    },
    'radius':{
        'type': 'float',
        'default': 10,
        'max': 30.0,
        'min': 0.1,
        'coerce': (float, lambda x: round(x, 1))
    },
    'variable':{
        'type': 'list',
        'default': ['lightning','precipitation'],
        'allowed': [
            'lightning',
            'precipitation'
        ]
    }  
}

create_schema = {
    'payload':{
        'oneof':[
            {
                'type': 'list',
                'schema':{
                    'type': 'dict',
                    'schema': user_schema
            }
            },
                {
                'type': 'dict',
                'schema': user_schema
            
            }

        ]
    }
}

batch_create_schema = {
    'payload':{
        'type': 'list',
        'schema':{
            'type': 'dict',
            'schema': user_schema
        }
    }
}

payload_schema = {
    'payload':{
        'type': 'dict',
        'schema': user_schema
    }
}

# Schema of AWS event
event_schema = {
    'pathParameters':{
        'type': 'dict',
        'default': {},
        'schema':{
            'uid':{
                'type': 'string',
                'required': True,
            },
        }
    }
}