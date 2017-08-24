from django.test import TestCase
from .utils import create_paper

class PaperTest(TestCase):
    def test_get_source_url(self):
        paper = create_paper(arxiv_id='1708.03312v1')
        self.assertEqual(paper.get_source_url(), 'https://arxiv.org/e-print/1708.03312v1')