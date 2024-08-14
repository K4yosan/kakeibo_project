from django.conf import settings
from django.urls import path, include
from . import views

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('', views.index, name='index'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('delete_income/<int:income_id>/', views.delete_income, name='delete_income'),  # 新しいURLパターン
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('stats/', views.stats_view, name='stats_view'),
]

# DEBUGモード時にのみdebug_toolbarのURLを追加
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]