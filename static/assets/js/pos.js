

    $('input[name="Searchitem"]').change(function(e) {
       var search_items  = $(this).val();
        //this is equal to hidden form 
       $('#Seachitem_name').val(search_items);

       $('#SearchForm').submit();
   
        });
    $('#SearchForm').submit(function(e) {
        e.preventDefault();
    
      
        $.ajax({
            type: "POST",
            url: window.location.href + "search/",
            data: $(this).serialize(),
            success: function (response) {
                console.log(response.success);
                location.reload();  
            },
           
        });
    });
   