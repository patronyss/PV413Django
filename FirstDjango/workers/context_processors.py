from workers.models import Worker


def workers_count(request):
    context = {
        'workers_count': Worker.objects.count()
    }

    return context
