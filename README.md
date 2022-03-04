# 1102_SDM_HW2


https://user-images.githubusercontent.com/31082466/156895456-493d4e30-c884-495a-93cd-526c0b931a90.mov



確定電腦有安裝 `python3` 以及完成上述資料匯入資料庫的指令後打開終端機執行以下指令：

```shell
# for mac
cd backend
python3 -m venv virtual-env #建立虛擬環境 #-m: module-name
source tutorial-env/bin/activate #啟動虛擬環境 for mac
```

```shell
# for windows
cd backend
python3 -m venv virtual-env #建立虛擬環境 #-m: module-name
tutorial-env\Scripts\activate.bat #啟動虛擬環境 for windows
```

成功的話，command prompt 前面應該會多出 `(virtual-env)` 的字樣，代表已經進入這個虛擬環境。如果未來你想退出這個虛擬環境，可以輸入 `deactivate`。
接著下載所需套件，需要的套件與版本已定義在 `requirements.txt`，下載完輸入`pip list`檢查所有用 `pip` 下載的套件。

```shell
python -m pip install --upgrade pip #pip更新至最新版本
pip install -r requirements.txt
pip list
```
```
Package             Version
------------------- -------
asgiref             3.5.0
dj-database-url     0.5.0
Django              3.2.6
django-cors-headers 3.8.0
djangorestframework 3.12.4
Faker               13.3.0
faker-vehicle       0.2.0
pip                 20.1.1
psycopg2-binary     2.9.1
python-decouple     3.4
```


>`.env`裡存的是環境變數。可以將當中的變數改成符合你電腦資料庫的值。
```shell
ALLOWED_HOSTS=.localhost,127.0.0.1
DATABASE_URL=postgres://root:secret1234@127.0.0.1:5432/order_application
```


最後,啟動 Django server。

```shell
python manage.py runserver
```
