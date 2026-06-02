const express = require('express');
const router = express.Router();

// Mock Data
let services = [
    { id: 1, name: 'Electrician', category: 'Home Services', price: 50 },
    { id: 2, name: 'Plumber', category: 'Home Services', price: 60 }
];

router.get('/', (req, res) => {
    res.json(services);
});

module.exports = router;
