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
  $('tbody > tr[id*=itemservico]').parent('tbody').bind("DOMSubtreeModified", soma_total );
  
  $("input[name=_save]").click(function() {
     if ($('select[name=situacao] :selected').val() === "naoiniciado") {
         confirm('Imprimir Ordem de Serviço ?') && $('<input type="hidden" name="imprimir" value="s">').appendTo('form');
     }
  });
})



