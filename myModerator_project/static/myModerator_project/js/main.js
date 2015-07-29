
$(document).ready(function($) {


    
  jQuery.validator.addMethod('selectcheck', function (value) {
      if (value == '' || value =='none') {
         return false;
      }else{
         return true;
      }
    }, "This field is required.");
    
    
    $('form').each(function(){
        $(this).validate();
    });
    
    
    
    $("#createForum-form").ajaxForm({ 
            success:       function(responseText){
                console.log(responseText);
                if (responseText.error) {
                    alert(responseText.error);
                }else{
                    window.location.href = "/forumView/"+responseText.forumID+"/";
                }
            },
            dataType:  'json',
            timeout:   4000 
        });
    
    
    $("#createPost-form").ajaxForm({ 
            success:       function(responseHTML){
                console.log(responseHTML);
                $("#allposts").prepend(responseHTML);
            },
            clearForm: true,
            resetForm:  true,
            dataType:  'html',
            timeout:   4000 
        });
    
    $('.comment-link').click(function(){
        var element = $(this).closest('.item.row').next('div');
        if ($('.comment-Submission').is(':visible')) {
            $('.comment-Submission').filter(':visible').slideToggle('slow');
        }
        element.slideToggle('slow');
    });
    
    $(".commentSubmit").click(function(e){
        e.preventdefault;
    });

    function getCookie(cname){
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i++){
            var c = ca[i].trim();
            if (c.indexOf(name)==0) return c.substring(name.length,c.length);
          }
        return "";
        }
        
    
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    $('#dashboardLink').click(function(){
        if ($('#groupsLink').hasClass('active')){
            $('#groupsLink').removeClass('active');
        }
        $('#dashboardLink').addClass('active');
        });
    $('#groupsLink').click(function(){
        
        if ($('#dashboardLink').hasClass('active')){
            $('#dashboardLink').removeClass('active');
        }
        $('#groupsLink').addClass('active');
        });

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

});