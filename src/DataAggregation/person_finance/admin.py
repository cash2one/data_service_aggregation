from django.contrib import admin #@UnusedImport
from models import Bank_account_info,Alipay_account_info
#Charge_type, DM_Charge_type, Cost_type, DM_Cost_type

#User_account, Charge_logs, Cost_logs

# Register your models here.
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name','company_name','account','score')
admin.site.register(Bank_account_info, BankAccountAdmin)

class AlipayAccountAdmin(admin.ModelAdmin):
    list_display = ('company_name','account','score')
admin.site.register(Alipay_account_info, AlipayAccountAdmin)

#admin.site.register(Charge_type)
#admin.site.register(DM_Charge_type)
#admin.site.register(Cost_type)
#admin.site.register(DM_Cost_type)
#admin.site.register(User_account)
#admin.site.register(Charge_logs)
#admin.site.register(Cost_logs)