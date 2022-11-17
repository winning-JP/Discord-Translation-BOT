
# Discord-Translation-BOT
スラッシュコマンドに対応した翻訳BOT
### 動作環境
| OS | Windows 10 |
|:---|:---|
| Python | 3.10.5 |
| discord.py | 2.0.1 |
| discord-ext-ui | 3.1.9 |
| pycord | 2.1.3 |
| deepl | 1.9.0 |

| OS | Ubuntu 20.04 LTS Server |
|:---|:---|
| Python | 3.8.10 |
| discord.py | 2.0.1 |
| discord-ext-ui | 3.1.9 |
| pycord | 2.1.3 |
| deepl | 1.9.0 |

これをぶっこんどけば多分動く  
動かなかったらググってください。  
ググったら基本的に解決します。  
`python3 -m pip install -U discord.py`  
`python3 -m pip install -U py-cord`  
`pip install discord-ext-ui`  
`pip install --upgrade deepl`  
↑いらないモジュールもあるかも？


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
