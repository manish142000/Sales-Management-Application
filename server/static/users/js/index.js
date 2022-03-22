$("#login-form").submit(function (event) {
    console.log("Yaha aa rha!");
    event.preventDefault();
    let formData = new FormData();
    formData.append('username', $('#email').val().trim());
    formData.append('password', $('#password').val().trim());

    $.ajax({
        url: "/login",
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


$(document).ready(function () {
    /*
        Hitting an API endpoint, By sending access token in header of an API request
    */
    $.ajax({
        url: 'loggedin/',
        headers: {
            'Authorization': `Bearer ${window.localStorage.getItem('accessToken')}`
        },
        type: "GET",
        tokenFlag: true,
        success: function (data) {
            console.log(data);
        },
        error: handleAjaxError
    }); // end ajax
});

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

$("#logout-form").submit(function (event) {
    event.preventDefault();
    window.localStorage.removeItem('refreshToken');
    window.localStorage.removeItem('accessToken');
    window.location.href = "/login/";
});