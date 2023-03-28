document.getElementById("a2").classList.add("active");
document.getElementById("a2").classList.add("actives");
function removeoneregister(){
    document.getElementById('student_register').classList.add('d-none');
    document.getElementById('teacher_register').classList.add('d-none');

}

function removetworegister(){
    document.getElementById('studentclickr').classList.remove('bgcolor');
    document.getElementById('studentclickrp').classList.remove('text-white');
    document.getElementById('teacherclickr').classList.remove('bgcolor');
    document.getElementById('teacherclickrp').classList.remove('text-white');
}

document.getElementById('studentclickr').addEventListener('click', function() {	
    removeoneregister();
    document.getElementById('student_register').classList.remove('d-none'); 

    removetworegister();
    document.getElementById('studentclickr').classList.add('bgcolor');
    document.getElementById('studentclickrp').classList.add('text-white');
    });

    document.getElementById('teacherclickr').addEventListener('click', function() {
        removeoneregister();
         document.getElementById('teacher_register').classList.remove('d-none');

         removetworegister();
        document.getElementById('teacherclickr').classList.add('bgcolor');
        document.getElementById('teacherclickrp').classList.add('text-white');
    });

    document.addEventListener("DOMContentLoaded", function() {
        var imageUpload = document.getElementById("studentimage");
        imageUpload.addEventListener("change", function() {
            readURL(this,"studentimagepreview");
        });
 
        var imageUploads = document.getElementById("teacherimage");
        imageUploads.addEventListener("change", function() {
            readURL(this,"teacherimagepreview");
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
   
        $(document).ready(function() {
          setTimeout(function() {
            $('#alert_message').fadeOut('slow');
          }, 3000);
        });
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()