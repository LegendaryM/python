const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const imagesDir = 'E:/1gp/png';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  fs.readdir(imagesDir, (err, files) => {
    if (err) {
      return res.status(500).send('Unable to scan directory: ' + err);
    }
    // Filter out non-image files
    const images = files.filter(file => {
      const ext = path.extname(file).toLowerCase();
      return ext === '.jpg' || ext === '.jpeg' || ext === '.png' || ext === '.gif';
    });

    const imageData = images.map(file => {
      const statusFilePath = path.join(imagesDir, `${file}.txt`);
      let status = '';
      if (fs.existsSync(statusFilePath)) {
          status = fs.readFileSync(statusFilePath, 'utf8').trim();
      }
      return { name: file, status };
  });

    res.render('index', { images: imageData });
  });
});

app.post('/select-image', (req, res) => {
  const selectedImage = req.body.imageName;
  const value = req.body.value;
  fs.writeFile(path.join(imagesDir, selectedImage + '.txt'), value , (err) => {
    if (err) {
      return res.status(500).send('Unable to write file: ' + err);
    }
    res.send('Image name written to file successfully');
  });
});

app.use('/images', express.static(imagesDir));

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
