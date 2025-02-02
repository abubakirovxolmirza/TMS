import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Load

@receiver(post_save, sender=Load)
def send_telegram_message(sender, instance, created, **kwargs):
    if created: 
        bot_token = "7582469651:AAHBtrGUmdo2tzDPU4RSI61AFN99EQnqbJE" 
        channel_id = "@nnt_tms"  

        message = f"""
🚚 #{instance.load_id} :
🔖 Reference ID: {instance.reference_id if instance.reference_id else 'Not Provided'}
👨‍✈️ Driver: {instance.driver if instance.driver else 'Not Assigned'}
Load: #{instance.load_id}  # Haqiqiy Hashtag

Company: {instance.company_name if instance.company_name else 'No company'}
Instructions: {instance.instructions if instance.instructions else 'No instructions'}

Status: {instance.load_status if instance.load_status else 'No status'}
Tags: {instance.tags if instance.tags else 'No tags'}
Equipment: {instance.equipment_type if instance.equipment_type else 'No equipment'}

Pick up: 🏭
{instance.created_date if instance.created_date else 'No date provided'}
Arrive: Date TBD, Time TBD

Estimated Payout: ${instance.load_pay if instance.load_pay else 'TBD'}
Driver Pay: ${instance.driver_pay if instance.driver_pay else 'TBD'}
Total Pay: ${instance.total_pay if instance.total_pay else 'TBD'}

Miles: {instance.mile if instance.mile else 'TBD'}
Empty Miles: {instance.empty_mile if instance.empty_mile else 'TBD'}
Total Miles: {instance.total_miles if instance.total_miles else 'TBD'}

📑 Documents:
- Rate Con: {instance.rate_con.url if instance.rate_con else 'No Rate Con'}
- BOL: {instance.bol.url if instance.bol else 'No BOL'}
- POD: {instance.pod.url if instance.pod else 'No POD'}
- Invoice: {instance.comercial_invoice.url if instance.comercial_invoice else 'No Invoice'}

⚠️ Important:
- Ensure all required documents are uploaded.
- Verify load status regularly.
        """

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": channel_id,
            "text": message,
            "parse_mode": "Markdown" 
        }

        response = requests.post(url, data=data)
        response_data = response.json()

        if response_data.get("ok"):
            instance.message_id = response_data["result"]["message_id"] 
            instance.save() 
        print(response_data)
