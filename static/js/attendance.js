document.getElementById("a5").classList.add("active");
document.getElementById("a5").classList.add("actives");
$(document).ready(function () {
    $('#dataTable4').DataTable();
  });


  $(document).ready(function(){

    $('.clickable-row').click(function(){
        var name = $(this).find('td:nth-child(1)').text();
        var roll = $(this).find('td:nth-child(2)').text();
        var date = $(this).find('td:nth-child(3)').text();
        $('#myModal .modal-title').text(name);
        document.getElementById("attendance_roll").value= roll;
        const dateObject = new Date(date);
        const year = dateObject.getFullYear();
        const months = dateObject.getMonth() + 1;
        const month = months.toString().padStart(2, '0');
        const days = dateObject.getDate();
        const day = days.toString().padStart(2, '0');
        const formattedDate = [year, month, day].join('-');
        document.getElementById("attendance_date").value= formattedDate;
    });
});
 