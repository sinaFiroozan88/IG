$(document).ready(function () {
    $('#id_crystal_water_rawmat').change (function () {
        $("#id_purity_rm").val(($("#id_crystal_water_rawmat").val() * 4.7785).toFixed(3))
    })
})

$(document).ready(function (){
    $('[data-toggle="tooltip"]').tooltip({html:true, placement:'bottom', trigger:'hover'});
})

$(document).ready(function (){
    $('#id_remarks').focusin(function (){
        $("#remarklable").width("350px")
    })
    $("#id_remarks").focusout(function (){
        $("#remarklable").width("175px")
    })
})

$(document).ready(function () {
    $(".nonconf").hide();
    $("#id_non_conformity").click(function() {
        if ($(this).is(":checked")) {
            $(".nonconf").show(300);
        } else {
            $(".nonconf").hide(200);
        }
    })
})

