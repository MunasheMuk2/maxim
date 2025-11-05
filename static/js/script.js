// Wait until the page loads
window.onload = function() {
    // Get the messages container
    var messageDiv = document.getElementById("messages");
    
    if (messageDiv) {
        // Get all messages from the data attribute
        var messages = messageDiv.dataset.messages.split("|");
        
        // Show each message using an alert
        for (var i = 0; i < messages.length; i++) {
            var msg = messages[i].trim();
            if (msg) {
                alert(msg);
            }
        }
    }
};

/* Accordion*/

// Code amended from W3schools 

window.onload = function () {
    var accordion = document.querySelectorAll(".accordion");
    var i;
  
    for (i = 0; i < accordion.length; i++) {
      accordion[i].addEventListener("click", function () {
        this.classList.toggle("active");
  
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
          panel.style.display = "none";
        } else {
          panel.style.display = "block";
        }
      });
    }
  };
  