==============================================================
利用方法
	GUIPosition.pyでcolabの新規セルの座標を指定し代入
	X_POS,Y_POS
	activateしclickd.pyを実行させる

	もしくは
	clickd.pyのディレクトリで
	pyinstaller clickd.pyを実行
	dist/clickd.exeを起動させる

==============================================================
参考
	https://qiita.com/takanorimutoh/items/53bf44d6d5b37190e7d1
	https://qiita.com/enmaru/items/2770df602dd7778d4ce6
	https://flat-kids.net/2020/07/28/google-colab-%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E5%88%87%E3%82%8C%E3%82%92%E9%98%B2%E6%AD%A2%E3%81%99%E3%82%8B/
	function ClickConnect(){
	  console.log("60sごとに再接続");
	  document.querySelector("colab-connect-button").click()
	}
	setInterval(ClickConnect,1000*60);
==============================================================
