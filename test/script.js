$(document).ready(function() {

    function vary(e, variations){
        settings = e.css('font-variation-settings').split(',');
        
        Object.keys(variations).forEach(function(key) {
            for(var i = settings.length - 1; i >= 0; i--) {
                if(settings[i].indexOf(key) !== -1){
                    settings.splice(i, 1);
                }
            }
        })
        Object.keys(variations).forEach(function(key) {
            settings.push('"' + key + '" ' + String(variations[key]));
        })
        e.css('font-variation-settings', settings);
    }

    var edit = $("#edit1");
    var edit2 = $("#edit2");

    // link sliders with variable font settings
    $("#change_wght").on('input', function(){
        vary(edit, {"wght": this.value});
    });

    $("#change_wdth").on('input', function(){
        vary(edit, {"wdth": this.value});
    });

    $("#change_opsz").on('input', function(){
        vary(edit, {"opsz": this.value});
    });
    
    $("#change_wght2").on('input', function(){
        vary(edit2, {"wght": this.value});
    });

    $("#change_wdth2").on('input', function(){
        vary(edit2, {"wdth": this.value});
    });

    $("#change_opsz2").on('input', function(){
        vary(edit2, {"opsz": this.value});
    });

    $("#change_shift2").on('input', function(){
        edit2.offset({"left": this.value});
    });

    // show/hide controls for edit2
    $("#view_layer").click(function(){
        $(".red").toggle();
        $(".red .range-slider__range").toggle();
        edit2.toggle();
        if($(this).prop("checked")) {
            edit.attr("contenteditable", false);
            edit2.attr("contenteditable", true);
            edit2.html(edit.text());
        } 
        else {
            edit.attr("contenteditable", true);
        }
    });
    
    // sync content between edit and edit2
    edit2.keyup(function(){
        edit.html(edit2.text());
    });

});
