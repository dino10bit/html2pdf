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
            'base64_html': base64.encodestring('<p>Hello World</p>')
        }
        response = self.client.post('/html2pdf', data=json.dumps(data),
                                    content_type='application/json')
        json_data = json.loads(response.data)
        with open(self.output, 'w') as f:
            f.write(base64.decodestring(json_data['base64_pdf']))

        self.assertEqual(200, response.status_code)
        self.assertTrue(os.path.exists(self.output))

    def tearDown(self):
        super(PdfTest, self).tearDown()
        os.unlink(self.output)
