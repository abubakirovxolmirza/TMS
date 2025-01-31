from django.db import models
import requests
from apps.load.models import Load
from apps.auth.models import User

class Chat(models.Model):
    load_id = models.ForeignKey(Load, related_name='LoadChat', on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name='UserChat', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Yangi chat saqlanayotganini tekshirish
        if not self.pk:
            super().save(*args, **kwargs)

            # Telegram bot orqali xabar yuborish
            if self.load_id.message_id:  # Yuborilgan Load xabarining message_id si bo'lsa
                bot_token = "7582469651:AAHBtrGUmdo2tzDPU4RSI61AFN99EQnqbJE"
                group_channel_id = "@nnt_tms_chat"  # Guruh username
                message = f"New comment from {self.user.username}: {self.message}"

                # Kommentariyani yuborish (reply_to_message_id parametrini qo'shish)
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                data = {
                    "chat_id": group_channel_id,  # Guruh ID sini ishlatamiz
                    "text": message,
                    "parse_mode": "Markdown",
                    "reply_to_message_id": self.load_id.message_id  # Xabarga javob sifatida yuborish
                }

                # Xabarni yuborish
                response = requests.post(url, data=data)
                response_data = response.json()

                if response_data.get("ok"):
                    print("Comment added as reply successfully.")
                    # Guruhdagi xabar uchun message_id ni saqlash
                    self.group_message_id = response_data["result"]["message_id"]
                    self.save()  # message_id ni saqlash
                else:
                    print(f"Xatolik: {response_data.get('description')}")
                    print("Javob ma'lumotlari:", response_data)