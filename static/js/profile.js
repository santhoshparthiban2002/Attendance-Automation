document.getElementById("a4").classList.add("active");
document.getElementById("a4").classList.add("actives");


disable_form = document.getElementById("disable_form");
enable_form = document.getElementById("enable_form");
formon = document.querySelectorAll(".formon");
formbutton = document.querySelectorAll(".formbutton");


disable_form.addEventListener("click", function() {
    formon.forEach(input => {
        input.disabled = false;
        disable_form.classList.add("d-none");
        enable_form.classList.remove("d-none");
      });
      formbutton.forEach(button => {
        button.classList.remove("d-none");
      });
  });

  enable_form.addEventListener("click", function() {
    formon.forEach(input => {
        input.disabled = true;
        enable_form.classList.add("d-none");
        disable_form.classList.remove("d-none");
        
      });
      formbutton.forEach(button => {
        button.classList.add("d-none");
      });
  });



  document.addEventListener("DOMContentLoaded", function() {
    var imageUpload = document.getElementById("studentimage");
    imageUpload.addEventListener("change", function() {
        readURL(this,"studentimagepreview");
    });
    function readURL(input,previewimg) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                var imagePreview = document.getElementById(previewimg);
                imagePreview.style.backgroundImage = 'url('+e.target.result +')';
                imagePreview.style.display = 'none';
                fadeIn(imagePreview, 650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }



    function fadeIn(element, duration) {
        var opacity = 0;
        var interval = 50;
        var gap = interval / duration;
        element.style.opacity = 0;
        element.style.display = "block";
        function func() {
            opacity += gap;
            element.style.opacity = opacity;
            if(opacity >= 1) {
                clearInterval(fading);
            }
        }
        var fading = setInterval(func, interval);
    }
});


setTimeout(function() {
    $('#alert_message').fadeOut('slow');
  }, 3000);