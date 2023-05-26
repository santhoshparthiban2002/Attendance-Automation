
document.getElementById("a3").classList.add("active");
document.getElementById("a3").classList.add("actives");
function removeonecourse(){
    document.getElementById('course_registration').classList.add('d-none');
   document.getElementById('holiday_declaration').classList.add('d-none');
   document.getElementById('course_overview').classList.add('d-none');
   document.getElementById('holiday_overview').classList.add('d-none');


}
function removetwocourse(){
document.getElementById('holidayclick').classList.remove('bgcolor');
     document.getElementById('holidayclickp').classList.remove('text-white');
       document.getElementById('courseclick').classList.remove('bgcolor');
      document.getElementById('courseclickp').classList.remove('text-white');

}
document.getElementById('courseclick').addEventListener('click', function() {
       
removeonecourse();
       document.getElementById('course_registration').classList.remove('d-none'); 
       document.getElementById('course_overview').classList.remove('d-none'); 
       removetwocourse();
      document.getElementById('courseclick').classList.add('bgcolor');
       document.getElementById('courseclickp').classList.add('text-white');
  
   });

   document.getElementById('holidayclick').addEventListener('click', function() {
       removeonecourse();
        document.getElementById('holiday_declaration').classList.remove('d-none');
        document.getElementById('holiday_overview').classList.remove('d-none');
        removetwocourse();
        document.getElementById('holidayclick').classList.add('bgcolor');
      document.getElementById('holidayclickp').classList.add('text-white');
   });

   $(document).ready(function() {
    $('#dataTable1').DataTable();
    $('#dataTable2').DataTable();
    $('#dataTable3').DataTable();


    setTimeout(function() {
      $('#alert_message').fadeOut('slow');
    }, 3000);
  });


  document.addEventListener('DOMContentLoaded', function() {
    var clickableRows = document.querySelectorAll('.coursedatas');
    for (var i = 0; i < clickableRows.length; i++) {
      clickableRows[i].addEventListener('click', function() {
        var name = this.querySelector('td:nth-child(1)').textContent;
        document.querySelector('#myModal1 .modal-title').textContent = name;
        document.getElementById('name').value = name;



      });
    }
  });

  document.addEventListener('DOMContentLoaded', function() {
    var clickableRows = document.querySelectorAll('.holidaydata');
    for (var i = 0; i < clickableRows.length; i++) {
      clickableRows[i].addEventListener('click', function() {
        var years = this.querySelector('td:nth-child(1)').textContent;
        var date = this.querySelector('td:nth-child(2)').textContent;
        var reason = this.querySelector('td:nth-child(3)').textContent;
        document.querySelector('#myModal2 .modal-title').textContent = years+"-"+date;
        var parts = date.split('-');
        var yyyyMMdd = parts[2] + '-' + parts[1] + '-' + parts[0];
        var dateObject = new Date(yyyyMMdd);
        var year = dateObject.getFullYear();
        var months = dateObject.getMonth() + 1;
        var month = months.toString().padStart(2, '0');
        var days = dateObject.getDate();
        var day = days.toString().padStart(2, '0');
        var formattedDate = [year, month, day].join('-');

        document.getElementById('hdyear').value = years;
        document.getElementById('hddate').value = formattedDate;
        document.getElementById('hdreason').value = reason;     

      });
    }
  });
