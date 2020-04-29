from django.urls import path

from apps.employee_register.views import employee_list, employee_delete, employee_form

urlpatterns = [
    # get and post req. for insert operation
    path('form', employee_form, name='employee_insert'),

    # get and post req. for update operation
    path('<int:id>/', employee_form, name='employee_update'),

    path('delete/<int:id>/',employee_delete, name='employee_delete'),

    # get req. to retrieve and display all records
    path('list/', employee_list, name='employee_list')
]
