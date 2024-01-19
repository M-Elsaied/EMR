const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
require('dotenv').config();

const exampleUser = {
  id: 1,
  username: 'admin',
  role: 'admin'
};

// Hash the actual password and store it in the hashedPassword variable
const plainPassword = 'password';
const saltRounds = 10; // The number of salt rounds (a higher value is more secure)

const hashedPassword = bcrypt.hashSync(plainPassword, saltRounds);

const login = (req, res) => {
  const { username, password } = req.body;
  if (username === exampleUser.username && bcrypt.compareSync(password, hashedPassword)) {
    const payload = { sub: exampleUser.id, role: exampleUser.role };
    const token = jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.status(200).json({ token });
  } else {
    res.status(401).send('Username or password incorrect');
  }
};

module.exports = {
  login
};
