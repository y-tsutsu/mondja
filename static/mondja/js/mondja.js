$('form').submit(function () {
    $(this).submit(function () {
        //alert('二度押し防止！！');
        return false;
    });
});
