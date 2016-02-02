#coding=utf-8
from person_finance.models import User_account, Cost_normal_logs, User_DM_account, User_DM_charge_log, Cost_type #@UnresolvedImport
import datetime

def reduceAccount(user,charges):
    account = User_account.objects.get(user = user)
    money_before = account.money
    money_after = account.money - charges
    
    account.money = account.money - charges
    account.modify_time = datetime.datetime.now()
    account.save();
    
    Cost_normal_logs.objects.create(user = user , account = account , cost_type = Cost_type.objects.get(id=2), cost_money = charges,
                                    money_before = money_before, money_after = money_after ,)


def chargeDMAccount(user,charges):
    coins_price_per_rmb = 10
    charges_coins = charges * coins_price_per_rmb
    
    dm_account = User_DM_account.objects.get(user = user)
    coins_before = dm_account.coins
    coins_after = dm_account.coins + charges_coins
    pay_coins_before = dm_account.pay_coins
    pay_coins_after = dm_account.pay_coins + charges_coins
    free_coins_before = dm_account.free_coins
    free_coins_after = dm_account.free_coins
    
    dm_account.coins = coins_after
    dm_account.pay_coins = pay_coins_after
    dm_account.modify_time = datetime.datetime.now()
    dm_account.save()
    
    User_DM_charge_log.objects.create(user = user , coins = charges_coins , coins_before = coins_before, coins_after = coins_after, 
                                      free_coins_before = free_coins_before, free_coins_after = free_coins_after, 
                                      pay_coins_before = pay_coins_before,  pay_coins_after = pay_coins_after,)
    