var $ = django.jQuery;

$(document).ready(function() {
  
  var soma_total =  function() {
        var total=0;
        $("td.valor>input").each(function() {
            total += Number($(this).val());
        });
        $("#id_valor_total").val(total);
  }; 
 
  $("td.valor>input").live("blur", soma_total ); 
  $('tbody > tr[id*=itemservico]').parent('tbody').bind("DOMSubtreeModified", soma_total )
})



