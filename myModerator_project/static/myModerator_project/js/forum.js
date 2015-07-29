
$(document).ready(function($) {

    $(".commentInput").unbind('keydown').keydown(function(key){
        console.log('keyup');
        var code = key.keyCode || key.which;
        var $this = $(this);
        
        if(code == 13) {
            var postID = $(this).data('options').postID;
            var value = $(this).val();
            if (value != "" ) {
                $.ajax({
                    method: "POST",
                    url: createCommentURL,
                    data: { postID: postID, commentText: $(this).val() },
                    dataType: "html"
                })
                    .done(function( html ) {
                      console.log(html);
                     var element = $this.closest('ul').prev('ul');
                     var element2 = element.prev('ul');
                     var togglecommentBtn = element2.prev('span').children('span');
                     var commentNumber = togglecommentBtn.html();
                     togglecommentBtn.html(parseInt(commentNumber)+1);
                     element.append(html);
                     element2.append(html);
                    });
            } 
        }

    });

    $(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
       
        if (scroll > 65) {
            $("#sticky").attr("style","position:fixed; top:25px;");
            $(".submit-btn").hide();
            $(".description").hide();
            
        } else {
            $("#sticky").attr('style','position:absolute;');
            $(".submit-btn").show();
            $(".description").show();
        }
    });
    
    
    $(document).scroll(function (event) {
    var width = $(document).width();
       console.log(width);
        if (width < 768) {
            $("#logo").hide();
          
        } else {
            $("#logo").show();
        }
    });
    
    $(".togglecommentBtn").unbind("click").click(function (){
        var element = $(this).closest('div');
        var element2 = element.next('ul');
        var element3 = element2.next('ul');
        element2.slideToggle("slow");
        if (element3.is(':visible')) {
            element3.hide();
        
        } else {
            element3.show();
        }
        });
    
    $(".upvoting-button").unbind("click").click(function (){
        var element = $(this).prev('div');
        console.log(element.attr('class'));
        var upVoteSection = element.children('span');
        var rating = upVoteSection.html();
        var postID = $(this).data('options').postID;
        
        
        var value = rating + 1;
        
        if (value != "" ) {
            $.ajax({
                method: "POST",
                url: adjustRatingURL,
                data: { postID: postID, rating: "add" },
                dataType: "json"
            })
                .done(function( response ) {
                    console.log(response);
                    if (response.error) {
                        alert(response.error);
                    }else{
                        upVoteSection.html(parseInt(rating)+1);
                    }
             });
            } 
        });

    
    $(".downvoting-button").unbind("click").click(function (){
        var element = $(this).closest('div');
        var element2 = element.children('div');
        console.log(element2.attr('class'));
        var downVoteSection = element2.children('span');
        var rating = downVoteSection.html();
        var postID = $(this).data('options').postID;
        
        
        var value = rating + 1;
        
        if (value != "" ) {
            $.ajax({
                method: "POST",
                url: adjustRatingURL,
                data: { postID: postID, rating: "subtract" },
                dataType: "json"
            })
                .done(function( response ) {
                    console.log(response);
                    if (response.error) {
                        alert(response.error);
                    }else{
                        downVoteSection.html(parseInt(rating)-1);
                    }
             });
            } 
        });

    
    $("#forumInfo").click(function (){
        var element = $(this).closest('div');
        console.log(element.attr('class'));
        var element2 = element.parent('div');
        console.log(element2.attr('class'));
        var element3 = element2.next('div');
        element3.slideToggle( "slow" );
        
        });
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

});