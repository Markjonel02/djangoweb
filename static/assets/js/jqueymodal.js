$(document).ready(function() {
    $('#editForm').on('submit', function(event) {
        event.preventDefault();
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            success: function(response) {
                if (response.success) {
                    // update the page with the new data
                    $('#name').val(response.name);
                    $('#number').val(response.number);
                    $('#email').val(response.email);
                    $('#add').val(response.add);
                    // close the modal
                    $('#editmodal').modal('hide');
                }
            }
        });
    });
});