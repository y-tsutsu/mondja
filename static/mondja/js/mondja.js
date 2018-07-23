// Buttonの連打対応
$('form').submit(function () {
    $(this).submit(function () {
        //alert('二度押し防止！！');
        return false;
    });
});

// トップへのスクロールボタン
$(function () {
    var topBtn = $('#totop > a');
    topBtn.hide();
    // スクロールしたらボタン表示
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            topBtn.fadeIn();
        } else {
            topBtn.fadeOut();
        }
    });
    // スクロールしてトップ
    topBtn.click(function () {
        $('body, html').animate({
            scrollTop: 0
        }, 500);
        return false;
    });
});

// highlight.js initialize
hljs.initHighlightingOnLoad();

// Materialize
M.AutoInit();