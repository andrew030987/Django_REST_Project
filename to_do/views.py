from rest_framework import generics, permissions
from to_do.serializers import BoardListAPIViewSerializer, BoardCreateAPIViewSerializer
from to_do.models import Board
from django.db.models import Count


class BoardListAPIView(generics.ListAPIView):
    """
    API to get all Boards with counts from To_do_list for each board
    permission: - Is Authenticated
    """
    serializer_class = BoardListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Board.objects.annotate(count=Count('todolist__board'))
        return queryset


class BoardCreateAPIView(generics.CreateAPIView):
    """
    API to create new Board
    permission: - Admin
    """
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser]


class BoardUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API to update/delete Board
    use row Id to execute
    permission: - Admin
    """
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Board.objects.all()


