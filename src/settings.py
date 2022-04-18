import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

# ".env"があるディレクトリのパスの取得, dotenvに設定
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path=dotenv_path)

# TOKENに".env"で設定していたTOKEN内容を代入
TOKEN = os.environ.get("TOKEN")
