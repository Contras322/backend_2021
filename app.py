import json
from datetime import datetime
from urllib.parse import urlunparse


def app(environ, start_response):
    time = datetime.now().strftime("%H:%M:%S")
    url = urlunparse(("http", environ["SERVER_NAME"] + ':' + environ["SERVER_PORT"],  environ["PATH_INFO"],
                      "", environ["QUERY_STRING"],  ""))

    raw_data = json.dumps(dict(time=time, url=url), indent=4).encode("utf-8")
    start_response("200 OK",
                   [("Content-Type", "text/plain"),
                    ("Content-Length", str(len(raw_data))),
                    ])

    print(iter([raw_data]))
    return iter([raw_data])
