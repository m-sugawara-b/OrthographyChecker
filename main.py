import sys
import orthographic as og

TARGET_FILE_INDEX = 1
ORTHOGRAPHIC_FILE_INDEX = 2

# コマンドライン引数を取得
args = sys.argv

# 引数が設定されていなければ終了
if len(args) != 3:
    sys.exit()

# 揺らぎチェックの実行
try:
    text = og.gettext(args[TARGET_FILE_INDEX])
    oglist = og.read(args[ORTHOGRAPHIC_FILE_INDEX])
    result = og.wc(text, oglist)
    og.pprint(result)
except Exception as e:
    print(e)