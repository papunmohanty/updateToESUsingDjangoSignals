# Update To Elasticsearch using Django's Signals

## Commands

Create Elastic Search Indexes from Django command
```sh
python manage.py search_index --create
```

## CURL: to create Order

```sh
curl --location 'http://127.0.0.1:8000/orders/create' \
--header 'Content-Type: application/json' \
--data '{
    "order_number": "order00003",
    "customer_name": "John Doe",
    "total_amount": 1234.56
}'
```

## CURL: to update Order

```sh
curl --location --request PATCH 'http://127.0.0.1:8000/orders/update/3/' \
--header 'Content-Type: application/json' \
--data '{
    "customer_name": "Jane Doe",
    "total_amount": 12.56
}'
```


> :warning: **If you are using signal to update elasticsearch, then things can be slow if time taken is long**: Be very careful here!

Django signals are synchronous and run in the same thread as the code that triggers them. When a signal is sent, all of the receivers for that signal are executed in the order in which they were connected.
Here's a brief overview of Django's signal architecture:

- Django signals provide a way for decoupling parts of an application, allowing different components to communicate with each other without being tightly coupled.

- Django signals are implemented using Python's built-in signals framework, which provides a simple way to define and send signals.
- Signals are triggered by sending them using the Signal.send(sender, **kwargs) method. The sender is usually the model class that is triggering the signal, and the **kwargs can include any additional data that needs to be sent with the signal.

- Receivers are functions that are registered to handle a specific signal. They are connected to the signal using the Signal.connect(receiver, sender=None, weak=True, dispatch_uid=None) method. The receiver function will be called whenever the signal is sent, and will receive the sender and any additional data sent with the signal as arguments.

- Django signals are executed synchronously in the same thread as the code that triggers them. If the receiver function takes a long time to execute, it will block the thread and slow down the entire application.

- Django signals can be used for a variety of purposes, such as updating a search index when a model is saved, sending an email when a user signs up, or logging activity in the application.

Overall, Django's signal architecture provides a flexible and powerful way to decouple components of an application and enable communication between them. However, it's important to use signals judiciously and be aware of their potential impact on performance.