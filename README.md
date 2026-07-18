# Chain DualKey HID Controller
##動機：
在使用看圖程式（BandiView)時，通常都只用到 pagedown, pageup, del（刪除）, ins（另存到圖庫），偶而用到放大縮小檢視細節。
以前使用滑鼠、鍵盤搭配，但長期檢視一堆照片，手腕感覺不太舒服，那天看到M5 出了 dualkey 這產品，想說買來兜一個外接小鍵盤用用。

##硬體
這次共買了 Chain Dualkey, Chain Key, Chain Angle, Chain Joystick, 這些設備可以一直串接，感覺很好玩。
總之，想將這些硬體整合起來，在看圖時有個快速鍵的小keypad可用。

##軟體
DualKey這個雙按鍵的設備，內含小型ESP32，若要自己用UIFlow2寫程式，得先用m5 burner燒錄 UIFlow2的韌體給它。
（另一個選擇，是燒錄 Chain Dualkey User Demo官方範例，完全不寫程式，可將dualkey透過WIFI與電腦連線後，設置HID使用）
![Platform](https://img.shields.io/badge/platform-Windows-blue)

##技術
用設備模擬電腦的滑鼠、鍵盤，需有HID支援。

##硬體串接
接著在UIFlow2中，用USB實體連線接上設備DualKey。
注意:在UIFlow2中，
DualKey的buttonA（離吊繩比較近）, buttonB（離吊繩遠）
要接上 chainKey, Angle, Joystick等設備時，注意離吊繩近的是 Bus1, l另一個是bus2
左右兩側都能接，但每個 Chain 裝置底部的三角箭頭，必須由 DualKey 主控端朝外指。

##UIFlow2中寫程式
要執行可分「一次性測試」、「永久燒錄」兩種。
執行時得先選擇Com port，只要USB有接好，大概沒問題。

##Chain Dualkey的設定、取用非常方便，而且執行速度很快
###但其他串接的周邊，因為是使用STM32與其通訊連接，因此速度不快，建議不要在上面執行太複雜的功能，尤其是想要及時性高的話，不要在程式中設定燈光顏色。

這個範例會使用時，得一直接著USB，模擬HID的鍵盤。
UIFlow2不支援同時模擬 USB鍵盤跟滑鼠。所以這程式只模擬鍵盤。

ps. 若要同時模擬兩種裝置，可能要進Arduino直接寫更底層的程式。
