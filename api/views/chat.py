from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.chat.models import Chat
from api.dto.chat import ChatSerializer

class ChatList(ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetail(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
