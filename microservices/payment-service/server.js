const express = require('express');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.PORT || 5001;

app.use(cors());
app.use(express.json());

// In-memory mock database for transactions
const transactions = [];

// Process Payment Endpoint
app.post('/api/payments/process', (req, res) => {
    const { amount, bookingId, paymentMethod } = req.body;

    if (!amount || !bookingId) {
        return res.status(400).json({ error: 'Amount and bookingId are required.' });
    }

    // Simulate payment processing logic (e.g., calling Stripe API)
    const isSuccess = Math.random() > 0.1; // 90% success rate

    const transaction = {
        transactionId: uuidv4(),
        bookingId,
        amount,
        paymentMethod: paymentMethod || 'credit_card',
        status: isSuccess ? 'COMPLETED' : 'FAILED',
        timestamp: new Date()
    };

    transactions.push(transaction);

    if (isSuccess) {
        return res.status(200).json({ message: 'Payment processed successfully', transaction });
    } else {
        return res.status(400).json({ error: 'Payment failed due to insufficient funds or bank error', transaction });
    }
});

// Get Payment Status Endpoint
app.get('/api/payments/:transactionId', (req, res) => {
    const { transactionId } = req.params;
    const transaction = transactions.find(t => t.transactionId === transactionId);

    if (!transaction) {
        return res.status(404).json({ error: 'Transaction not found' });
    }

    return res.status(200).json(transaction);
});

// Global Error Handler
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Internal Microservice Error' });
});

if (require.main === module) {
    app.listen(PORT, () => console.log(`Payment Microservice running on port ${PORT}`));
}

module.exports = app;
