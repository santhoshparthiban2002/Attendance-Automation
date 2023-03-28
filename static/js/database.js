
function removeone(){
    document.getElementById('student_database').classList.add('d-none');
   document.getElementById('teacher_database').classList.add('d-none');
  document.getElementById('course_database').classList.add('d-none');
  document.getElementById('holiday_database').classList.add('d-none');
}
function removetwo(){
     document.getElementById('teacherclick').classList.remove('bgcolor');
     document.getElementById('teacherclickp').classList.remove('text-white');
       document.getElementById('studentclick').classList.remove('bgcolor');
      document.getElementById('studentclickp').classList.remove('text-white');
      document.getElementById('courseclick').classList.remove('bgcolor');
     document.getElementById('courseclickp').classList.remove('text-white');
     document.getElementById('holidayclick').classList.remove('bgcolor');
     document.getElementById('holidayclickp').classList.remove('text-white');
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

   document.getElementById('holidayclick').addEventListener('click', function() {
    removeone();
     document.getElementById('holiday_database').classList.remove('d-none');
     removetwo();
    document.getElementById('holidayclick').classList.add('bgcolor');
    document.getElementById('holidayclickp').classList.add('text-white');
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

    rows.forEach(function(row) {
      row.addEventListener("click", function() {
        var href = this.getAttribute("data-href");
        window.location = href;
      });
    });

$(document).ready(function () {
    $('#dataTable1').DataTable();
    $('#dataTable2').DataTable();
    $('#dataTable3').DataTable();
    $('#dataTable4').DataTable();
  });