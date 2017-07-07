$(document).ready(function(){
    let weddingPlanner = $("#clickable");
    weddingPlanner.on("click", function(){
        window.location.href="/menu/";
        return false;
    })

    let inputs = $("input");
    $(inputs).addClass("form-control");

    let toPay = $("#id_to_pay");
    // $(toPay.attr('disabled','disabled'));
    let toPayParent = $("#id_to_pay").parent();
    toPayParent.hide();
    let cost = $("#id_cost");
    let paid = $("#id_paid");
    $("#add").click(function(){
        $(toPay).val(cost.val()-paid.val())
    });

    let currUser = $("#curr-user").attr("name"); // user.id
    let selectUser = $("#id_user"); // oznaczenie całego selecta
    let selectUserParent = $(selectUser.parent());
    selectUserParent.hide();
    selectUser.html(""); // wyczyszczenie selecta z option
    selectUser.append("<option selected value='"+currUser+"'></option>"); // dodanie aktywnego użytkownika do option

    let weddText = $("#id_wedding option").filter(function(){
        return $(this).text() === currUser;
    }).first().attr("value")

    let selectWedding = $("#id_wedding");
    let selectWeddingParent = $(selectWedding.parent());
    selectWeddingParent.hide();
    selectWedding.html("");
    selectWedding.append("<option selected value='"+weddText+"'></option>");

});
