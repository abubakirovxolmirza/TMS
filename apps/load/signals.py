import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Load  # Предполагается, что модель называется "Загрузить"

@receiver(post_save, sender=Load)
def send_telegram_message(sender, instance, created, **kwargs):
    if created:
        bot_token = "7582469651:AAHBtrGUmdo2tzDPU4RSI61AFN99EQnqbJE"
        channel_id = "@nnt_tms"  # Оригинальный канал
        group_chat_id = "-1002261791758"  # Замените на реальный ID группы каналов (например, -100123456789)

        message = f"""
🚚 #{instance.load_id}
🔖 Идентификатор ссылки: {instance.reference_id if instance.reference_id else 'Не указано'}
👨‍✈️ Водитель: {instance.driver if instance.driver else 'Не назначен'}
Загрузка: #{instance.load_id} # Фактический хэштег

Компания: {instance.company_name if instance.company_name else 'Нет компании'}
Инструкции: {instance.instructions if instance.instructions else 'Нет инструкций'}

Статус: {instance.load_status if instance.load_status else 'Нет статуса'}
Теги: {instance.tags if instance.tags else 'Нет тегов'}
Оборудование: {instance.equipment_type if instance.equipment_type else 'Нет оборудования'}

Подобрать: 🏭
{instance.created_date if instance.created_date else 'Дата не указана'}
Приезжать: Дата будет объявлена позже, время будет объявлено позже

Предполагаемая выплата: ${instance.load_pay if instance.load_pay else 'TBD'}
Оплата труда водителя: ${instance.driver_pay if instance.driver_pay else 'TBD'}
Общая заработная плата: ${instance.total_pay if instance.total_pay else 'TBD'}

Мили: {instance.mile if instance.mile else 'TBD'}
Пустые мили: {instance.empty_mile if instance.empty_mile else 'TBD'}
Всего миль: {instance.total_miles if instance.total_miles else 'TBD'}

📑 Документы:
- Оценить минус: {instance.rate_con.url if instance.rate_con else 'Нет тарифа Con'}
- МЯЧ: {instance.bol.url if instance.bol else 'Нет BOL'}
- ПОД: {instance.pod.url if instance.pod else 'Нет POD'}
- Счет: {instance.comercial_invoice.url if instance.comercial_invoice else 'Нет счета'}

⚠️ Важно:
- Убедитесь, что все необходимые документы загружены.
- Регулярно проверяйте состояние груза.
        """

        # Отправка в группу каналов
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": group_chat_id,  # Отправляем в группу каналов
            "text": message,
            "parse_mode": "Markdown"
        }

        response = requests.post(url, data=data)
        response_data = response.json()

        if response_data.get("ok"):
            # Сохраняем message_id из группы каналов
            instance.message_id = response_data["result"]["message_id"]
            instance.save()
            print(f"Сообщение отправлено в группу каналов, message_id: {instance.message_id}")
        else:
            print(f"Ошибка отправки в группу каналов: {response_data}")

        # Опционально: отправка в оригинальный канал (если нужно)
        data["chat_id"] = channel_id  # Меняем chat_id на канал
        channel_response = requests.post(url, data=data)
        channel_response_data = channel_response.json()

        if channel_response_data.get("ok"):
            print(f"Сообщение отправлено в канал {channel_id}")
        else:
            print(f"Ошибка отправки в канал: {channel_response_data}")