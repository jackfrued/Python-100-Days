## RESTful架构和DRF进阶

除了上一节讲到的方法，使用DRF创建REST风格的数据接口也可以通过CBV（基于类的视图）的方式。使用CBV创建数据接口的特点是代码简单，开发效率高，但是没有FBV（基于函数的视图）灵活，因为使用FBV的方式，数据接口对应的视图函数执行什么样的代码以及返回什么的数据是高度可定制的。下面我们以定制学科的数据接口为例，讲解通过CBV方式定制数据接口的具体做法。

### 使用CBV

#### 继承APIView的子类

修改之前项目中的`polls/views.py`，去掉`show_subjects`视图函数，添加一个名为`SubjectView`的类，该类继承自`ListAPIView`，`ListAPIView`能接收GET请求，它封装了获取数据列表并返回JSON数据的`get`方法。`ListAPIView`是`APIView` 的子类，`APIView`还有很多的子类，例如`CreateAPIView`可以支持POST请求，`UpdateAPIView`可以支持PUT和PATCH请求，`DestoryAPIView`可以支持DELETE请求。`SubjectView` 的代码如下所示。

```Python
from rest_framework.generics import ListAPIView


class SubjectView(ListAPIView):
    # 通过queryset指定如何获取学科数据
    queryset = Subject.objects.all()
    # 通过serializer_class指定如何序列化学科数据
    serializer_class = SubjectSerializer
```

刚才说过，由于`SubjectView`的父类`ListAPIView`已经实现了`get`方法来处理获取学科列表的GET请求，所以我们只需要声明如何获取学科数据以及如何序列化学科数据，前者用`queryset`属性指定，后者用`serializer_class`属性指定。要使用上面的`SubjectView`，需要修改`urls.py`文件，如下所示。

```Python
urlpatterns = [
    path('api/subjects/', SubjectView.as_view()),   
]
```

很显然，上面的做法较之之前讲到的FBV要简单很多。

#### 继承ModelViewSet

如果学科对应的数据接口需要支持GET、POST、PUT、PATCH、DELETE请求来支持对学科资源的获取、新增、更新、删除操作，更为简单的做法是继承`ModelViewSet`来编写学科视图类。再次修改`polls/views.py`文件，去掉`SubjectView`类，添加一个名为`SubjectViewSet`的类，代码如下所示。

```Python
from rest_framework.viewsets import ModelViewSet


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
```

通过查看`ModelViewSet`类的源代码可以发现，该类共有6个父类，其中前5个父类分别实现对POST（新增学科）、GET（获取指定学科）、PUT/PATCH（更新学科）、DELETE（删除学科）和GET（获取学科列表）操作的支持，对应的方法分别是`create`、`retrieve`、`update`、`destroy`和`list`。由于`ModelViewSet`的父类中已经实现了这些方法，所以我们几乎没有编写任何代码就完成了学科数据全套接口的开发，我们要做的仅仅是指出如何获取到数据（通过`queryset`属性指定）以及如何序列化数据（通过`serializer_class`属性指定），这一点跟上面继承`APIView`的子类做法是一致的。

```Python
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
```

要使用上面的`SubjectViewSet`，需要在`urls.py`文件中进行URL映射。由于`ModelViewSet`相当于是多个视图函数的汇总，所以不同于之前映射URL的方式，我们需要先创建一个路由器并通过它注册`SubjectViewSet`，然后将注册成功后生成的URL一并添加到`urlspattern`列表中，代码如下所示。

```Python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/subjects', SubjectViewSet)
urlpatterns += router.urls
```

除了`ModelViewSet`类外，DRF还提供了一个名为`ReadOnlyModelViewSet` 的类，从名字上就可以看出，该类是只读视图的集合，也就意味着，继承该类定制的数据接口只能支持GET请求，也就是获取单个资源和资源列表的请求。

### 数据分页

在使用GET请求获取资源列表时，我们通常不会一次性的加载所有的数据，除非数据量真的很小。大多数获取资源列表的操作都支持数据分页展示，也就说我们可以通过指定页码（或类似于页码的标识）和页面大小（一次加载多少条数据）来获取不同的数据。我们可以通过对`QuerySet`对象的切片操作来实现分页，也可以利用Django框架封装的`Paginator`和`Page`对象来实现分页。使用DRF时，可以在Django配置文件中修改`REST_FRAMEWORK`并配置默认的分页类和页面大小来实现分页，如下所示。

```Python
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
}
```

除了上面配置的`PageNumberPagination`分页器之外，DRF还提供了`LimitOffsetPagination`和`CursorPagination`分页器，值得一提的是`CursorPagination`，它可以避免使用页码分页时暴露网站的数据体量，有兴趣的读者可以自行了解。如果不希望使用配置文件中默认的分页设定，可以在视图类中添加一个`pagination_class`属性来重新指定分页器，通常可以将该属性指定为自定义的分页器，如下所示。

```Python
from rest_framework.pagination import PageNumberPagination


class CustomizedPagination(PageNumberPagination):
    # 默认页面大小
    page_size = 5
    # 页面大小对应的查询参数
    page_size_query_param = 'size'
    # 页面大小的最大值
    max_page_size = 50
```

```Python
class SubjectView(ListAPIView):
    # 指定如何获取数据
    queryset = Subject.objects.all()
    # 指定如何序列化数据
    serializer_class = SubjectSerializer
    # 指定如何分页
    pagination_class = CustomizedPagination
```

如果不希望数据分页，可以将`pagination_class`属性设置为`None`来取消默认的分页器。

### 数据筛选

如果希望使用CBV定制获取老师信息的数据接口，也可以通过继承`ListAPIView`来实现。但是因为要通过指定的学科来获取对应的老师信息，因此需要对老师数据进行筛选而不是直接获取所有老师的数据。如果想从请求中获取学科编号并通过学科编号对老师进行筛选，可以通过重写`get_queryset`方法来做到，代码如下所示。

```Python
class TeacherView(ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.defer('subject')
        try:
            sno = self.request.GET.get('sno', '')
            queryset = queryset.filter(subject__no=sno)
            return queryset
        except ValueError:
            raise Http404('No teachers found.')
```

除了上述方式之外，还可以使用三方库`django-filter`来配合DRF实现对数据的筛选，使用`django-filter`后，可以通过为视图类配置`filter-backends`属性并指定使用`DjangoFilterBackend`来支持数据筛选。在完成上述配置后，可以使用`filter_fields` 属性或`filterset_class`属性来指定如何筛选数据，有兴趣的读者可以自行研究。