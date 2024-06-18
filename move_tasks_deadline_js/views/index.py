from django.shortcuts import render
from ..utils.is_handler_bound import is_bound
from django.views.decorators.csrf import requires_csrf_token
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def index(request):
    """Страница из списка с приложениями, на которой можно привязать
    хендлер к окну просмотра задачи"""
    bound = {}
    for handler_type in ["js", "admin", "self"]:
        bound[handler_type] = is_bound(request.bitrix_user_token, handler_type)

    return render(request, 'move_tasks_deadline_js/index.html', {
        "bound": bound
    })
