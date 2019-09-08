import sys
import orthographic

ORTHOGRAPHIC_FILE_NAME = "orthographic.csv"
TARGET_FILE_CMD_INDEX = 1

# コマンドライン引数を取得
args = sys.argv

# 引数が設定されていなければ終了
if len(args) != 2:
    print("引数を設定してください。")
    sys.exit()

# 揺らぎチェックの実行
try:
    olist = orthographic.readcsv(ORTHOGRAPHIC_FILE_NAME)
    text = orthographic.gettext(args[TARGET_FILE_CMD_INDEX])
    check_result = orthographic.count(text, olist)
    orthographic.pprint(check_result)
except EnvironmentError:
    print(EnvironmentError)