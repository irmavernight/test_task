from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
import logging


def InterestRateCalculation(loan, period_months, interest):
    cumulative_interest=0
    ending_balance = loan
    interest = interest/ 100
    nper = period_months
    interest_monthly = interest/12
    numerator = interest_monthly*((1+interest_monthly)**nper)
    denominator = (1+interest_monthly)**nper-1
    payment_total = round(loan*numerator/denominator,2)
            
    for i in range (nper):
        interesrt_paid = round(ending_balance*interest_monthly,2)
        principal_paid = round(payment_total-interesrt_paid,2)
        ending_balance -=principal_paid
        cumulative_interest +=interesrt_paid
    return(round(cumulative_interest,2))

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    def do_GET(self):
        self._set_headers()
        self.wfile.write(b'Try POST')
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype = self.headers.get('content-type')
            
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
    
        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        resp = {"cumulative_interest": InterestRateCalculation(message["loan"],message["period_months"],message["interest"])}
        self._set_headers()
        self.wfile.write(str.encode(json.dumps(resp)))
        
def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
if __name__ == "__main__":
    run(port=int(5000))
