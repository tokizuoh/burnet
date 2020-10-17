import sys
import shutil
import os.path
import zipfile
import datetime
import xml.etree.ElementTree as ET


class ArgumentError(Exception):
    def __init__(self, message = "Wrong number of arguments."):
        self.message = message
        super().__init__(self.message)


class FileExtensionNotIpaError(Exception):
    def __init__(self, message = "File extension is not .ipa."):
        self.message = message
        super().__init__(self.message)


def generate_now_time_str():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def extract_dtx_code_build(plist_path):
    tree = ET.parse(plist_path)
    root = tree.getroot()
    isKeyExists = False
    is_before_key_dtx_code_build = False
    ver = ""
    for child in root[0]:
        if child.text == "DTXcodeBuild":
            is_before_key_dtx_code_build = True
            continue
        if is_before_key_dtx_code_build:
            ver = child.text
            break
    return ver

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
    zip_file_path = "{}_{}.{}".format(ipa_path[:-4], generate_now_time_str(), "zip")
    shutil.copyfile(ipa_path, zip_file_path)
    
    # unzip
    with zipfile.ZipFile(zip_file_path) as ez:
        ez.extractall('./')
    
    # extract
    plist_path = './Payload/{}.{}/Info.plist'.format(ipa_path[2:-4], "app")
    xcode_build_version = extract_dtx_code_build(plist_path)
    print(xcode_build_version)