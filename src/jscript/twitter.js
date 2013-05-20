function ajaxTwitterPost(shrtlivedtoken, loginType) {
	var xmlhttp;
	if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp = new XMLHttpRequest();
	} else {// code for IE6, IE5
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			alert(xmlhttp.responseText);
		}
	}
	xmlhttp.open("POST", "https://api.twitter.com/oauth/request_token", true);
	xmlhttp.setRequestHeader("Content-type",
			"application/x-www-form-urlencoded");
	
	OAuth oauth_nonce="K7ny27JTpKVsTgdyLdDfmQQWVLERj2zAK5BslRsqyw",
	oauth_callback="http%3A%2F%2Fmyapp.com%3A3005%2Ftwitter%2Fprocess_callback",
	oauth_signature_method="HMAC-SHA1", 
	oauth_timestamp="1300228849", 
	oauth_consumer_key="OqEqJeafRSF11jBMStrZz", 
	oauth_signature="Pc%2BMLdv028fxCErFyi8KXFM%2BddU%3D", 
	oauth_version="1.0"
		
	xmlhttp
			.send("shrtlivedtoken=" + shrtlivedtoken + "&loginType="
					+ loginType);
}