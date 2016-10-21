from tests.base import BaseCase
import json
import base64
import os
import tempfile


class PdfTest(BaseCase):
    def setUp(self):
        super(PdfTest, self).setUp()
        self.output = tempfile.NamedTemporaryFile().name

    def testShouldConvertHtmlToPdf(self):
        data = {
            'base64_html': base64.b64encode('<p>Hello World</p>'),
            'pin': ''
        }
        response = self.client.post('/html2pdf', data=json.dumps(data),
                                    content_type='application/json')
        json_data = json.loads(response.data)
        with open(self.output, 'w') as f:
            f.write(base64.b64decode(json_data['base64_pdf']))
            f.close()

        self.assertEqual(200, response.status_code)
        self.assertTrue(os.path.exists(self.output))

    def testShouldConvertHtmlToPdfWithPin(self):
        data = {
            'base64_html': base64.b64encode('<p>Hello World</p>'),
            'pin': '1234'
        }
        response = self.client.post('/html2pdf', data=json.dumps(data),
                                    content_type='application/json')
        json_data = json.loads(response.data)
        with open(self.output, 'w') as f:
            f.write(base64.b64decode(json_data['base64_pdf']))
            f.close()

        self.assertEqual(200, response.status_code)
        self.assertTrue(os.path.exists(self.output))

    def tearDown(self):
        super(PdfTest, self).tearDown()
        print self.output
        os.unlink(self.output)
