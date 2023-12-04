from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer


@api_view(["GET", "POST", "PUT"])
def index(request):
    courses = {
        "course_name": "Python",
        "learn": ["Flask", "Django", "FastApi"],
        "course_provider": "Scalar",
    }

    if request.method == "GET":
        print(request.GET.get("search"))
        return Response(courses)
    elif request.method == "POST":
        data = request.data
        print(data)
        return Response(data)


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def person(request):
    if request.method == "GET":
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "PUT":
        data = request.data
        obj = Person.objects.get(id=data["id"])
        serializer = PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id=data["id"])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        data = request.data
        obj = Person.objects.get(id=data["id"])
        obj.delete()
        return Response({"message": "person deleted"})
