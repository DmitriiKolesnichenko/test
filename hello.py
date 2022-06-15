def wsgi_application(environ, start_response):
    headers = [('Content-type', 'text/plain')]
    status = '200 OK'
    start_response(status, headers)
    res = '\n'.join(environ['QUERY_STRING'].split('&'))
    print(res)

    return [res.encode('utf-8')]
