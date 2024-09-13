// api/posts.js
module.exports = (req, res) => {
    const { method } = req;
  
    switch (method) {
      case 'GET':
        // Logic to fetch posts data
        res.status(200).json({ message: 'Fetch posts data' });
        break;
      case 'POST':
        // Logic to create a new post
        res.status(201).json({ message: 'Post created' });
        break;
      // Handle other HTTP methods if needed
      default:
        res.setHeader('Allow', ['GET', 'POST']);
        res.status(405).end(`Method ${method} Not Allowed`);
    }
  };
  