# from celery import task
# from django.core.mail import send_mail
# from .models import Order
#
#
# @task
# def order_created(order_id):
#     """
#     Задача для відправлення повідомлення по електроній почті при умові успішного створення заказу.
#     :param order_id:
#     :return:
#     """
#     order = Order.objects.get(id=order_id)
#     subject = 'Order nr. {}'.format(order_id)
#     message = 'Dear {},\n\nYou have successfuly placed an order.\
#                 Your order id is {} '.format(order.first_name,
#                                              order_id)
#     mail_sent = send_mail(subject,
#                           message,
#                           'admin@myshop.com',
#                           [order.email])
#     return mail_sent
