$(document).ready(function(){
    let weddingPlanner = $("#clickable");
    weddingPlanner.on("click", function(){
        window.location.href="/menu/";
        return false;
    })
    
    let inputs = $("input");
    $(inputs).addClass("form-control");
    let toPay = $("#id_to_pay");
    let toPayParent = $(toPay.parent());
    toPayParent.hide();

    let cost = $("#id_cost");
    let paid = $("#id_paid");
    $("#add").click(function(){
        $(toPay).val(cost.val()-paid.val())
    })
});
