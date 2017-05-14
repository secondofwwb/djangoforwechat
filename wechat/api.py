from wechat.models import Content, icons
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

# 内容序列化
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

# icon序列化据
class iconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = icons
        fields = '__all__'



class contentviewset(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    # serializer_class = ContentSerializer
    http_method_names = ['get']

    # 获取不同类型的文章
    @detail_route(methods=['get'], url_path='contentbytype')
    def contentgetbytype(self, request, pk=None):
        contents = Content.objects.filter(contenttypeid=pk)
        serializers = ContentSerializer(contents, many=True, context={'request': request})
        # 获取传入的参数
        content_num = int(request.query_params['page'])
        page_num = 3 * content_num
        return Response(serializers.data[page_num:3+page_num])

    # 获取单一文章
    @detail_route(methods=['get'], url_path='contentbyid')
    def getcontent(self, request, pk=None):
        content = Content.objects.get(contentid=pk)
        serializer = ContentSerializer(content, context={'request': request})
        return Response(serializer.data)

    # 获取推荐
    @detail_route(methods=['get'], url_path='recimfor')
    def getrecimfor(self, request, pk=None):
        recimfors = Content.objects.filter(recimfor=pk)
        serializer = ContentSerializer(recimfors, many=True, context={'request': request})
        content_num = int(request.query_params['page'])
        page_num = 3 * content_num
        return Response(serializer.data[page_num:3+page_num])

class icons_list_viewset(viewsets.ModelViewSet):
    queryset = icons.objects.all()
    serializer_class = iconsSerializer
    http_method_names = ['get']
