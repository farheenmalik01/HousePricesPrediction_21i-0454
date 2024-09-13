
module.exports = (req, res) => {
    const { method } = req;
  
    switch (method) {
      case 'GET':

        res.status(200).json({ message: 'Fetch user data' });
        break;
      case 'POST':

        res.status(201).json({ message: 'User created' });
        break;

      default:
        res.setHeader('Allow', ['GET', 'POST']);
        res.status(405).end(`Method ${method} Not Allowed`);
    }
  };
  