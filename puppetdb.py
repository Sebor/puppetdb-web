import requests
from bottle import Bottle, template, abort

ListQueries = {
    'inactive': '["=", "node_state", "inactive"]',
    'changed': '["=", "latest_report_status", "changed"]',
    'failed': '["=", "latest_report_status", "failed"]',
    'active': '["=", "node_state", "active"]',
}

CountQueries = {
    #Full example:
    #["extract", [["function","count"]], ["and", ["=", "latest_report_status", "failed"]]]
    'count': '["extract", [["function","count"]]'
}

baseurl = 'http://localhost:8080/pdb/query/v4'

app = application = Bottle()

@app.route('/')
def MainPage():
    action_list = []
    count_list =[]
    for k, v in ListQueries.items():
        action_list.append(k)
        q = '{}, ["and", {}]]'.format(CountQueries['count'], v)
        params = dict(
            query=q
        )
        r = requests.get('{}/nodes'.format(baseurl), params=params)
        count_list.append(r.json()[0]['count'])
    general_dict = dict(zip(action_list, count_list))
    return template('main_page', action_list=general_dict)


@app.route('/:state')
def NodeList(state):
    if state not in ListQueries:
        return abort(404, 'Page not found')
    else:
        params = dict(
            query=ListQueries[state],
        )
    r = requests.get('{}/nodes'.format(baseurl), params=params)
    data = r.json()
    nodelist = [i['certname'] for i in data]
    output = template('all_nodes', rows=nodelist, state=state, count=len(nodelist))
    return output


@app.route('/node/:nodename')
def NodeDef(nodename):
    r = requests.get('{}/nodes/{}'.format(baseurl, nodename))
    data = r.json()
    output = template('single_node', rows=data)
    return output


@app.route('/report/:reporthash')
def GetReport(reporthash):
    r = requests.get('{}/reports/{}/logs'.format(baseurl, reporthash))
    data = r.json()
    return {'log': data}


if __name__ == '__main__':
    debug = 'True'
    reloader = 'True'
    port = 8090
    app.run(debug=debug, port=port, reloader=reloader)
