'use strict';

const { Model } = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class Patient extends Model {}

  Patient.init({
    firstName: DataTypes.STRING,
    lastName: DataTypes.STRING,
    dateOfBirth: DataTypes.DATE,
    email: DataTypes.STRING,
    phoneNumber: DataTypes.STRING,
    address: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'Patient',
  });

  return Patient;
};
