from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.management import call_command

@api_view(['GET'])
def home(request):
    
    call_command('test_check')
    f = open("file.txt", "a")
    f.write(str(request.data))
    f.close()

    #open and read the file after the appending:
    f = open("file.txt", "r")
    data=f.read()
    f.close()
    return HttpResponse(data)

