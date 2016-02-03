
$('#strainItem').click(function (e) {
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: $(this).attr('href'),
        success: function (data, textStatus, jqXHR) {
           $('#strainModal').find('.modal-body').html(data);
           $('#strainModal').modal('show');
        }
    });
});
