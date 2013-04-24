function onLinkedInLoad() {
    IN.Event.on(IN, "auth", onLinkedInAuth);
  }

  // 2. Runs when the viewer has authenticated
  function onLinkedInAuth() {
    IN.API.Profile("me").result(displayProfiles);
  }

  // 2. Runs when the Profile() API call returns successfully
  function displayProfiles(profiles) {
    member = profiles.values[0];
    alert(member.firstName); 
   }
  
  function tokenExchange() {
      // this must be the same domain as the application, where we write the cookie
      $.post('https://www.example.org/token-exchange.html');
 }