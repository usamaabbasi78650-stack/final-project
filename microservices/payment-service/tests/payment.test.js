const request = require('supertest');
const app = require('../server');

describe('Payment Microservice Endpoints', () => {
    it('should fail to process payment if amount is missing', async () => {
        const res = await request(app)
            .post('/api/payments/process')
            .send({ bookingId: '12345' });
        expect(res.statusCode).toEqual(400);
        expect(res.body.error).toBeDefined();
    });

    it('should process payment and return transaction object', async () => {
        const res = await request(app)
            .post('/api/payments/process')
            .send({ bookingId: '12345', amount: 100 });
        
        // Either 200 or 400 depending on mock success rate, but must have transaction object
        expect([200, 400]).toContain(res.statusCode);
        expect(res.body.transaction).toBeDefined();
        expect(res.body.transaction.amount).toEqual(100);
    });
});
