while True:
    print('あなたはだれ？')
    name = input()
    if name != 'Joe':
        continue
    print('こんにちわJoe。パスワードは何？（魚の名前）')
    password = input()
    if password == 'fish':
        break
print('認証しました。')
