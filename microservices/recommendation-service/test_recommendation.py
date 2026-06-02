import unittest
import json
from app import app

class TestRecommendationService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/health')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')

    def test_recommendation_by_category(self):
        payload = {
            "preferredCategory": "Utility Services"
        }
        response = self.app.post('/api/recommend', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertGreater(len(data['recommendations']), 0)
        
        # The top recommendation should match our preferred category
        self.assertEqual(data['recommendations'][0]['category'], 'Utility Services')

    def test_recommendation_by_search_query(self):
        payload = {
            "searchQuery": "emergency electrician"
        }
        response = self.app.post('/api/recommend', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        # The top recommendation should be the Emergency Electrician
        self.assertEqual(data['recommendations'][0]['name'], 'Emergency Electrician')

if __name__ == '__main__':
    unittest.main()
