from celery import shared_task

from upload_files.models import File


@shared_task
def upload_file(file_id: int) -> int:
    """В идеале эта функция должна выполнять какую-то бизнес логику."""
    summ = sum(i ** 2 for i in range(10000))
    file_instance = File.objects.get(id=file_id)
    file_instance.processed = True
    file_instance.save()
    return summ
