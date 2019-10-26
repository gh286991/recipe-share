# 美食分享網站

這是一個簡單的Django專案，主要實作會員註冊，登入，登出功能，以及基本的資料庫操作。

![image-20191026235512721](https://i.imgur.com/Ll8LkEN.png)



## 啟動

將此專案clone下來

```sh
$ git clone
```

安裝所需要的套件

```shell
$ pip -r requirements.txt
```

啟動伺服器

```shell
$ python manage.py runserver
```

如果啟動成功，恭喜可以在 `http://localhost:8000/index` 看到頁面🎉。

## 簡介

### 會員功能：

1. 可以註冊新帳號
2. 可以登入，登出

### 主要功能：

1. 登入後可以新增美食
2. 可以修改自己發佈的美食
3. 可以刪除自己發佈的美食
4. 可以看其他人發佈的美食