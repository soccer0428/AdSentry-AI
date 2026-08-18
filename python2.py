from datetime import datetime

danger_words = {
    # ダウンロード・更新
    "download": 20,
    "installer": 20,
    "setup": 15,
    "install": 15,
    "update": 20,
    "upgrade": 15,

    # 無料・特典
    "free": 15,
    "gift": 10,
    "bonus": 10,
    "reward": 15,
    "prize": 15,
    "winner": 20,
    "win": 15,
    "campaign": 15,
    "coupon": 10,
    "point": 10,

    # ログイン・認証
    "login": 20,
    "signin": 20,
    "account": 15,
    "verify": 20,
    "verification": 20,
    "confirm": 15,
    "password": 20,
    "security": 20,
    "secure": 10,

    # 警告・ウイルス
    "warning": 20,
    "alert": 20,
    "urgent": 20,
    "virus": 25,
    "scan": 20,
    "repair": 15,
    "fix": 15,
    "clean": 15,

    # サポート詐欺
    "support": 15,
    "help": 10,
    "service": 10,

    # 有名サービスを悪用
    "google": 15,
    "chrome": 15,
    "windows": 15,
    "defender": 20,
    "microsoft": 15,
    "apple": 15,
    "amazon": 15,
    "paypal": 20,
    "bank": 20,

    # ダウンロード誘導
    "start": 10,
    "launch": 10,
    "fast": 10,
    "speed": 10,
    "boost": 15,
    "optimizer": 20,
    "optimize": 15,
    "performance": 10,

    # システム異常を装う
    "detected": 20,
    "infected": 25,
    "critical": 20,
    "risk": 15,
    "error": 15,
    "failed": 15,
    "failure": 15,
    "damaged": 20,
    "corrupted": 20,

    # PC・スマホを狙う
    "android": 15,
    "ios": 15,
    "device": 10,
    "browser": 10,
    "extension": 15,

    # セキュリティを装う
    "firewall": 20,
    "protection": 15,
    "antivirus": 20,
    "cleanup": 20,
    "optimum": 10,

    # 誘導
    "continue": 10,
    "proceed": 10,
    "activate": 15,
    "enable": 15,
    "accept": 10,
    "allow": 15,
    "open": 10,

    # 特典・当選
    "lucky": 15,
    "surprise": 10,
    "congratulations": 20,
    "selected": 15,
    "exclusiveoffer": 20,

    # 金銭関連
    "subscription": 15,
    "purchase": 10,
    "checkout": 10,
    "receipt": 10,

    # その他
    "claim": 15,
    "offer": 10,
    "promo": 10,
    "cash": 10,
    "money": 10,
    "click": 15,
    "redirect": 20,
    "tracking": 10,
    "ads": 10,
    "pop": 10
}

url = input("URLを入力してください: ").lower()

score = 0
found_words = []

# 危険単語の判定
for word, points in danger_words.items():
    if word in url:
        score += points
        found_words.append(word)

# URLの特徴で加点
if len(url) >= 80:
    score += 15

if url.count("-") >= 3:
    score += 10

if sum(c.isdigit() for c in url) >= 5:
    score += 10

if "@" in url:
    score += 30

if url.count("=") >= 3:
    score += 10

if url.count(".") >= 4:
    score += 15

# 怪しいトップレベルドメイン
danger_domains = [
    ".xyz", ".top", ".click", ".live", ".shop",
    ".site", ".online", ".monster", ".buzz"
]

found_domains = []

for domain in danger_domains:
    if domain in url:
        score += 20
        found_domains.append(domain)

# 最大100%
if score > 100:
    score = 100

# 結果表示
print("\n========== 判定結果 ==========")
print("危険度:", score, "%")

if score >= 70:
    print("🚨 高リスク")
elif score >= 40:
    print("⚠️ 注意")
else:
    print("✅ 低リスク")

# 検出単語
if found_words:
    print("\n検出された危険単語")
    for word in found_words:
        print(" -", word)

# 検出ドメイン
if found_domains:
    print("\n検出された怪しいドメイン")
    for domain in found_domains:
        print(" -", domain)

# URLの特徴
print("\nURLの特徴")
print("文字数 :", len(url))
print("ハイフン数 :", url.count("-"))
print("数字の数 :", sum(c.isdigit() for c in url))
print("ドット数 :", url.count("."))

# ===============================
# URLの履歴を保存
# ===============================
with open("url_history.txt", "a", encoding="utf-8") as file:
    file.write(f"日時: {datetime.now()}\n")
    file.write(f"URL: {url}\n")
    file.write(f"危険度: {score}%\n")

    if found_words:
        file.write("検出単語: " + ", ".join(found_words) + "\n")
    else:
        file.write("検出単語: なし\n")

    if found_domains:
        file.write("怪しいドメイン: " + ", ".join(found_domains) + "\n")
    else:
        file.write("怪しいドメイン: なし\n")

    file.write("-" * 40 + "\n")

print("\nURLを『url_history.txt』に保存しました。")