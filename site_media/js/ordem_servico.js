var $ = django.jQuery;

$(document).ready(function() {
  $("td.valor>input").bind("focus", function() {
    $("td.valor>input").each(function() {
        $(this).blur(function() {
            var total=0;
            $("td.valor>input").each(function() {
                total += Number($(this).val());
            });
            $("#id_valor_total").val(total);
        });
    });
  });  
})

