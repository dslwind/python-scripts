## 批量下载 B 站 UP 主主页视频及弹幕

### 安装依赖

`pip install -r requirements.txt`

### 使用说明

- 准备工作
  以 Firefox 浏览器为例，打开 B 站 UP 主主页，鼠标停留在某一视频预览图上方，右键检查元素，定位到`<div class="content clearfix">`，复制内部 HTML，并保存为`1.html`。

- 多线程下载
  `python bilibili_download.py`
  默认 8 线程下载，可将以下代码中，调整为想要的线程数。

  ```python
  pool = Pool(processes=8)
  ```

- 保存为批处理下载脚本
  `python write_to_bat.py`
  程序将生成`download.bat`，只能单线程下载。
