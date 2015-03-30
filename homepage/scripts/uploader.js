$(function() {
    var inputElement = $('#id_upload_file');

    inputElement.off('change.uploader').on('change.uploader', function() {

        var fd = new FormData();
        var file = this.files[0];

        fd.append("uploadfile", file);

        $('.progress').fadeTo(1000, 1);

        $.ajax({

            url: '/homepage/uploader.upload/',
            type: 'POST',
            contentType: false,
            processData: false,
            data: fd,
            xhr: function() {
                var xhr = jQuery.ajaxSettings.xhr();
                if (xhr.upload) {
                    xhr.upload.addEventListener('progress', function(evt) {
                        if (evt.lengthComputable) {
                            var percentComplete = (evt.loaded / evt.total) * 100;
                            $('#progress_bar').css("width", percentComplete + '%').attr('aria-valuenow', percentComplete);
                        } //endif
                    }, false); //eventlistener
                } //endif
                return xhr;
            }, //xhr
            success: function(data){
                $('#id_upload_fullname').val(data);
                $('#id_original_name').val(file.name);
                $('.progress').delay(500).fadeTo(2000, 0);


            }, // success
            error: function(err){
                console.log("Error!!!!!!");
                console.log(err);
            }, // error
        }); //ajax

    }); //change

    inputElement.closest('form').off('submit.uploader').on('submit.uploader', function() {
        inputElement.remove();
    }); //submit

}); //ready