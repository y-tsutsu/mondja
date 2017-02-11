// Buttonの連打対応
$('form').submit(function () {
    $(this).submit(function () {
        //alert('二度押し防止！！');
        return false;
    });
});

// Every time a modal is shown, if it has an autofocus element, focus on it.
$('.modal').on('shown.bs.modal', function () {
    $(this).find('[autofocus]').focus();
});

// highlight.js initialize
hljs.initHighlightingOnLoad();
