from .utils import post_pingpong_webhook, post_pr_webhook, extract_payload
import archie
import logging
import os, sys
import json
import unittest

class test_payload_server(unittest.TestCase):
    def test_webhooks_ok(self):
        """
        Test that the Uncle Archie webhook server returns status 200
        """
        archie.webapp.app.config['debug'] = True
        archie.webapp.app.config['DEBUG'] = True
        archie.webapp.app.config['TESTING'] = True
        client = archie.webapp.app.test_client()
        archie.webapp.app.set_payload_handler('')
    
        r = post_pr_webhook(client)
        self.assertEqual(r.status_code,200)
    
    def test_ping_webhook(self):
        """
        Test that the Uncle Archie webhook server plays ping pong
        """
        archie.webapp.app.config['DEBUG'] = True
        archie.webapp.app.config['TESTING'] = True
        client = archie.webapp.app.test_client()
        archie.webapp.app.set_payload_handler('')
    
        r = post_pingpong_webhook(client)
        self.assertEqual(r.status_code,200)
    
        d = extract_payload(r)
        self.assertIn('msg',d.keys())
        self.assertEqual(d['msg'],'pong')
    