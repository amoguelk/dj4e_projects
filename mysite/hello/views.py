from django.http import HttpResponse

def helloView(request):
    visits = request.session.get('visits', 0) + 1
    request.session['visits'] = visits
    if visits > 4: del(request.session['visits'])
    resp = HttpResponse('view count=' + str(visits))
    resp.set_cookie('dj4e_cookie', '410e7a82', max_age=1000)
    return resp
