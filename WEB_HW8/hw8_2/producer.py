import json
from mongoengine import connect
from datetime import datetime

import pika



credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

exchange_name = 'Web16Exchange'

channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
channel.queue_declare(queue='web_16_queue', durable=True)
channel.queue_bind(exchange=exchange_name, queue='web_16_queue')


def create_tasks(nums: int):
    for i in range(nums):
        message = {
            'id': i,
            'payload': f"Date: {datetime.now().isoformat()}",
            'processed': False  # Поле, що вказує, чи було повідомлення оброблено
        }

        channel.basic_publish(exchange=exchange_name, routing_key='web_16_queue', body=json.dumps(message))

    connection.close()


if __name__ == '__main__':
    create_tasks(100)
