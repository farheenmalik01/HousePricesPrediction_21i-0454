import { Router } from 'express';
const router = Router();

router.get('/', (req, res) => {
  res.json({ message: 'List of users' });
});

router.get('/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ message: `Details of user with ID ${userId}` });
});

router.post('/', (req, res) => {
  res.json({ message: 'User created' });
});

router.put('/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ message: `User with ID ${userId} updated` });
});

router.delete('/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ message: `User with ID ${userId} deleted` });
});

export default router;
