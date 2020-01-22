from haystack import indexes
from .models import News

from django.core.paginator import Paginator

class NewsIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)
    def get_model(self):
        return News
    def index_queryset(self,using=None):
        Newses = self.get_model().objects.order_by('-pub_time').all()
        #根据时间排序，并取出News model所有文件
        return Newses