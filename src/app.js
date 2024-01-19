const express = require('express');
const patientRoutes = require('./routes/patientRoutes');
const authRoutes = require('./routes/authRoutes');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.use('/api/patients', patientRoutes);
app.use('/api/auth', authRoutes);

app.get('/ping', (req, res) => {
    res.status(200).send('pong');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

module.exports = app;
