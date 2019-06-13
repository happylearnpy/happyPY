$(function () {

        // 	验证码
    //	 验证码刷新
    function code() {
        var str = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM";
        var str1 = 0;
        for (var i = 0; i < 4; i++) {
            str1 += str.charAt(Math.floor(Math.random() * 62))
        }
        str1 = str1.substring(1)
        $("#code").text(str1);
    }


    code();
    $("#code").click(code);
     $("#123").blur(function () {
        if ($(this).val().length == 0) {
            $(this).parent().next().next("div").text("");
            $(this).parent().next().next("div").css("color", '#ccc');
        } else if ($(this).val().toUpperCase() != $("#code").text().toUpperCase()) {
            $(this).parent().next().next("div").text("验证码不正确");
            $(this).parent().next().next("div").css("color", 'red');
        } else {
            $(this).parent().next().next("div").text("");
        }

    })
    $("#login_submit_btn").click(function (e) {
            if ($("input[name='logidentify']").val().length == 0) {
                 $("#identifyid").text("此处不能为空");
                $("input[name='logidentify']").parent().next().next("div").css("color", 'red');
                e.preventDefault();
                return;
            } else if ($("input[name='logidentify']").val().toUpperCase() != $("#code").text().toUpperCase()) {
               $("#identifyid").text("验证码不正确");
                $("input[name='logidentify']").parent().next().next("div").css("color", 'red');
                e.preventDefault();
                return;
            } else {
                $("input[name='logidentify']").parent().next().next("div").text("");
                var encrypt = new JSEncrypt();
                var pubkey='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCTTxg035BIC/NNkjg67w6+uS4bx9f9CkCRM8/y8SqfC2GKA1+bq4z4ukLFhh8zaLmHexXWoxST/F7HEyfebt0y7QkuwVbF0QUyEGLNEGhV5a/WEC/E/96c/eUi1yKlZh69MbsxxvTMVldaqoPtC3N/0vlNYHmVyOBjp7gZReFb3wIDAQAB';
                encrypt.setPublicKey(pubkey);
                var password = encrypt.encrypt($("input[name='password']").val());
                // alert(password);
                $("input[name='password']").val(password);
                //     $("input[name='password2']").attr("value",password)

                // alert($("input[name='password']").val());
            }

    })

})
