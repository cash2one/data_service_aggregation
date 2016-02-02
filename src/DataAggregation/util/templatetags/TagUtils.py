#coding=utf8
from django.utils.encoding import force_unicode
import re
from django import template

register = template.Library()

@register.filter(name='substr')
def do_substr(s,num,end_text='...'):
    out = s[0:int(num)]
    if len(s) > 50:
        out += end_text
    return out

@register.filter('range')
def do_range(value):
    return range(1, value+1)


@register.filter('abs')
def do_minus(value):
    return abs(value)

##################################################################################
#截取字符工具,不保留html
##################################################################################
@register.filter(name='truncateCHwords')
def truncatewords(s,num,end_text='...'):

    re_tag= re.compile(r'<(/)?([^ ]+?)(?: (/)| .*?)?>')
    re_words = re.compile(u'(&.*?;)|[\u4e00-\u9fa5]{1}|[^\u4e00-\u9fa5]{1}',re.UNICODE)
    
    s = force_unicode(s)

    length=int(num) 

    if length<=0:
        return u''
    
    pos = 0
    words=0
    data=[]
    out='' #@UnusedVariable
    current_word = ''
    while words <= length:
        if words==length:
            break

        #查找第一个标签结束的>
        m= re_tag.search(s,pos)
        if not m:
            break
        pos = m.end()

        #开始从这个位置向后搜索字符,匹配到第一个字符，停止，检查,如果字符是<,说明匹配到了html标签了,则跳出去,否则开始检查下一个标签的>
        while words <= length:
            if words==length:
                break
            m = re_words.search(s,pos)   
            if not m:
                break
            current_word = m.group()
            if current_word=='<':
                break
            else:
                if not m.group(1):
                    words+=1
                    data.append(str(m.group()))
                    pos+=1
                else:
                    words+=1
                    data.append(str(m.group()))
                    pos=m.end()

    out = ''.join(data)

    out+=end_text
    return out

##################################################################################
#截取字符工具，保留html
##################################################################################
@register.filter(name='truncateCHwordshtml')
def truncatewords_html(s,num,end_text='...'):
    
    html4_singlets = ('br', 'col', 'link', 'base', 'img', 'param', 'area', 'hr', 'input')
    re_tag= re.compile(r'<(/)?([^ ]+?)(?: (/)| .*?)?>')
    re_words = re.compile(u'(&.*?;)|[\u4e00-\u9fa5]{1}|[^\u4e00-\u9fa5]{1}',re.UNICODE)
    
    s = force_unicode(s)
    
    
    length=int(num)
    
    if length<=0:
        return u''
    
    pos = 0
    words=0
    current_word = ''
    open_tags=[]
    while words <= length:
        if words==length:
            break

        #查找第一个标签结束的>
        m= re_tag.search(s,pos)
        if not m:
            break
        pos = m.end()
        closing_tag,tagname,self_closing=m.groups()
        
        #自关闭标签不处理,或者是单标签
        if self_closing or tagname in html4_singlets:
            pass
        elif closing_tag:
            # Check for match in open tags list
            try:
                i = open_tags.index(tagname) #@UnusedVariable
            except ValueError:
                pass
            else:
                #移除该标签，说明该标签已经闭合
                open_tags.remove(tagname)
        else:
            #把标签加入到仍然打开的标签中
            open_tags.insert(0, tagname)
            
        #开始从这个位置向后搜索字符,匹配到第一个字符，停止，检查,如果字符是<则跳出去,否则开始检查下一个标签的>
        while words <= length:
            
            if words==length:
                break
            m = re_words.search(s,pos)
            if not m:
                break
            current_word = m.group()
            if current_word=='<':
                break
            else:
                if not m.group(1):
                    words+=1
                    pos+=1
                else:
                    words+=1
                    pos=m.end()
    #如果本身的大小就不够，则不加结尾
    if pos==len(s):
        return s
    out = s[:pos]
    if end_text:
        out += ' ' + end_text
    # Close any tags still open
    for tag in open_tags:
        out += '</%s>' % tag

    # Return string
    return out
