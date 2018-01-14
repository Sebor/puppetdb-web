%include('table_style.tpl')
<h2>The {{state}} nodes:</h2>

<table border="1">
%for row in rows:
  <tr>
      <td><a href="/node/{{row}}">{{row}}</a></td>
  </tr>
%end
<h3>Total nodes: {{count}}</h3>
</table>