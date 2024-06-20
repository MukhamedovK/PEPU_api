from rest_framework import status


def get_template(request, modelName, serializerName):
    queryset = modelName.objects.all()
    serializer = serializerName(queryset, many=True)
    return serializer.data


def get_one_template(request, modelName, serializerName, pk):
    queryset = modelName.objects.get(id=pk)
    serializer = serializerName(queryset)
    return serializer.data


def post_template(request, serializerName):
    serializer = serializerName(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return ({"data": serializer.data}, status.HTTP_201_CREATED)
    return ({"error": serializer.errors}, status.HTTP_204_NO_CONTENT)


def put_template(request, modelName, serializerName, pk):
    if not modelName.objects.filter(id=pk).exists():
        return ({"error": "Data does not exists!"}, status.HTTP_204_NO_CONTENT)

    instance = modelName.objects.get(id=pk)
    serializer = serializerName(data=request.data)
    if serializer.is_valid():
        serializer.update(instance, serializer.validated_data)
        return (
            {f"data": serializer.data},
            status.HTTP_205_RESET_CONTENT,
        )

    return (serializer.errors, status.HTTP_400_BAD_REQUEST)


def delete_template(request, modelName, pk):
    if not modelName.objects.filter(id=pk).exists():
        return ({"error": "Data does not exists!"}, status.HTTP_204_NO_CONTENT)

    modelName.objects.get(id=pk).delete()
    return ({"data": f"Deleted data by id [{pk}]"}, status.HTTP_418_IM_A_TEAPOT)