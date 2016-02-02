#coding=utf8
from django.core.mail.message import EmailMultiAlternatives #@UnresolvedImport
from django.contrib.auth.hashers import make_password, check_password
from person_space.models import User_Secret #@UnresolvedImport
import uuid
from person_finance.models import User_account, User_account_alarm, User_DM_account #@UnresolvedImport


def generate_active_html(username,req_url):
    passwd = make_password(username, None, 'pbkdf2_sha256')
    if(req_url.endswith('/')):
        req_url = req_url[:-1]
    return u'''<b>激活链接：</b><a href="http://%(req_url)s/active_finish/%(u_name)s/%(u_pass)s">点击此链接，完成激活</a>
            <br/> 或复制下面链接在浏览器中访问<br/>http://%(req_url)s/active_finish/%(u_name)s/%(u_pass)s'''  % {'u_name':username, 'u_pass':passwd ,'req_url':req_url }
              
def check_active_url(username,passwd):
    return check_password(username, passwd)

def send_active_email(active_form,user_email):
    subject,form_email,to = u'数据服务平台-激活邮件','zhiaixuexi@126.com',user_email
    text_content = u'数据服务平台-激活邮件'
    html_content = active_form
    msg = EmailMultiAlternatives(subject,text_content,form_email,[to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    
def generateSecret(current_user):
    cur_user_secret = User_Secret.objects.filter(user = current_user)
    if not cur_user_secret.count() > 0:
        uuid_seed = uuid.uuid1()
        cur_open_id = uuid.uuid3( uuid_seed, "open_id_user_%s" % (current_user.id))
        cur_access_Key = uuid.uuid5( uuid_seed, "access_key_user_%s" % (current_user.id))
        User_Secret.objects.create(user=current_user,
                                   open_id=cur_open_id,
                                   access_Key=cur_access_Key);


def generateAccount(current_user):
    account = User_account.objects.create(user=current_user)
    User_account_alarm.objects.create(user=current_user,account = account)
    User_DM_account.objects.create(user=current_user)
    
    
    
