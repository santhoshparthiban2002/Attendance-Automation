document.getElementById("a6").classList.add("active");
document.getElementById("a6").classList.add("actives");
$(document).ready(function () {
    $('#dataTable1').DataTable();
    $('#dataTable2').DataTable();

  });
function removeonecourse(){
    document.getElementById('course_enrollment').classList.add('d-none');
   document.getElementById('grade_promotion').classList.add('d-none');
   document.getElementById('enrollment_overview').classList.add('d-none');
   document.getElementById('promotion_overview').classList.add('d-none');
}
function removetwocourse(){
document.getElementById('enrollmentclick').classList.remove('bgcolor');
     document.getElementById('enrollmentclickp').classList.remove('text-white');
       document.getElementById('promotionclick').classList.remove('bgcolor');
      document.getElementById('promotionclickp').classList.remove('text-white');

}
document.getElementById('promotionclick').addEventListener('click', function() {
       
removeonecourse();
       document.getElementById('grade_promotion').classList.remove('d-none'); 
       document.getElementById('promotion_overview').classList.remove('d-none'); 
       removetwocourse();
      document.getElementById('promotionclick').classList.add('bgcolor');
       document.getElementById('promotionclickp').classList.add('text-white');
   });

   document.getElementById('enrollmentclick').addEventListener('click', function() {
       removeonecourse();
        document.getElementById('course_enrollment').classList.remove('d-none');
        document.getElementById('enrollment_overview').classList.remove('d-none');
        removetwocourse();
        document.getElementById('enrollmentclick').classList.add('bgcolor');
      document.getElementById('enrollmentclickp').classList.add('text-white');
   });

