$(document).ready(function () {
	field = $('#id_tr_lists').parent()

	if ($("#id_creation_type").val() == 'smoke' ) {
	    field.css("display","none");
	} else {
	    field.css("display","block");
	}

	$("#id_creation_type").change( function() {
		if ($("#id_creation_type").val() == 'smoke' ) {
		    field.css("display","none");
		} else {
		    field.css("display","block");
		}
	    }); 

    });
