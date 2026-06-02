const request = require('supertest');
const app = require('../server');

describe('Service Endpoints', () => {
    it('should return a list of services', async () => {
        const res = await request(app).get('/api/services');
        expect(res.statusCode).toEqual(200);
        expect(res.body).toHaveLength(2);
        expect(res.body[0]).toHaveProperty('name', 'Electrician');
    });
});
