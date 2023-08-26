# Generated by Django 4.2.3 on 2023-08-26 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("orders", "0002_alter_order_currency_alter_ordertoken_currency"),
    ]

    operations = [
        migrations.CreateModel(
            name="PGDataPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("KCP", "KCP"),
                            ("INICIS", "INICIS"),
                            ("PAYPAL", "PAYPAL"),
                            ("PAYAPP", "PAYAPP"),
                        ],
                        max_length=32,
                        verbose_name="PG 타입",
                    ),
                ),
                ("status", models.CharField(max_length=16, verbose_name="PG 상태")),
                (
                    "vid",
                    models.CharField(
                        max_length=128, verbose_name="PG 고유 거래 번호(결제요청번호)"
                    ),
                ),
                (
                    "method_type",
                    models.CharField(max_length=32, verbose_name="PG 결제 수단"),
                ),
                (
                    "pg_message",
                    models.CharField(max_length=128, verbose_name="PG 메시지(에러시)"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pg_data_payment",
                        to="orders.order",
                        verbose_name="주문",
                    ),
                ),
            ],
            options={"verbose_name": "PG 결제 데이터", "verbose_name_plural": "PG 결제 데이터",},
        ),
        migrations.CreateModel(
            name="PGDataRefund",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("KCP", "KCP"),
                            ("INICIS", "INICIS"),
                            ("PAYPAL", "PAYPAL"),
                            ("PAYAPP", "PAYAPP"),
                        ],
                        max_length=32,
                        verbose_name="PG 타입",
                    ),
                ),
                (
                    "cancel_memo",
                    models.CharField(max_length=128, verbose_name="PG 취소 메모"),
                ),
                ("status", models.CharField(max_length=16, verbose_name="PG 상태")),
                (
                    "pg_message",
                    models.CharField(max_length=128, verbose_name="PG 메시지(에러시)"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pg_data_refund",
                        to="orders.order",
                        verbose_name="주문",
                    ),
                ),
                (
                    "pg_data_payment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payments.pgdatapayment",
                    ),
                ),
            ],
            options={"verbose_name": "PG 환불 데이터", "verbose_name_plural": "PG 환불 데이터",},
        ),
    ]
