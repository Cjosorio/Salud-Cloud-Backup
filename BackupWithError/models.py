from django.db import models


class BackupWithError(models.Model):
    id = models.AutoField(primary_key=True)
    backup_id = models.CharField(max_length=100)
    error_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.backup_id

