#coding=utf8
from django.db import connection
from django.core.paginator import PageNotAnInteger, EmptyPage

def executeQuerySql(sql, params):
    cursor = connection.cursor() #获得一个游标(cursor)对象
    cursor.execute(sql, params) #执行SQL
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall() #cursor.fetchone()：返回结果行
    ]
    

from django.core.paginator import Paginator
  
class dcPaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num
  
    def page(self, number):
        self.page_num = number
        return super(dcPaginator, self).page(number)
 
    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)
 
            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list
    page_range_ext = property(_page_range_ext)

def divide_page(lists, page_count, page_num):
    paginator = dcPaginator(lists, page_count)
    try:
        rtn_list = paginator.page(page_num)
    except PageNotAnInteger: 
        rtn_list = paginator.page(1)
    except EmptyPage:
        rtn_list = paginator.page(paginator.num_pages)
    return rtn_list

class Paginator_da(Paginator):
    def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num
  
    def page(self, number):
        self.page_num = number
        return super(Paginator_da, self).page(number)
 
    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)
 
            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list
    page_range_ext = property(_page_range_ext)
