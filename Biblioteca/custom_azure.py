from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name = os.getenv('ACCOUNT_NAME_AZURE')
    account_key = 'nY/rsHD+qGQPs5pLk7592uI380tAx1C1tHliTTP1v2fdmNQv7TEr/vOLylJ5LBjfk7d2/z8QHscfWDdU7+lbbw=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = os.getenv('ACCOUNT_NAME_AZURE') 
    account_key = os.getenv('ACCOUNT_KEY_AZURE')
    azure_container = 'static'
    expiration_secs = None