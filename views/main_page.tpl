%include('table_style.tpl')
<h3>Overview</h3>
<p>
<table border="1">
    %for k, v in action_list.items():
        <tr>
            <th><a href="/{{k}}">{{k}} nodes</a></th>
            <td>{{v}}</td>
        </tr>
        <p>
    %end
</table>
