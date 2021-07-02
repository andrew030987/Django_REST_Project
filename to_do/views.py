from rest_framework import generics, permissions
from to_do.serializers import BoardListAPIViewSerializer, BoardCreateAPIViewSerializer, TodoListAPIViewSerializer
from to_do.models import Board, ToDoList
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


class TodoCreateApiView(generics.CreateAPIView):
    """
    API to create a new task for the board
    permission: - Admin
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]
    queryset = ToDoList.objects.all()


class TodoListApiView(generics.ListAPIView):
    """
    API to get list of all todos for boards
    to perform: - use board row id
    permissions: for all Authenticated
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        queryset = ToDoList.objects.filter(board=self.kwargs['board'])


class TodoListUnDoneApiView(generics.ListAPIView):
    """
    API to get list of all undone todos for boards
    to perform: - use board row Id
    permission: - for all authenticated
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        queryset = ToDoList.objects.filter(board=self.kwargs['board']).filter(done=False)
        return queryset


class TodoDeleteApiView(generics.DestroyAPIView):
    """
    API to delete todos
    use todolist row id
    permission: - admin only
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = ToDoList.objects.all()


class IsOwnerOrAdminPermission(permissions.BasePermission):
    """
    Check if object owner or staff
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class TodoUpdateApiView(generics.RetrieveUpdateAPIView):
    """"
    API to update todos
    use - todo_list row Id
    permission: - object owner or admin
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [IsOwnerOrAdminPermission, ]
    queryset = ToDoList.objects.all()
