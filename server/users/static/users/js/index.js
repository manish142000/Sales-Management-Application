
$("#login").onclick( function (event) {
    console.log("Ye hai yaha aa rha!");
    event.preventDefault();
    $.ajax({
        url: "/loggedin/",
        headers: {
            'Authorization': `Bearer ${window.localStorage.getItem('accessToken')}`
        },
        type: "GET",
        tokenFlag: true,
        success: function (data) {
            console.log("-> " + data);
        },
        error: handleAjaxError
    });
});


$("#login-form").submit(function (event) {
    event.preventDefault();
    let formData = new FormData();
    formData.append('email', $('#email').val().trim());
    formData.append('password', $('#password').val().trim());
    $.ajax({
        url: "/login/",
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            // store tokens in localStorage
            window.localStorage.setItem('refreshToken', data['refresh']);
            window.localStorage.setItem('accessToken', data['access']);
        },
        error: function (rs, e) {
            console.error(rs.status);
            console.error(rs.responseText);
        }
    }); // end ajax
    //console.log("Ye token hai! " + window.localStorage.getItem('accessToken'))
    function handleAjaxError(rs, e) {
        /*
            And if it returns 401, then we call obtainAccessTokenWithRefreshToken() method 
            To get a new access token using refresh token.
        */
        if (rs.status == 401) {
            if (this.tokenFlag) {
                this.tokenFlag = false;
                if (obtainAccessTokenWithRefreshToken()) {
                    this.headers["Authorization"] = `Bearer ${window.localStorage.getItem('accessToken')}`
                    $.ajax(this);  // calling API endpoint again with new access token
                }
            }
        } else {
            console.error(rs.responseText);
        }
    }
});


function obtainAccessTokenWithRefreshToken() {
    /*
        This method will create new access token by using refresh token.
        If refresh token is invalid it will redirect user to login page
    */
    let flag = true;
    let formData = new FormData();
    formData.append('refresh', window.localStorage.getItem('refreshToken'));
    $.ajax({
        url: 'token/refresh/',
        type: "POST",
        data: formData,
        async: false,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            window.localStorage.setItem('accessToken', data['access']);
        },
        error: function (rs, e) {
            if (rs.status == 401) {
                flag = false;
                window.location.href = "/login/";
            } else {
                console.error(rs.responseText);
            }
        }
    }); // end ajax
    return flag
}


