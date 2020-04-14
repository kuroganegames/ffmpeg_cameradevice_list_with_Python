# カメラデバイス一覧の取得(windows用)
これはPythonのsubprocessからffmpegを叩いてwindowsのカメラデバイス一覧をcsvファイルとして保存します。

DirectShowに対応したデバイスが取得できます。

## 要求
windows

python 3.x系

ffmpeg

## 使い方
Windows環境上でのみ使用できます。

pythonの3.x系とffmpeg共にパスが通っている状態で、「ffmpeg_list_device.py」をDL&実行してください。

「ffmpeg_list_device.py」を設置した場所に「device_sorted.txt」が作成されます。

csvファイルを開くと1列目にデバイス名が、2列目に代替デバイス名が表示されます。

DirectShowに対応したデバイスが取得できるので、環境によっては表示されたデバイス名が使用できないことがあります。
