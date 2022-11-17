
# Discord-Translation-BOT
### Discordのスラッシュコマンドに対応した翻訳BOTです。  
基本的にDeepL APIを使用して翻訳されます。  
韓国語から多言語に翻訳する際はPapago APIを使用するようになってます。  
また、多言語から韓国語に翻訳する際もPapago APIを使用しています。  
※BOTのソースコードはすごく雑に書いてあります。  
`ソースコードを綺麗にかける方ぜひコミットお願いします。`
### 動作環境
| OS | Windows 10 |
|:---|:---|
| Python | 3.10.5 |
| discord.py | 2.0.1 |
| discord-ext-ui | 3.1.9 |
| pycord | 2.1.3 |
| deepl | 1.9.0 |
| 最終確認 | 2022/09/07 |

| OS | Ubuntu 20.04 LTS Server |
|:---|:---|
| Python | 3.8.10 |
| discord.py | 2.1.0 |
| discord-ext-ui | 3.1.9 |
| pycord | 2.2.2 |
| deepl | 1.11.0 |
| 最終確認 | 2022/11/17 |

これをぶっこんどけば多分動く  
動かなかったらググってください。  
多分ググったら基本的に解決します。  
`python3 -m pip install -U discord.py`  
`python3 -m pip install -U py-cord`  
`pip install discord-ext-ui`  
`pip install --upgrade deepl`  
↑いらないモジュールもあるかも？


# 事前準備   
> ### Discord BOTの設定   

> リンク：[Discord Developer Portal](https://discord.com/developers/applications)   

`config.yml`を開いて3~4行目にあるDiscord TokenのTokenをご自身で用意してあるトークンに変更してください。
```
# Discord Token
  Token : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
5~6行目にあるDiscord Test_TokenはBOTのテストをする際に使用します。   
使用する場合はTokenをご自身で用意してあるトークンに変更してください。   
```
# Discord Test_Token
  Test_Token : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
その後`bot.py`を開いて424行目にあるトークンを指定する場所に`token`を`Test_Token`に変更して使用してください。
`bot.run(token)`→`bot.run(Test_Token)`   

> ### Papago APIの設定   

> リンク：[애플리케이션 - NAVER Developers](https://developers.naver.com/apps/)   

7~8行目にあるNaver Open API application ID (Papago)はPapago APIを使用する際に使用します。   
ご自身で用意したClient IDを指定してあげてください。   
```
# Naver Open API application ID (Papago)
  client_id : "xxxxxxxxxxxxxxxxxxxx"
```
![image](https://user-images.githubusercontent.com/38372880/202445825-2a9d9d7f-a635-458c-b492-761d0729a910.png)

9~10行目にあるNaver Open API application token (Papago)はPapago APIを使用する際に使用します。   
ご自身で用意したClient Secretを指定してあげてください。   
```
# Naver Open API application token (Papago)
  client_secret : "xxxxxxxxxx"
```
![image](https://user-images.githubusercontent.com/38372880/202446472-c20372a1-415a-4d2e-9fc8-cd470615e8d3.png)

> ### DeepL APIの設定 

> リンク：[DeepLのアカウント](https://www.deepl.com/ja/account/summary)   

11~12行目にあるDeepL API KeyはDeepL APIを使用する際に使用します。   
ご自身で用意したDeepL_Tokenを指定してあげてください。   
```
# DeepL API Key
  DeepL_Token : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
<img width="605" alt="image" src="https://user-images.githubusercontent.com/38372880/202448974-18b47e96-1d3e-4cae-bc21-bc2f6c07e8d6.png">

# 事前準備が終わったら   
> ### bot.pyを実行して終わりです。   
> ### ※すべてPythonなど、モジュールが導入されているのを前提に説明してます。
> ### 　導入方法などは、ご自身で検索して導入してください。
> ### 　導入に必要な物は上に[記載](https://github.com/winning-JP/Discord-Translation-BOT#%E5%8B%95%E4%BD%9C%E7%92%B0%E5%A2%83)してあります。

# コマンド
**日本語から多言語へ翻訳する場合**  
`/ja_en`  
`/ja_cn`  
`/ja_ko`　※Papago API使用  
**英語から多言語へ翻訳する場合**  
`/en_ja`  
`/en_cn`  
`/en_ko`　※Papago API使用  
**中国語から多言語へ翻訳する場合**  
`/cn_ja`  
`/cn_en`  
`/cn_ko`　※Papago API使用  
**韓国語から多言語へ翻訳する場合 ※Papago API使用**  
`/ko_ja`  
`/ko_en`  
`/ko_cn`  
![例](https://user-images.githubusercontent.com/38372880/202450865-a4871a98-9457-47bc-a958-70fca2a0904d.gif)

