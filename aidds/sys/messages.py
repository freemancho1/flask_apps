from dotmap import DotMap


_log = {
    'main': 'The construction cost prediction web service is ready. Please visit http://aidds.kdn.com:',
    'debug_mode': 'This server is running in debug mode.',
    'product_mode': 'This server is running in product mode.', 
    'exit': 'When you press Ctrl+C, the service will be terminated.', 
    'samples': {
        'main': 'The sample manager for the web service has started.',
        'samples': 'Accept numbers of sample data:',
    },
    'predict': {
        'main': 'The predic manager for the web service has started.',
        'json_size': 'Prediction request data size:',
        'result': 'Predict result:',
    },
    'manager': 'The service manager for the web service has started.',
    'exception': 'The system has terminated unexpectedly for an unknown reason.',
    'shut_down': 'The system has been shut down at the request of the administrator.'
}
log = DotMap(_log)


_exception = {
    'exception': 'The system has terminated unexpectedly for an unknown reason.',
    'unknown_file_ext': 'Unknown file extension error, the extension is',
    'bad_json': 'An error in the request JSON data',
    'hc_msg': {
        'ok': 'Service Ok',
        'cr': 'Service Ok, Data has been created',
        'nc': 'Service Ok, But no data returned',
        'e400': 'The browser (or proxy) sent a request that this server could not understand.',
        'e401': 'The server could not verify that you are authorized to access the URL requested.',
        'e403': 'You don\'t have the permission to access the requested resource. It is either read-protected or not readable by the server.',
        'e404': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.',
        'e405': 'No access permission for the requested method',
        'e500': 'The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.',
    }
}
exception = DotMap(_exception)