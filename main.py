import sys
import orthographic_util

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
    orthographic_list = orthographic_util.get_orthographic_list(ORTHOGRAPHIC_FILE_NAME)
    text = orthographic_util.gettext(args[TARGET_FILE_CMD_INDEX])
    check_result = orthographic_util.check_orthographic(text, orthographic_list)
    orthographic_util.print_result(check_result)
except EnvironmentError:
    print(EnvironmentError)