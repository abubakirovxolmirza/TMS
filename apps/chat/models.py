from django.db import models
import requests
from apps.load.models import Load
from apps.auth.models import User

class Chat(models.Model):
    load_id = models.ForeignKey(Load, related_name='LoadChat', on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name='UserChat', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)

            if self.load_id.message_id:   
                bot_token = "7582469651:AAHBtrGUmdo2tzDPU4RSI61AFN99EQnqbJE"
                group_channel_id = "@nnt_tms_chat" 
                message = f"New comment from {self.user.username}: {self.message}"

                url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                data = {
                    "chat_id": group_channel_id,
                    "text": message,
                    "parse_mode": "Markdown",
                    "reply_to_message_id": int(self.load_id.message_id) + 1
                }

                response = requests.post(url, data=data)
                response_data = response.json()

                if response_data.get("ok"):
                    print("Comment added as reply successfully.")
                    self.group_message_id = response_data["result"]["message_id"]
                    self.save()
                else:
                    print(f"Xatolik: {response_data.get('description')}")
                    print("Javob ma'lumotlari:", response_data)
