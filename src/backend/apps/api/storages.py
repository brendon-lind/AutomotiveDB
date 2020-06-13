from django.conf import settings
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage
# Let's switch from S3 storage to local file storage as needed!
if settings.DEFAULT_FILE_STORAGE == 'storages.backends.s3boto3.S3Boto3Storage':
    class PublicStorage(S3Boto3Storage):
        default_acl = "public-read"
        gzip = True
else:
    class PublicStorage(FileSystemStorage):
        pass
