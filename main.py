import sys
import shutil
import os.path
import datetime

class ArgumentError(Exception):
    def __init__(self, message = "Wrong number of arguments."):
        self.message = message
        super().__init__(self.message)


class FileExtensionNotIpaError(Exception):
    def __init__(self, message = "File extension is not .ipa."):
        self.message = message
        super().__init__(self.message)

def get_now_time_str():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


if __name__ == '__main__':
    # コマンドライン引数取得
    args = sys.argv
    if len(args) != 2:
        raise ArgumentError

    # コマンドライン引数の2つ目の末尾が.ipaであることを確認
    ipa_path = args[1]
    if (ext := (_ := os.path.splitext(ipa_path))[1]) != ".ipa":
        raise FileExtensionNotIpaError

    # ipaファイルの存在確認
    if not os.path.exists(ipa_path):
        raise FileNotFoundError(ipa_path)

    # ipaファイルをコピーし、zipに変換
    after_copying_file_path = "{}_{}.{}".format(ipa_path[:-4], get_now_time_str(), "zip")
    shutil.copyfile(ipa_path, after_copying_file_path)
    