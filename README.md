# DualKey_ChainKey_Angle_Joystick
想將這些硬體整合起來，在看圖時有個快速鍵的小keypad可用。

實際步驟：
DualKey這個雙按鍵的設備，內含小型ESP32，若要自己開發程式，得先用m5 burner燒錄 UIFlow2的韌體給它。
接著在UIFlow2中，用USB實體連線接上設備DualKey。
注意:在UIFlow2中，
DualKey的buttonA（離吊繩比較近）, buttonB（離吊繩遠）
要接上 chainKey, Angle, Joystick等設備時，注意離吊繩近的是 Bus1, l另一個是bus2
要執行可分「一次性測試」、「永久燒錄」兩種。
執行時得先選擇Com port，只要USB有接好，大概沒問題。

這個範例會使用時，得接著USB，模擬HID的鍵盤。
UIFlow2不支援同時模擬 USB鍵盤跟滑鼠。所以這程式只模擬鍵盤。

ps. 若要同時模擬兩種裝置，可能要進Arduino直接寫更底層的程式。
