const { Patient } = require('../../models');

const createPatient = async (req, res) => {
  try {
    const patient = await Patient.create(req.body);
    res.status(201).json(patient);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

const getAllPatients = async (req, res) => {
  try {
    const patients = await Patient.findAll();
    res.status(200).json(patients);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const getPatientById = async (req, res) => {
  try {
    const patient = await Patient.findByPk(req.params.id);
    if (patient) {
      res.status(200).json(patient);
    } else {
      res.status(404).json({ message: 'Patient not found' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const updatePatient = async (req, res) => {
  try {
    const [updatedRows] = await Patient.update(req.body, {
      where: { id: req.params.id }
    });
    if (updatedRows) {
      const updatedPatient = await Patient.findByPk(req.params.id);
      res.status(200).json(updatedPatient);
    } else {
      res.status(404).json({ message: 'Patient not found' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const deletePatient = async (req, res) => {
  try {
    const deleted = await Patient.destroy({
      where: { id: req.params.id }
    });
    if (deleted) {
      res.status(204).send();
    } else {
      res.status(404).json({ message: 'Patient not found' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

module.exports = {
  createPatient,
  getAllPatients,
  getPatientById,
  updatePatient,
  deletePatient
};
