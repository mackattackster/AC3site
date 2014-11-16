$(document).ready(function() {
    $("#bEdit").click(function () {
        $(".info").toggle();
        $(".edit").toggle();
        $("#userselect").prop('disabled', true)

        $("#ifirst").val($("#lfirst").text())
        $("#ilast").val($("#llast").text())
        $("#ipin").val($("#lpin").text())
        $("#iemail").val($("#lemail").text())
        $("#iphone").val($("#lphone").text())
    });

    $("#bCancel").click(function () {
        $(".info").toggle();
        $(".edit").toggle();
        $("#userselect").prop('disabled', false)
        return false;
    });
});

function Userselect(){
    $("select option:selected").each(function () {
        $("#name").val($(this).val());
        var s = {'name': $(this).val()}
        jQuery.ajax({
            type: "GET",
            url: '../profileAjax/',
            dataType: "text",
            data: s,
            beforesend: function(){
                $("#bEdit").prop('disabled', true)
            },
            success: function(data) {
                data = JSON.parse(data);
                fillUserData(data);
                $("#bEdit").prop('disabled', false)
            }
        })
    });
}

function fillUserData(data){
    $("#id").text(data.id)
    $("#isStaff").text(data.is_staff)
    $("#lfirst").text(data.first)
    $("#llast").text(data.last)
    $("#lpin").text(data.pin)
    $("#lemail").text(data.email)
    $("#lphone").text(data.phone)
}

