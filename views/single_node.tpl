%include('table_style.tpl')
<table border="1">
    %for k, v in rows.items():
        <tr>
            %if k == 'latest_report_hash':
                <th>{{k}}</th>
                <td><a href="/report/{{v}}">{{v}}</a></td>
            %else:
                <th>{{k}}</th>
                <td>{{v}}</td>
            %end
        </tr>
    %end
</table>
<p>
