from sanic import Sanic
import json as j
app = Sanic()
from sanic.response import json
from console_logging.console import Console
console = Console()

routing_table = dict()
with open('paths.json') as f:
    for d in j.load(f): routing_table[d["passkey"]] = d["url"]

console.info("Compiled routing table of %d routes." % len(routing_table.keys()))

@app.middleware('response')
async def all_cors(r, s):
    s.headers['Access-Control-Allow-Origin'] = '*'
    s.headers['Access-Control-Allow-Headers'] = '*'

@app.route("/knock", methods=['POST', 'OPTIONS'])
async def whos_there(r):
    if r.method == 'OPTIONS': return json({},  status=200)
    if 'name' not in r.json.keys(): return json({}, status=500)
    console.log("%s@%s is knocking." % (r.json['name'], r.ip))
    if r.json['name'] in routing_table.keys():
        p = routing_table[r.json['name']]
        console.log("%s is answering." % p)
        return json({ "url" : p }, status=200)
    return json({}, status=401)

if __name__ == "__main__":
    console.success("Starting server.")
    app.run(host="0.0.0.0", port=7734)
