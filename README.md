# GrammerChecker
基本的に自分用に作っているので、コミット履歴などがめちゃくちゃですが、ご了承ください。

## 1. 表記揺れチェック
ogcheckは文章中の表記揺れをチェックするプログラムです。<br>
やっていること自体はシンプルで、事前にCSVに表記揺れを記述しておき、チェック対象の文中にその揺れがいくつあるかカウントするというものです。

### 使い方

***1. 事前にCSVにチェックしたい表記揺れを記述しておく***

例として、次のようなCSVを作成して、任意のフォルダに保存します。<br>
```
おれ、俺
わたし、私
国際連合、国連、UN
```
<br>

***2. チェックしたいテキストファイルを用意***

例として、次のようなテキストファイルを用意します。
```
おれは猫である。俺にはまだ名前がない。
```
<br>

***3. コマンドラインから実行***

最後に、コマンドラインで次のように実行します。
```
python ogcheck.py "チェック対象のパス" "表記揺れCSVのパス"`
```
すると、下記のような結果が得られます。<br>
テキストファイルには、「おれ」という単語が１つ、「俺」という単語が１つあり、つまり表記揺れがあることがわかります。
```
{'おれ' : 1 , '俺' : 1}
```

<br>

### 背景
業種や業界によって、やたらと文書の表記揺れなどに厳しい会社があると思います。
毎回、人の手を借りて目視で確認するのは非効率だと思い、このような形でプログラムにしてみました。
このような形にしておけば、どのような表記揺れがあるかをCSVに知見として確実に積むことができます。失敗を確実に財産として蓄積していくことができるのです。また、表記揺れチェックが自動化されるので工数の削減にもつながります。

いちおう、この手のプログラムはウェブサイトにも存在しますが、機密性の高い文書などのチェックをするときに、なんとなく後ろめたい気持ちがあると思い、ローカルで実行するプログラムを作成しました。（とはいえ、その手のウェブサイトの処理はクライアント側で行なっているとは思いますが）

