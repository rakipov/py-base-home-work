import os
import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_files_from_folder(self) -> list:
        """Метод получает список файлов из каталога по пути self.file_path и возвращает список файлов для дальнейшей работы"""
        file_list = os.listdir(self.file_path)
        return file_list

    def upload(self):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_list = self._get_files_from_folder()
        file_path = self.file_path
        api_token = ''
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'{api_token}'}
        for file in file_list:
            params = {'path': f'{file_path}/{file}'}
            get_upload_url = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload/', headers=headers, params=params)
            get_url = get_upload_url.json()
            upload_url = get_url['href']
            file_upload = requests.api.put(upload_url, data=open(f'{file_path}/{file}', 'rb'), headers=headers)
            status = file_upload.status_code
        if 500 > status != 400:
            print('Файлы успешно загружены')
        else:
            print('Ошибка при загрузке')
        return status

    def create_folder(self):
        """Метод создает папку на яндекс.диске с таким же именем как и в self.file_path"""
        file_path = self.file_path
        api_token = ''
        mkdir_url = f'https://cloud-api.yandex.net:443/v1/disk/resources?path={file_path}'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'{api_token}'}
        create_dir = requests.api.put(mkdir_url, headers=headers)


if __name__ == '__main__':
    uploader = YaUploader('files')
    result = uploader.upload()