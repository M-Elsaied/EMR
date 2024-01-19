const express = require('express');
const { authenticateJWT } = require('../middleware/authMiddleware');
const router = express.Router();
const patientsController = require('../controllers/patientsController');

router.post('/', authenticateJWT, patientsController.createPatient);
router.get('/', authenticateJWT, patientsController.getAllPatients);
router.get('/:id', authenticateJWT, patientsController.getPatientById);
router.put('/:id', authenticateJWT, patientsController.updatePatient);
router.delete('/:id', authenticateJWT, patientsController.deletePatient);

module.exports = router;
