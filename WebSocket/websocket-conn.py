import websocket
from websocket import create_connection
import ssl
import json



def conn(senseHost, userDirectory, userId, privateKeyPath):
    url = "wss://" + senseHost + ":4747/app"  # valid
    certs = ({"ca_certs": privateKeyPath + "root.pem",
              "certfile": privateKeyPath + "client.pem",
              "keyfile": privateKeyPath + "client_key.pem",
              "cert_reqs":ssl.CERT_REQUIRED,
              "server_side": False
              })
    ssl.match_hostname = lambda cert, hostname: True
    ws = create_connection(url, sslopt=certs,
                                header={'X-Qlik-User: UserDirectory=%s; UserId=%s'% (userDirectory, userId)})
    
    session = ws.recv()
    return session    


c = conn("blablah.com","XYZ","ME","path/to/cert/")
print("Session created")
#header_user = {'header_user': 'dilip_rathod'}
#header_user = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJkaWxpcF9yYXRob2QiLCJ1c2VyRGlyZWN0b3J5IjoiRE9NQUlOIn0.c_Tw6ipn5DgbehawF1z_QBMGlsnNAlxOD7a91T7raAlCwnvNE1tbJjsWHn-VJgIkFarN3HnPjijp-g66wi3ijBfSowYD7K_oxLRO6WpuHAwFzGrsVtfGOsAgejo7GFESiS2xmoO1vn3Fk-i_6clwaK48lHxH32aoqteSwyBniVs_Ah-G_RjvSQRCuRRG6O-wQlaUsuAAXiGRa0h8qJN9Tz5NzXmeDSjdfzI-yoIHlIph42B9X8-fgnUjn1E5Pj69yp3aXC-P62LxcaDjDVbypsAbKg4lw_SxeS1peVhGY0gXH8J7O8WG1vHzLB3VJU_Ozj7o34trLdv6Rye0oIeUlw'}

#ws = websocket.create_connection("wss://qlikserver1.domain.local/hdr/app/", sslopt={"cert_reqs": ssl.CERT_NONE},header=header_user)

#ws = websocket.create_connection("wss://104.199.79.190:4747/app/", sslopt={"cert_reqs": ssl.CERT_NONE},header=header_user)

ws.send(json.dumps({
	"handle": -1,
	"method": "GetDocList",
	"params": [],
	"outKey": -1,
	"id": 1
}))

result = ws.recv()

while result:
    result=ws.recv()
    y = json.loads(result)
    print(y)

ws.close()