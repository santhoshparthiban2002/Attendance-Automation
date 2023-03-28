document.getElementById("a5").classList.add("active");
document.getElementById("a5").classList.add("actives");
$(document).ready(function () {
    $('#dataTable4').DataTable();
  });


  document.addEventListener('DOMContentLoaded', function() {
    var clickableRows = document.querySelectorAll('.clickable-row');
    for (var i = 0; i < clickableRows.length; i++) {
      clickableRows[i].addEventListener('click', function() {
        var name = this.querySelector('td:nth-child(1)').textContent;
        var roll = this.querySelector('td:nth-child(2)').textContent;
        var date = this.querySelector('td:nth-child(3)').textContent;
        document.querySelector('#myModal .modal-title').textContent = name;
        document.getElementById('attendance_roll').value = roll;
        var parts = date.split('-');
        var yyyyMMdd = parts[2] + '-' + parts[1] + '-' + parts[0];
        var dateObject = new Date(yyyyMMdd);
        var year = dateObject.getFullYear();
        var months = dateObject.getMonth() + 1;
        var month = months.toString().padStart(2, '0');
        var days = dateObject.getDate();
        var day = days.toString().padStart(2, '0');
        var formattedDate = [year, month, day].join('-');
        document.getElementById('attendance_date').value = formattedDate;
      });
    }
  });
  
  $(document).ready(function() {
    setTimeout(function() {
      $('#alert_message').fadeOut('slow');
    }, 3000);
  });