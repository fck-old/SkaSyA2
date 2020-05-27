$(document).ready(function() {
    $("#button-now").click(function() {
        var d = new Date();
        $("#datetime").val(
            d.getFullYear() + "-" + ("0"+(d.getMonth()+1)).slice(-2) + "-" +
            ("0" + d.getDate()).slice(-2) + "T" + ("0" + d.getHours()).slice(-2) +
            ":" + ("0" + d.getMinutes()).slice(-2)
        );
    });
    
    $("#percentdone").change(function(event) {
        $("#percent-label").text(event.target.value + "%");
    });
    
    $("#percent-label").text($("#percentdone").val() + "%");
});
