function removeone(){
    document.getElementById('student_database').classList.add('d-none');
   document.getElementById('teacher_database').classList.add('d-none');
  document.getElementById('course_database').classList.add('d-none');
}
function removetwo(){
document.getElementById('teacherclick').classList.remove('bgcolor');
     document.getElementById('teacherclickp').classList.remove('text-white');
       document.getElementById('studentclick').classList.remove('bgcolor');
      document.getElementById('studentclickp').classList.remove('text-white');
      document.getElementById('courseclick').classList.remove('bgcolor');
     document.getElementById('courseclickp').classList.remove('text-white');
}
document.getElementById('studentclick').addEventListener('click', function() {
       
       removeone();
       document.getElementById('student_database').classList.remove('d-none'); 
       removetwo();
       document.getElementById('studentclick').classList.add('bgcolor');
      document.getElementById('studentclickp').classList.add('text-white');
  
   });

   document.getElementById('teacherclick').addEventListener('click', function() {
       removeone();
        document.getElementById('teacher_database').classList.remove('d-none');
        removetwo();
       document.getElementById('teacherclick').classList.add('bgcolor');
       document.getElementById('teacherclickp').classList.add('text-white');
   });

   document.getElementById('courseclick').addEventListener('click', function() {
       removeone();
       document.getElementById('course_database').classList.remove('d-none');
       removetwo();
       document.getElementById('courseclick').classList.add('bgcolor');
  document.getElementById('courseclickp').classList.add('text-white');
   });



document.getElementById("a4").classList.add("active");
document.getElementById("a4").classList.add("actives");


    // Get all rows with the "clickable-row" class
    var rows = document.querySelectorAll(".clickable-row");
  
    // Add a click event listener to each row
    rows.forEach(function(row) {
      row.addEventListener("click", function() {
        // Get the value of the "data-href" attribute
        var href = this.getAttribute("data-href");
  
        // Redirect the user to the next page with the student ID as a URL parameter
        window.location = href;
      });
    });

$(document).ready(function () {
    $('#dataTable1').DataTable();
    $('#dataTable2').DataTable();
    $('#dataTable3').DataTable();
  });