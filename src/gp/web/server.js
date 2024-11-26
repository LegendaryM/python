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
      let new_img = 0;
      if (file.indexOf('_new') > 0) {
        file = file.replace('_new', '')
        new_img = 1
      }
        
      const statusFilePath = path.join(imagesDir, `${file}.txt`);
      let status = '';
      if (fs.existsSync(statusFilePath)) {
          status = fs.readFileSync(statusFilePath, 'utf8').trim();
      }
      return { name: file, status,  new_img};
  });

    res.render('index', { images: imageData });
  });
});

function readFilesFromDirectory() {
  const filesData = [];
  const files = fs.readdirSync(imagesDir).filter(file => path.extname(file) === '.txt');

  files.forEach(file => {
    const content = fs.readFileSync(path.join(imagesDir, file), 'utf8');
    const fileNameWithoutExtension = path.basename(file, '.txt');
    filesData.push({ name: fileNameWithoutExtension, content: content });
  });

  return filesData;
}

app.get('/t', (req, res) => {
  const filesData = readFilesFromDirectory();
  res.render('index1', { filesData, 'searchTerm':'' });
});

app.post('/search', (req, res) => {
  const searchTerm = req.body.searchTerm;
  const filesData = readFilesFromDirectory();
  const filteredData = filesData.filter(file => file.content.includes(searchTerm) );
  // const filteredData = filesData.map(file => ({
  //   name: file.name,
  //   content: file.content.includes(searchTerm) ? file.content : ''
  // }));
  res.render('index1', { filesData: filteredData, searchTerm });
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

const os = require('os');

// 获取网络接口信息
const networkInterfaces = os.networkInterfaces();

// 遍历所有网络接口
for (const interfaceName in networkInterfaces) {
    const addresses = networkInterfaces[interfaceName];
    for (const addressInfo of addresses) {
        // 检查IPv4地址并且不是内部地址（例如127.0.0.1）
        if (addressInfo.family === 'IPv4' && !addressInfo.internal) {
            console.log(`IP Address: ${addressInfo.address}`);
        }
    }
}


app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
