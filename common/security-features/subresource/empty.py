import os, sys
from wptserve.utils import isomorphic_decode
subresource = __import__("common.security-features.subresource.subresource")

def generate_payload(server_data):
    return u''

def main(request, response):
    subresource.respond(request,
                        response,
                        payload_generator = generate_payload,
                        access_control_allow_origin = b"*",
                        content_type = b"text/plain")
