import os
import yadisk


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_files_from_folder(self) -> list:
        """Метод получает списк файлов из каталога по пути self.file_path и возвращает список файлов для дальнейшей работы"""
        file_list = os.listdir(self.file_path)
        return file_list

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        file_list = self._get_files_from_folder()
        file_path = self.file_path
        y = yadisk.YaDisk(token="")
        y.mkdir(file_path)
        for file in file_list:
            y.upload(f'{file_path}/{file}', f'{file_path}/{file}')
        return

    def create_folder(self):
        """метод создает папку на яндекс.диске с таким же именем как и в self.file_path"""
        file_path = self.file_path
        y = yadisk.YaDisk(token="")
        y.mkdir(file_path)


if __name__ == '__main__':
    uploader = YaUploader('files')
    result = uploader.upload()
