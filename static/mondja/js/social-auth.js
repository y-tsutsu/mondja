// facebook認証でURLに「#_=_」が表示される問題
if (window.location.hash == '#_=_') window.location.hash = '';
