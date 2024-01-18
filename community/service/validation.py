from functools import wraps
from typing import Type
from django.http import JsonResponse
from rest_framework import status
from community.domain.categories import PostCategories
from pydantic import BaseModel, Field

from community.service.define import PostCategoriesParam, PostSearchFilterParam, PostSortCategoryParam

"""validator에 사용되는 임시 model class"""


# post view 에 들어오는 query_param을 validate 하기위한 임의의 model
class PostQueryParam(BaseModel):
    page: int = Field(default=1, ge=1)
    category: PostCategoriesParam = Field(default=PostCategoriesParam.ENG_QUESTION)
    search_filter: PostSearchFilterParam = Field(default=PostSearchFilterParam.TOTAL)
    q: str = Field(default=None)
    sort: PostSortCategoryParam = Field(default=PostSortCategoryParam.CREATE_AT)


class PostPathParam(BaseModel):
    post_id: int = Field(ge=0)


"""validator 모음"""


def login_required(view_func):
    """
        <설명>
        로그인을 하지않은 유저를 제한하고 401 response를 return 한다.
    """

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse(message={"error": "Authentication required"},
                                status=status.HTTP_401_UNAUTHORIZED)
        return view_func(request, *args, **kwargs)

    return wrapper


def restrict_post_create_permission(service_func):
    """
        <설명>
        staff 권한 이상이 아닌 user가 notice_board에 접근시 제한한다.
    """

    @wraps(service_func)
    def wrapper(*args, **kwargs):
        request = args[1]
        category = request.data.get('category')  # json body내에서 category를 찾는다.
        if category == PostCategories.NOTICE:
            user = request.user
            if not (user.is_superuser or user.is_staff):
                return JsonResponse(message={'message': 'Permission Denied'},
                                    status=status.HTTP_403_FORBIDDEN)
            else:
                # 만약 카테고리가 notice_board가 아니거나 notice_board지만 user가 staff이상이라면 view 엑세스
                return service_func(*args, **kwargs)

    return wrapper


# query_param validator
def validate_query_params(model: Type[BaseModel]):
    """
        <설명>
        정의된 query_param model 외의 query param 들은 모두 무시한다.
        validated_query_params에 validation한 param을 넘겨준다.
    """

    def decorated_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            request = args[1]
            params = request.GET.dict()
            try:
                validated_params = model.model_validate(params)
            except ValueError as e:
                return JsonResponse(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"message": str(e)}
                )
            return f(*args, **kwargs, validated_query_params=validated_params)

        return wrapper

    return decorated_func


# path_param validator
def validate_path_params(model: Type[BaseModel]):
    """
        <설명>
        만약 path_param이 없을시 넘어간다.
        잘못된 path_param일시 400 response를 return 한다.
    """

    def decorated_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):  # url 캡처후 view로 보내주는 path_params 은 kwargs로 넘겨준다.
            if kwargs:
                try:
                    model(**kwargs)
                except ValueError as e:
                    return JsonResponse(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={"message": str(e)},
                    )

            return f(*args, **kwargs)

        return wrapper

    return decorated_func


