import web, psutil

urls = ('/(.*)', 'hello')

app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!' + str(psutil.virtual_memory())
app.run()