from django.http import JsonResponse

def getRoute(request):
    routes=[
        {
            'name':'Geo Thomas',
            'age':'23',
            'place':'Kottayam'
        },
        {
            'name':'Manuel Rober',
            'age':'23',
            'place':'Eranakulam'
        },
        {
            'name':'Joseph John',
            'age':'23',
            'place':'Kottayam'
        },

    ]
    return JsonResponse(routes,safe=False)