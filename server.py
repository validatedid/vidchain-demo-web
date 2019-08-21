import http.server
import socketserver
import multiprocessing, time

DIRECTORY = "demo/"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_demo_server(host='0.0.0.0', port=8080):
    with socketserver.TCPServer((host, port), Handler) as httpd:
        print(' * Starting VidChain demo server at http://' + host + ':' + str(port))
        httpd.serve_forever()

if __name__ == "__main__":
    print (" * Starting VidChain demo")
    # Start the job processes
    try:
        web_demo_server_proc = multiprocessing.Process(target=start_demo_server)

        # launch servers
        web_demo_server_proc.start()

        # Keep the main thread running, otherwise signals are ignored.
        while True:
            time.sleep(0.5)
 
    except KeyboardInterrupt:
        # Terminate the running processes.
        web_demo_server_proc.terminate()
        print('\n * Exiting VidChain demo')