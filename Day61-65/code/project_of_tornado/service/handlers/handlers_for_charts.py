import json
import random
import time

import tornado.websocket

clients_set = set()


class ChartHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        clients_set.add(self)

    def on_close(self):
        clients_set.remove(self)


def gen_mock_data(num_of_series, num_of_sample):
    data = []
    for _ in range(num_of_series):
        series = []
        for _ in range(num_of_sample):
            series.append(random.randint(50, 500))
        data.append(series)
    return data


def send_data(delay):
    while True:
        for ws_client in clients_set:
            data = gen_mock_data(3, 7)
            ws_client.write_message(json.dumps(data).encode())
        time.sleep(delay)
