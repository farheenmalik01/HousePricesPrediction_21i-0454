import { Router } from 'express';
const router = Router();

router.get('/', (req, res) => {
  res.json({ message: 'List of posts' });
});

router.get('/:id', (req, res) => {
  const postId = req.params.id;
  res.json({ message: `Details of post with ID ${postId}` });
});

router.post('/', (req, res) => {
  res.json({ message: 'Post created' });
});

router.put('/:id', (req, res) => {
  const postId = req.params.id;
  res.json({ message: `Post with ID ${postId} updated` });
});

router.delete('/:id', (req, res) => {
  const postId = req.params.id;
  res.json({ message: `Post with ID ${postId} deleted` });
});

export default router;
