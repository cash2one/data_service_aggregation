#coding=utf-8
from person_finance.models import User_account, Cost_normal_logs #@UnresolvedImport
from person_space.models import User_Secret #@UnresolvedImport


def get_user_by_openid( openid ):
    User_Secret.objects.all();
    return None


def reduce_balance(user, service):
    User_account.objects.all();
    return None


def record_log(user, service):
    Cost_normal_logs.objects.all();
    return None