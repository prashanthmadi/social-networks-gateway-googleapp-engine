(function() {
	var po = document.createElement('script');
	po.type = 'text/javascript';
	po.async = true;
	po.src = 'https://apis.google.com/js/client:plusone.js';
	var s = document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(po, s);
})();

function signInCallback(authResult) {
	if (authResult['access_token']) {
		helper.onSignInCallback(authResult);
	} else if (authResult['error']) {
	}
}

var helper = (function() {
	var BASE_API_PATH = 'plus/v1/';

	return {
		/**
		 * Hides the sign in button and starts the post-authorization
		 * operations.
		 * 
		 * @param {Object}
		 *            authResult An Object which contains the access token and
		 *            other authentication information.
		 */
		onSignInCallback : function(authResult) {
			gapi.client.load('plus', 'v1', function() {
				helper.profile();
				helper.people();
			});
		},

		/**
		 * Calls the OAuth2 endpoint to disconnect the app for the user.
		 */
		disconnect : function() {
			// Revoke the access token.
			$.ajax({
				type : 'GET',
				url : 'https://accounts.google.com/o/oauth2/revoke?token='
						+ gapi.auth.getToken().access_token,
				async : false,
				contentType : 'application/json',
				dataType : 'jsonp',
				success : function(result) {
					alert("user loged out");
				},
				error : function(e) {
					console.log(e);
				}
			});
		},

		/**
		 * Gets and renders the list of people visible to this app.
		 */
		people : function() {
			var request = gapi.client.plus.people.list({
				'userId' : 'me',
				'collection' : 'visible'
			});
			request.execute(function(people) {
				for ( var personIndex in people.items) {
					person = people.items[personIndex];
				}
			});
		},

		/**
		 * Gets and renders the currently signed in user's profile data.
		 */
		profile : function() {
			var request = gapi.client.plus.people.get({
				'userId' : 'me'
			});
			request.execute(function(profile) {
				if (profile.error) {
					return;
				}
				alert(profile.id);
				alert(profile.displayName);
			});
		}
	};
})();