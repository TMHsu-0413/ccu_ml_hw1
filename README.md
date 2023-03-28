
- report.pdf較詳細，可以看那一份即可

## Q1
```python=
# 執行指令
python 611410086_proj1_ver1.py
```
- 執行後會跑出一張圖，分別為標記為-1(紅點)及+1(藍點)的資料
- m與b每次都會亂數產生

## Q2
```python=
# 執行指令
python 611410086_proj1_ver2.py
```
- 執行後會依順序顯示一行字 random x use y times 及一張圖，關閉圖後會顯示下一張圖
- 總共會顯示3次，每一次都是random 30個測資後跑pla algorithm的結果
- 最後顯示一行字 average z times，為3次訓練次數的平均值

## Q3
```python=
# 執行指令
python 611410086_proj1_ver3.py
```
- 執行後會依順序顯示一行字 x algorithm use y seconds 及一張圖，關閉圖後會顯示下一張圖
- 總共顯示2次，第一次為PLA algorithm，第二次為pocket algorithm
- 顯示的字為此algorithm跑了幾秒
- pocket algorithm的預設max iteration為500

## Q4
```python=
# 執行指令
python 611410086_proj1_ver4.py
```
- 執行後會跑出一行字 accuracy before/after mislabel: x 及一張圖，關閉圖後會顯示下一張圖
- 第一次顯示為mislabel前的結果及準確率(Q3的設定)
- 第二次顯示為隨機mislabel 50筆正及50筆負資料後的準確率(這張圖因為無法二分，所以會執行較久)
- pocket algorithm的預設max iteration為2000