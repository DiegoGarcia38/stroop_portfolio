from storages.backends.s3boto3 import S3Boto3Storage
from botocore.exceptions import ClientError


class R2Storage(S3Boto3Storage):
    file_overwrite = False

    def exists(self, name):
        try:
            return super().exists(name)
        except ClientError:
            return False


class CustomStorage(R2Storage):
    location = 'uploads'