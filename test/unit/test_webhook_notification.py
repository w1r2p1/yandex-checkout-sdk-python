# -*- coding: utf-8 -*-
import unittest

from yandex_checkout import WebhookNotification, RefundWebhookNotification, WebhookNotificationFactory
from yandex_checkout.domain.response.payment_response import PaymentResponse
from yandex_checkout.domain.response.refund_response import RefundResponse


class TestWebhookNotification(unittest.TestCase):

    def test_notification_payment(self):
        self.maxDiff = None
        notification = WebhookNotification({
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": {
                "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                "status": "waiting_for_capture",
                "paid": True,
                "amount": {
                    "value": "2.00",
                    "currency": "RUB"
                },
                "authorization_details": {
                    "rrn": "10000000000",
                    "auth_code": "000000"
                },
                "created_at": "2018-07-10T14:27:54.691Z",
                "description": "Заказ №72",
                "expires_at": "2018-07-17T14:28:32.484Z",
                "metadata": {},
                "payment_method": {
                    "type": "bank_card",
                    "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                    "saved": False,
                    "card": {
                        "first6": "555555",
                        "last4": "4444",
                        "expiry_month": "07",
                        "expiry_year": "2021",
                        "card_type": "MasterCard",
                        "issuer_country": "RU",
                        "issuer_name": "Sberbank"
                    },
                    "title": "Bank card *4444"
                },
                "refundable": False,
                "test": False
            }
        })

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, PaymentResponse)

        data = {
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": {}
        }

        with self.assertRaises(ValueError):
            WebhookNotification(data)

        data = {
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": 'Invalid object type'
        }

        with self.assertRaises(TypeError):
            WebhookNotification(data)

    def test_notification_refund(self):
        self.maxDiff = None
        notification = RefundWebhookNotification({
            "type": "notification",
            "event": "refund.succeeded",
            "object": {
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'payment_id': '21b23365-000f-500b-9000-070fa3554403',
                'created_at': "2017-11-30T15:11:33+00:00",
                'amount': {
                    "value": 250.0,
                    "currency": "RUB"
                },
                'receipt_registration': 'pending',
                'comment': 'test comment',
                'status': 'pending'
            }
        })

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, RefundResponse)

        data = {
            "type": "notification",
            "event": "refund.succeeded",
            "object": {}
        }

        with self.assertRaises(ValueError):
            RefundWebhookNotification(data)

        data = {
            "type": "notification",
            "event": "refund.succeeded",
            "object": 'Invalid object type'
        }

        with self.assertRaises(TypeError):
            RefundWebhookNotification(data)

    def test_notification_factory(self):
        self.maxDiff = None
        body = {
            "type": "notification",
            "event": "refund.succeeded",
            "object": {
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'payment_id': '21b23365-000f-500b-9000-070fa3554403',
                'created_at': "2017-11-30T15:11:33+00:00",
                'amount': {
                    "value": 250.0,
                    "currency": "RUB"
                },
                'receipt_registration': 'pending',
                'comment': 'test comment',
                'status': 'pending'
            }
        }

        notification = WebhookNotificationFactory().create(body)

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, RefundResponse)

        body = {
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": {
                "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                "status": "waiting_for_capture",
                "paid": True,
                "amount": {
                    "value": "2.00",
                    "currency": "RUB"
                },
                "authorization_details": {
                    "rrn": "10000000000",
                    "auth_code": "000000"
                },
                "created_at": "2018-07-10T14:27:54.691Z",
                "description": "Заказ №72",
                "expires_at": "2018-07-17T14:28:32.484Z",
                "metadata": {},
                "payment_method": {
                    "type": "bank_card",
                    "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                    "saved": False,
                    "card": {
                        "first6": "555555",
                        "last4": "4444",
                        "expiry_month": "07",
                        "expiry_year": "2021",
                        "card_type": "MasterCard",
                        "issuer_country": "RU",
                        "issuer_name": "Sberbank"
                    },
                    "title": "Bank card *4444"
                },
                "refundable": False,
                "test": False
            }
        }

        notification = WebhookNotificationFactory().create(body)

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, PaymentResponse)

        with self.assertRaises(TypeError):
            WebhookNotificationFactory().create('invalid data')

        with self.assertRaises(ValueError):
            WebhookNotificationFactory().create({'invalid': 'data'})
